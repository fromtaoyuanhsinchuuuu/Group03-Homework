#!/usr/bin/env python3
import os
import sys

def read(filename):
    with open(filename, 'rb') as fp: return fp.read()

def run(ifn):
    #c = 'python3 -B AC_Code.py'
    c = 'python -B AC_Code.py'
    c = './a.out'
    return os.system("%s < %s > %s"%(c,ifn,'slave.out'))

def main():
    score = 0
    for subtask in eval(read('subtasks.py')):        
        for trial in subtask[1:]:
            ifn, ofn, tl, ml, ol, idfn = trial
            print('%s '%ifn, end='')
            res = run(ifn)
            ResStr = ''
            if res != 0:
                ResStr = 'RE 0'
            else:
                waLine = os.system('python ./special %s %s slave.out' % (ifn, ofn))
                if waLine != 0:
                    ResStr = "WA 0" 
                else:
                    ResStr = "AC %d"%subtask[0]
                    score += subtask[0]
            print(ResStr)
    print(score)


if __name__ == '__main__':
    main()
    input('press enter to continue...')
