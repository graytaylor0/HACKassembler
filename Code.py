#Taylor Gray

def dest(command):
        if command == '':
            return '000'
        elif command == 'M':
            return '001'
            
        elif command == 'D':
            return '010'
            
        elif command == 'MD':
            return '011'
            
        elif command == 'A':
            return '100'
            
        elif command == 'AM':
            return '101'
            
        elif command == 'AD':
            return '110'
            
        else:
            return '111'

def comp(command):
        if command == '0':
            return '0101010'
        elif command == '1':
            return '0111111'
        elif command == '-1':
            return '0111010'
        elif command == 'D':
            return '0001100'
        elif command == 'A':
            return '0110000'
        elif command == '!D':
            return '0001111'
        elif command == '!A':
            return '0110001'
        elif command == '-D':
            return '0001111'
        elif command == '-A':
            return '0110011'
        elif command == 'D+1':
            return '0011111'
        elif command == 'A+1':
            return '0110111'
        elif command == 'D-1':
            return '0001110'
        elif command == 'A-1':
            return '0110010'
        elif command == 'D+A':
            return '0000010'
        elif command == 'D-A':
            return '0010011'
        elif command == 'A-D':
            return '0000111'
        elif command == 'D&A':
            return '0000000'
        elif command == 'D|A':
            return '0010101'
        elif command == 'M':
            return '1110000'
        elif command == '!M':
            return '1110001'
        elif command == '-M':
            return '1110011'
        elif command == 'M+1':
            return '1110111'
        elif command == 'M-1':
            return '1110010'
        elif command == 'D+M':
            return '1000010'
        elif command == 'D-M':
            return '1010011'
        elif command == 'M-D':
            return '1000111'
        elif command == 'D&M':
            return '1000000'
        elif command == 'D|M':
            return '1010101'


def jump(command):
        if command == '':
            return '000'
        elif command == 'JGT':
            return '001'
        elif command == 'JEQ':
            return '010'
        elif command == 'JGE':
            return '011'
        elif command == 'JLT':
            return '100'
        elif command == 'JNE':
            return '101'
        elif command == 'JLE':
            return '110'
        elif command == 'JMP':
            return '111'

