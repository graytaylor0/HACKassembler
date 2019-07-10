#Taylor Gray

import sys
import Parser
import Code
import SymbolTable

	
def main():
	symbolTable = SymbolTable.SymbolTable()
	symbolTable.addEntry('SP', 0)
	symbolTable.addEntry('LCL', 1)
	symbolTable.addEntry('ARG', 2)
	symbolTable.addEntry('THIS', 3)
	symbolTable.addEntry('THAT', 4)
	for i in range(16):
		symbolTable.addEntry('R' + str(i), i)
	symbolTable.addEntry('SCREEN', 16384)
	symbolTable.addEntry('KBD', 24576)
	indexToStop = sys.argv[1].find('.')
	hackFile = open(sys.argv[1][:indexToStop] + '.hack', 'w')
	parser = Parser.Parser(sys.argv[1])
	parsedCode = parser.parseMain()
	#FirstPass
	assemblerIndex = 0
	elementsToRemove = []
	for element in parsedCode:
		if element[0] == '(':
			if not symbolTable.contains(element):
				symbolTable.addEntry(element[1:], assemblerIndex)
				elementsToRemove.append(element)
		else:
			assemblerIndex += 1
	parsedCode = [elem for elem in parsedCode if elem not in elementsToRemove]
	startingAddressForVars = 16
	for element in parsedCode:
		if element.isnumeric():
			element = int(element)
			binaryInstruction = bin(element)[2:]
			while (len(binaryInstruction) != 16):
				binaryInstruction = '0' + binaryInstruction
			hackFile.write(binaryInstruction + '\n')
		elif symbolTable.contains(element):
			locationInTable = symbolTable.GetAddress(element)
			binaryInstruction = bin(locationInTable)[2:]
			while (len(binaryInstruction) != 16):
				binaryInstruction = '0' + binaryInstruction
			hackFile.write(binaryInstruction + '\n')
		elif len(element.split(',')) < 3:
			symbolTable.addEntry(element, startingAddressForVars)
			binaryInstruction = bin(startingAddressForVars)[2:]
			while len(binaryInstruction) != 16:
				binaryInstruction = '0' + binaryInstruction
			hackFile.write(binaryInstruction + '\n')
			startingAddressForVars += 1
		else:
			destCompJump = element.split(',')
			dest = Code.dest(destCompJump[0])
			comp = Code.comp(destCompJump[1])
			jump = Code.jump(destCompJump[2])
			binaryInstruction = '111' + comp + dest + jump
			hackFile.write(binaryInstruction + '\n')
	hackFile.close()
	

main()