# -*- coding: utf-8 -*-

#Open file
file_name = 'input.txt'
file = open(file_name,mode='r')

def processIP(ip):
    hyp_seq = []
    sps = []
    ip_divided = line.strip().split('[')
    sps.append(ip_divided[0])
    for i in range(1,len(ip_divided)):
        section = ip_divided[i].split(']')
        hyp_seq.append(section[0])
        sps.append(section[1])
    return (hyp_seq, sps)

#Read file
ip_list = []
for line in file:
    ip_list.append(processIP(line))
    
def hasABBA(s):
    for i in range(len(s)-3):
        if s[i] == s[i+3]:
            if s[i+1] != s[i] and s[i+1] == s[i+2]:
                return True
    return False

def part1(ip_list):
    total = 0
    for ip in ip_list:
        if any([hasABBA(s) for s in ip[0]]):
                continue
        if any([hasABBA(s) for s in ip[1]]):
            total += 1
    return total

print(part1(ip_list))
#---------------------------- Part 2 ----------------------------

def possiblesABAs(ip):
    abas = set()
    for hyp in ip[0]:
        for i in range(len(hyp)-2):
            if hyp[i] == hyp[i+2]:
                abas.add(hyp[i+1] + hyp[i] + hyp[i+1])
    return abas

def hasBAB(ip, abas):
    for sps in ip[1]:
        for i in range(len(sps)-2):
            if sps[i] == sps[i+2]:
                if sps[i:i+3] in abas:
                    return True
    return False

def part2(ip_list):
    total = 0
    for ip in ip_list:
        abas = possiblesABAs(ip)
        if hasBAB(ip, abas):
            total += 1
    return total

print(part2(ip_list))