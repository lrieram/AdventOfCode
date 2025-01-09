# -*- coding: utf-8 -*-

#Open file
file_name = 'input.txt'
file = open(file_name,mode='r')

#Read file
rules = []
for line in file:
    rules.append(line.strip().split(' => '))
    
molecule = rules[-1][0]
rules = rules[:-2]

#molecule = 'HOH'
#rules = [['e', 'O'], ['H', 'OH'], ['O', 'HH']]
    
def newMolecules(molecule, rules):
    new_molecules = set()
    for rule in rules:
        body = rule[0]
        head = rule[1]
        molecule_divided = molecule.split(body)
        for i in range(len(molecule_divided) - 1):
            new_molecule = ''
            for j in range(len(molecule_divided)-1):
                new_molecule += molecule_divided[j]
                if j == i:
                    new_molecule += head
                else:
                    new_molecule += body
            new_molecule += molecule_divided[-1]
            new_molecules.add(new_molecule)
    return new_molecules

#print(len(newMolecules(molecule, rules)))
#---------------------------- Part 2 ----------------------------
#Inspired by https://www.reddit.com/r/adventofcode/comments/3xflz8/comment/cy4etju/

atoms = set([rule[0] for rule in rules])


translated = molecule.replace('Rn', '(')
translated = translated.replace('Ar', ')')
translated = translated.replace('Y', ',')

#translate atoms to single characters
#The molecule does not use special characters
i = 200
for atom in atoms:
    translated = translated.replace(atom, chr(i))
    i += 1

#All atoms are translated except 'C' but len('C') = 1 so doesnt matter

print(len(translated) - 2 * translated.count('(') - 2 * translated.count(',') - 1)

