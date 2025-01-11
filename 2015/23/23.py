# -*- coding: utf-8 -*-

#Open file
file_name = 'input.txt'
file = open(file_name,mode='r')

#Read file
program = []
for line in file:
    program.append(line.strip())
    
def executeInstruction(instruction, a, b, ip):
    instruction = instruction.split(' ')
    operation = instruction[0]
    match operation:
        case 'hlf':
            register = instruction[1]
            if register == 'a':
                a = a // 2
            elif register == 'b':
                b = b // 2
            else:
                print('Invalid register for operation hlf in line ', ip, ' instruction: ', instruction)
                raise ValueError
            ip += 1
        case 'tpl':
            register = instruction[1]
            if register == 'a':
                a = a * 3
            elif register == 'b':
                b = b * 3
            else:
                print('Invalid register for operation tpl in line ', ip, ' instruction: ', instruction)
                raise ValueError
            ip += 1
        case 'inc':
            register = instruction[1]
            if register == 'a':
                a = a + 1
            elif register == 'b':
                b = b + 1
            else:
                print('Invalid register for operation inc in line ', ip, ' instruction: ', instruction)
                raise ValueError
            ip += 1
        case 'jmp':
            offset = instruction[1]
            ip += int(offset)
        case 'jie':
            #[:-1] to remove de ,
            register = instruction[1][:-1]
            offset = instruction[2]
            if register == 'a':
                reg_value = a
            elif register == 'b':
                reg_value = b
            else:
                print('Invalid register for operation jie in line ', ip, ' instruction: ', instruction)
                raise ValueError
            if reg_value % 2 == 0:
                ip += int(offset)
            else:
                ip += 1
        case 'jio':
            #[:-1] to remove de ,
            register = instruction[1][:-1]
            offset = instruction[2]
            if register == 'a':
                reg_value = a
            elif register == 'b':
                reg_value = b
            else:
                print('Invalid register for operation jio in line ', ip, ' instruction: ', instruction)
                raise ValueError
            if reg_value == 1:
                ip += int(offset)
            else:
                ip += 1
    return a, b, ip 
            
            
def executeProgram(program):
    a = 0
    b = 0
    ip = 0
    while ip < len(program):
        #Fetch
        instruction = program[ip]
        #Decode and Execute
        a, b, ip = executeInstruction(instruction, a, b, ip)
    return a, b

reg_a, reg_b = executeProgram(program)
print(reg_b)
#---------------------------- Part 2 ----------------------------

def executeProgramPart2(program):
    a = 1
    b = 0
    ip = 0
    while ip < len(program):
        #Fetch
        instruction = program[ip]
        #Decode and Execute
        a, b, ip = executeInstruction(instruction, a, b, ip)
    return a, b

reg_a, reg_b = executeProgramPart2(program)
print(reg_b)