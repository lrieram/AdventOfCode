# -*- coding: utf-8 -*-

#Open file
file_name = 'input.txt'
file = open(file_name,mode='r')

#Read file
instructions = []
for line in file:
    instructions.append(line.strip())

    
class Gate:
    
    def __init__(self, ins, out):
        self.ins = ins
        self.out = out
    
    def canProvide(self, wire_values):
        keys = wire_values.keys()
        for wire in self.ins:
            #It can be a fixed value
            try:
                int(wire)
            except:
                if wire not in keys:
                    return False
        return True
    
    def getValue(self, wire, wire_values):
        try:
            value = int(wire)
        except:
            value = wire_values.get(wire)
        return value

class ANDgate(Gate):
        
    def update(self, wire_values, wire_receivers):
        if self.canProvide(wire_values):
            value = self.getValue(self.ins[0], wire_values) & self.getValue(self.ins[1], wire_values)
            wire_values[self.out] = value
            for gate in wire_receivers.get(self.out, []):
                gate.update(wire_values, wire_receivers)
        
class ORgate(Gate):
        
    def update(self, wire_values, wire_receivers):
        if self.canProvide(wire_values):
            value = self.getValue(self.ins[0], wire_values) | self.getValue(self.ins[1], wire_values)
            wire_values[self.out] = value
            for gate in wire_receivers.get(self.out, []):
                gate.update(wire_values, wire_receivers)

class NOTgate(Gate):
    
    def update(self, wire_values, wire_receivers):
        if self.canProvide(wire_values):
            #AND with 0xFFFF to have only 16 bits
            value = (~self.getValue(self.ins[0], wire_values)) & 0xFFFF
            wire_values[self.out] = value
            for gate in wire_receivers.get(self.out, []):
                gate.update(wire_values, wire_receivers)
                
class RSHIFTgate(Gate):
    
    def update(self, wire_values, wire_receivers):
        if self.canProvide(wire_values):
            #AND with 0xFFFF to have only 16 bits
            value = (self.getValue(self.ins[0], wire_values) >> self.getValue(self.ins[1], wire_values)) & 0xFFFF
            wire_values[self.out] = value
            for gate in wire_receivers.get(self.out, []):
                gate.update(wire_values, wire_receivers)
                
class LSHIFTgate(Gate):

    def update(self, wire_values, wire_receivers):
        if self.canProvide(wire_values):
            #AND with 0xFFFF to have only 16 bits
            value = (self.getValue(self.ins[0], wire_values) << self.getValue(self.ins[1], wire_values)) & 0xFFFF
            wire_values[self.out] = value
            for gate in wire_receivers.get(self.out, []):
                gate.update(wire_values, wire_receivers)
                
class DIRECTgate(Gate):
    
    def canProvide(self, wire_values):
        keys = wire_values.keys()
        if self.ins[0] not in keys:
            return False
        return True
    
    
    def update(self, wire_values, wire_receivers):
        if self.canProvide(wire_values):
            value = wire_values.get(self.ins[0])
            wire_values[self.out] = value
            for gate in wire_receivers.get(self.out, []):
                gate.update(wire_values, wire_receivers)
    


wire_values = {}

#For each wire, I save the list of gates that receive it's value
wire_receivers = {}

for instruction in instructions:
    instruction = instruction.split(' -> ')
    origin = instruction[0]
    destination = instruction[1]
    if 'AND' in origin:
        operands = origin.split(' AND ')
        and_gate = ANDgate(operands, destination)
        receivers_0 = wire_receivers.get(operands[0], [])
        receivers_0.append(and_gate)
        receivers_1 = wire_receivers.get(operands[1], [])
        receivers_1.append(and_gate)
        wire_receivers[operands[0]] = receivers_0
        wire_receivers[operands[1]] = receivers_1
        and_gate.update(wire_values, wire_receivers)
    elif 'OR' in origin:
        operands = origin.split(' OR ')
        or_gate = ORgate(operands, destination)
        receivers_0 = wire_receivers.get(operands[0], [])
        receivers_0.append(or_gate)
        receivers_1 = wire_receivers.get(operands[1], [])
        receivers_1.append(or_gate)
        wire_receivers[operands[0]] = receivers_0
        wire_receivers[operands[1]] = receivers_1
        or_gate.update(wire_values, wire_receivers)
    elif 'NOT' in origin:
        operand = origin[4:]
        not_gate = NOTgate([operand], destination)
        receiver = wire_receivers.get(operand, [])
        receiver.append(not_gate)
        wire_receivers[operand] = receiver
        not_gate.update(wire_values, wire_receivers)
    elif 'LSHIFT' in origin:
        operands = origin.split(' LSHIFT ')
        lshift_gate = LSHIFTgate(operands, destination)
        receivers_0 = wire_receivers.get(operands[0], [])
        receivers_0.append(lshift_gate)
        receivers_1 = wire_receivers.get(operands[1], [])
        receivers_1.append(lshift_gate)
        wire_receivers[operands[0]] = receivers_0
        wire_receivers[operands[1]] = receivers_1
        lshift_gate.update(wire_values, wire_receivers)
    elif 'RSHIFT' in origin:
        operands = origin.split(' RSHIFT ')
        rshift_gate = RSHIFTgate(operands, destination)
        receivers_0 = wire_receivers.get(operands[0], [])
        receivers_0.append(rshift_gate)
        receivers_1 = wire_receivers.get(operands[1], [])
        receivers_1.append(rshift_gate)
        wire_receivers[operands[0]] = receivers_0
        wire_receivers[operands[1]] = receivers_1
        rshift_gate.update(wire_values, wire_receivers)
    else:
        try:
            value = int(origin)
            wire_values[destination] = value
            for receiver in wire_receivers.get(destination, []):
                receiver.update(wire_values, wire_receivers)
        except:
            direct_gate = DIRECTgate([origin], destination)
            receivers = wire_receivers.get(origin, [])
            receivers.append(direct_gate)
            wire_receivers[origin] = receivers
            direct_gate.update(wire_values, wire_receivers)
            



#print(wire_values.get('a'))
        
        
#---------------------------- Part 2 ----------------------------


wire_values = {}
wire_origin = {}
for instruction in instructions:
    instruction = instruction.split(' -> ')
    origin = instruction[0]
    destination = instruction[1]
    wire_origin[destination] = origin
        
def fetchValue(wire, wire_values, wire_origin):
    try:
        int(wire)
    except:
        if wire in wire_values.keys():
            return wire_values.get(wire)
        else:
            origin = wire_origin.get(wire)
            if 'AND' in origin:
                operands = origin.split(' AND ')
                operand0 = fetchValue(operands[0], wire_values, wire_origin)
                operand1 = fetchValue(operands[1], wire_values, wire_origin)
                value = operand0 & operand1
                wire_values[wire] = value
                return value
            elif 'OR' in origin:
                operands = origin.split(' OR ')
                operand0 = fetchValue(operands[0], wire_values, wire_origin)
                operand1 = fetchValue(operands[1], wire_values, wire_origin)
                value = operand0 | operand1
                wire_values[wire] = value
                return value
            elif 'NOT' in origin:
                operand = origin[4:]
                operand_value = fetchValue(operand, wire_values, wire_origin)
                value = (~operand_value) & 0xFFFF
                wire_values[wire] = value
                return value
            elif 'LSHIFT' in origin:
                operands = origin.split(' LSHIFT ')
                operand0 = fetchValue(operands[0], wire_values, wire_origin)
                operand1 = fetchValue(operands[1], wire_values, wire_origin)
                value = (operand0 << operand1) & 0xFFFF
                wire_values[wire] = value
                return value
            elif 'RSHIFT' in origin:
                operands = origin.split(' RSHIFT ')
                operand0 = fetchValue(operands[0], wire_values, wire_origin)
                operand1 = fetchValue(operands[1], wire_values, wire_origin)
                value = (operand0 >> operand1) & 0xFFFF
                wire_values[wire] = value
                return value
            else:
                try:
                    int(origin)
                except:
                    #Is something like 'lx -> lz'
                    value = fetchValue(origin, wire_values, wire_origin)
                    wire_values[wire] = value
                    return value
                else:
                    wire_values[wire] = int(origin)
                    return int(origin)
    else:
        return int(wire)

#To get the value of the signal in the wire a
fetchValue('a', wire_values, wire_origin)
value_a = wire_values.get('a')
wire_values = {'b' : value_a}

print(fetchValue('a', wire_values, wire_origin))


