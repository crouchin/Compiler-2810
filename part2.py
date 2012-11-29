# Jack compiler
# created by Eric Beilmann and Robert and Clauson

import os
import sys
#part one syntax analysis
symbols = "()[]{},;=.+-*/&|~<>"
reservedwords = ['class','constructor','method','function','int','boolean','char','void','var','static','field','let','do','if','else','while','return','true','false','null','this']
class JackTokenizer
    def __init__():


    def gettoken():
        whitecount = 0
        linenum = 0
        for i in filestr:
            while filestr[i] in isspace()
                whitecount += 1
            if i in "/n":
                linenum += 1
        filestr = filestr[whitecount:]
        
        for i in filestr:
            if filestr[i] and filestr[i + 1] in "/":
                commentstart = i
            elif filestr[i] in "'\'" and filestr[i + 1] in "n" and i > commentstart:
                commentend = i - 1
        filestr = filestr[:commentstart] + filestr[commentend:]
        
        for i in filestr:
            if filestr[i] in "/" and filestr[i + 1] in "*":
                commentstart = i
            elif filestr[i] in "*" and filestr[i + 1] in "/":
                commentend = i + 1
        filestr = filestr[:commentstart] + filestr[commentend:]

            #i didn't get much done but it is a start anyways

#################### Valid Tokens ########################

        for i in filestr:
            if filestr[i] in symbols:
                filestr = filestr[i:]
                return 'symbol', str(i), linenum

#################### Integers ############################

        number = ''
        for i in filestr:
            if filestr[i].isdigit():
                number = number + filestr[i]
                filestr = filestr[i:]
                if int(number) > 32767:
                    return "Error: Number too large"

            elif not filestr[i].isdigit() and number != '':
                return 'integer', int(number), linenum
                
            elif not filestr[i].isdigit():
                return False

#################### Constants ##########################

        for i in filestr:
            if filestr[i] == '"':
                isConst = True
                while isConst:

        # Here's what I got so far. Feel free to proof read. Also I'm thinking we should 
        # just be chaining the if statements the whole way or make these into functions. 
        # What do you think?



#part two code generation
class CompilationEngine
    def __init__(self,tokens,outfile):
        self.token=token
        self.i=0
        self.out=outfile
        self.indent=0

    def nextToken(self):
        if self.i>=len(self.tokens):
            fail("Too long")
        token=self.token[self.i]
        self.i+=1
        global glinenum
        glinenum=token[2]
        return token

    def peek(self):
        token=self.nextToken()
        self.i-=1
        return token

    def keyword(self,keyword):
        token=self.nextToken()
        if token[0]!=keyword or token[1]!=keyword:
            fail("your fail message here")
        print>>self.out," "*self.indent"<identifier>"
        return token

    def identifier(self):

    def symbol(self):

    def expectType(self):
        token=self.peek()
        if token[0]....int char boolean;
            return self.keyword(token[1])
        return self.identifier
        
    def compileClass(self):
        #about 5 lines I missed
        kind=self.keyword(token[1])
        vartype=self.expectType()
        while True:
            token=self.peek()
            if token[0]!=keyword or token[1] not in ['static','field']:
                break
            self.compile classVarDec()
        while True:
            token=self.peek()
            if token[0]!=symbol or token[1]!=',':
                break
            self.compileSubroutine()
        
def main():
    filestr = ""
    fp = open("infile.txt","r")
    for line in infile:
        self.line = fp.read().replace('\r\n', '\n').replace('\r', '\n')
        filestr += self.line

main()





            
            
