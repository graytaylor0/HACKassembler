#Taylor Gray

class Parser:
    
    def __init__(self, inFile):
        self.file = open(inFile, 'r')
        self.lines = self.file.readlines()
        self.removeWhiteSpace(self.lines)
        self.linesLeft = len(self.lines) + 1
        self.currentLine = -1
        self.currentCommand = None

    def removeWhiteSpace(self, lines):
        for i in range(len(lines)):
            lines[i] = lines[i].strip()

    def hasMoreCommands(self):
        return self.linesLeft > 0
    
    def advance(self):
        self.linesLeft -= 1
        if (self.hasMoreCommands()):
            self.currentLine += 1
            self.currentCommand = self.lines[self.currentLine]
    
    def commandType(self):
        if '/' in self.currentCommand:
            indexOfSlash = self.currentCommand.find('/')
            self.currentCommand = self.currentCommand[:indexOfSlash]
            self.currentCommand = self.currentCommand.strip()
        if len(self.currentCommand) == 0 or self.currentCommand[0] == '/': 
            self.advance()
            return self.commandType()
        elif self.currentCommand[0] == '(':
            return 'L_COMMAND'
        elif self.currentCommand[0] == '@':
            return 'A_COMMAND'
        else:
            return 'C_COMMAND'
    
    def symbol(self):
        if self.commandType() == 'A_COMMAND':
            return self.currentCommand[1:]
        else:
            return self.currentCommand[1:-1]

    def dest(self):
        indexToStop = self.currentCommand.find('=')
        if indexToStop == -1:
            return ''
        else:
            return self.currentCommand[:indexToStop]

    def comp(self):
        indexToStart = self.currentCommand.find('=') + 1
        indexToStop = self.currentCommand.find(';')
        if indexToStop == -1:
            indexToStop = None
        return self.currentCommand[indexToStart:indexToStop]

    def jump(self):
        indexToStart = self.currentCommand.find(';')
        if indexToStart == -1:
            return ''
        else:
            return self.currentCommand[indexToStart + 1:] 

    def parseMain(self):
        parsedCode = []
        self.advance()
        while self.hasMoreCommands():
            if self.commandType() == 'A_COMMAND':
                parsedCode.append(self.symbol())
            elif self.commandType() == 'L_COMMAND':
                parsedCode.append('(' + self.symbol())
            else:
                parsedCode.append(self.dest() + ',' + self.comp() + ',' + self.jump())
            self.advance()
        self.file.close()
        return parsedCode







    


    