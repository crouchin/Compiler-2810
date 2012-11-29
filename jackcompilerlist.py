# Jack compiler
# created by Eric Beilmann and Robert and Clauson

#How this file is different from the other one:
#I tend to be more familiar with working with lists so i decided to
#work with them untill (i think) all undesirable elements are gone
#then i just put it in a string afterwords   -Eric

#latest update as of 11/27 3:20
#I have finished the jack tokenizer to the point where it will
#make an outfile of all of the tokens.
#I started the next part by copying in the code i wrote
#earlier from class(change what ever you want of it because
#a backup is in the dropbox) -Eric

import os
import sys
#part one syntax analysis
symbols = "()[]{},;=.+-*/&|~<>"
integer = "0123456789"
lexicalelements = ['class',
                   'constructor',
                   'function',
                   'method',
                   'field',
                   'static',
                   'var',
                   'int',
                   'char',
                   'boolean',
                   'void',
                   'true',
                   'false',
                   'null',
                   'this',
                   'let',
                   'do',
                   'if',
                   'else',
                   'while',
                   'return',]


class JackTokenizer:
    def __init__(self,filelist):
        self.filelist = filelist
        self.linenum=0

    def gettoken(self, filelist):
        self.fout=open("tokenlist.txt","w")
        filelist=self.removecomments(filelist)
        self.istoken(filelist)
        self.isint(filelist)
        self.isconst(filelist)
        self.keywords(filelist)
        self.fout.close()


    def removecomments(self, filelist):
        popcount=0
        for i in range(len(filelist)):
            filelist[i]=filelist[i].strip()      
        popcount=0
        for i in range(len(filelist)):
            if filelist[i-popcount].startswith("//"):
                filelist.pop(i-popcount)
                popcount+=1
        popcount=0
        for i in range(len(filelist)):
            if not filelist[i-popcount]:
                filelist.pop(i-popcount)
                popcount+=1
        for i in range(len(filelist)):
            if filelist[i].startswith("/*"):
                commentstart=i
            if filelist[i].endswith("*/"):
                commentend=i
        popcount=0
        for i in range(len(filelist)):
            if i>=commentstart and i<=commentend:
                filelist.pop(i-popcount)
                popcount+=1
        return filelist
        
    def istoken(self, filelist):
        linecount=0
        print filelist
        for i in filelist:
            print i
            line=[]
            linecount+=1
            a=i.split()
            for j in a:
                if j in symbols:
                    line.append('symbol')
                    line.append(j)
                    line.append(linecount)
                    if len(line)>3:
                        line=line[3:]
                    print >>self.fout, line

    def isint(self, filelist):
        numparts=[]
        linecount=0
        for i in filelist:
            i=i.replace(";","")
            line=[]
            linecount+=1
            a=i.split()
            for j in a:
                try:
                    x=int(j)
                    if int(j)>=0 and int(j)<=32767:
                        line.append('integer')
                        line.append(j)
                        line.append(linecount)
                        if int(j) > 32767:
                            print "Error: Number too large"
                        print >>self.fout, line
                except ValueError:
                    pass
        
    def isconst(self, filelist):
        linecount=0
        for i in filelist:
            line=[]
            linecount+=1
            for j in i:
                if j=='"':
                    m=i.find('"')
                    m=m+1
                    newi=i[m:]
                    n=newi.find('"')
                    string='"'+newi[:n]+'"'
                    line.append('const')
                    line.append(string)
                    line.append(linecount)
                    if len(line)>3:
                        line=line[3:]
            if len(line)>0:
                print >>self.fout, line
                
    def keywords(self,filelist):
        linecount=0
        for i in filelist:
            line=[]
            linecount+=1
            a=i.split()
            for j in a:
                if j in lexicalelements:
                    line.append('keyword')
                    line.append(j)
                    line.append(linecount)
                    if len(line)>3:
                        line=line[3:]
                    print >>self.fout, line

#part Two Parsing(turning into xml)
class CompilationEngine:
    def __init__(self,tokens,outfile):
        self.token=token
        self.i=0
        self.out=outfile
        self.indent=0

    def nextToken(self):
        self.fout=open("tokenlist","r")
        #if self.i>=len(self.tokens):
            #fail("Too long")
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
            #fail("your fail message here")
            print>>self.out," ",self.indent,"<identifier>"
        return token

    def identifier(self):
        pass

    def symbol(self):
        pass

    def expectType(self):
        pass
##        token=self.peek()
##        if token[0]....int char boolean;
##            return self.keyword(token[1])
##        return self.identifier
        
    def compileClass(self):
        #about 5 lines I missed
        kind=self.keyword(token[1])
        vartype=self.expectType()
        while True:
            token=self.peek()
            if token[0]!=keyword or token[1] not in ['static','field']:
                break
            self.compileclassVarDec()
        while True:
            token=self.peek()
            if token[0]!=symbol or token[1]!=',':
                break
            self.compileSubroutine()                

                
#part Three code generation





def main():
    filelist=[]
    tokenlist=[]
    fin1 = open("Main.jack","r")
    for line in fin1:
        filelist.append(line)
    jack=JackTokenizer(filelist)
    jack=jack.gettoken(filelist)
    fin2=open("tokenlist.txt","r")
    for line in fin2:
        tokenlist.append(line)
    
    
main()





            
            
