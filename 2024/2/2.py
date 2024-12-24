# -*- coding: utf-8 -*-

file_name = 'input.txt'
file = open(file_name,mode='r')
    

def isSafeDes(report):
    for i in range(len(report)-1):
        if report[i]<=report[i+1] or (report[i] - report[i+1])>3:
            return False
    return True
        
def isSafeAs(report):
    for i in range(len(report)-1):
        if report[i]>=report[i+1] or (report[i+1] - report[i])>3:
            return False
    return True

def isSafe(report):
    if len(report)<=1:
        return True
    if report[0]>report[1]:
        return isSafeDes(report)
    elif report[0]<report[1]:
        return isSafeAs(report)
    return False

def isSafeDesPart2(report):
    for i in range(len(report)-1):
        if report[i]<=report[i+1] or (report[i] - report[i+1])>3:
            reportSinActual = report.copy()
            del reportSinActual[i]
            reportSinSig = report.copy()
            del reportSinSig[i+1]
            return isSafeDes(reportSinActual) or isSafeDes(reportSinSig)
    return True
        
def isSafeAsPart2(report):
    for i in range(len(report)-1):
        if report[i]>=report[i+1] or (report[i+1] - report[i])>3:
            reportSinActual = report.copy()
            del reportSinActual[i]
            reportSinSig = report.copy()
            del reportSinSig[i+1]
            return isSafeAs(reportSinActual) or isSafeAs(reportSinSig)
    return True

def isSafePart2(report):
    if len(report)<=1:
        return True
    if isSafeDesPart2(report) or isSafeAsPart2(report):
        return True
    return False


safe_reports = 0
for line in file:
     line = line.strip()
     line = line.split()
     report = [int(x) for x in line]
     if isSafePart2(report):
         print(line)
         safe_reports += 1
         
print(safe_reports)
