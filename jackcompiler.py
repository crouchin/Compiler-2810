 # Jack compiler
# created by Eric Beilmann and Robert and Clauson

import os
import sys
#part one syntax analysis
symbols = "()[]{},;=.+-*/&|~<>"
reservedwords = ['class','constructor','method','function','int','boolean','char','void','var','static','field','let','do','if','else','while','return','true','false','null','this']
class JackTokenizer:
    def __init__(self,filestr):
        self.filestr = filestr
        self.linenum=0

    def gettoken(self, filestr):
        print filestr
        filestr=self.removecomments(filestr)
        print '1',filestr
        out=self.istoken(filestr)
        print '2',out
        out=self.isint(filestr)
        print '3',out
        out=self.isconst(filestr)

    def removecomments(self, filestr):
        whitecount = 0
        commentstart=0
        commentend=0
        
        while filestr.isspace():
            whitecount+=1
        filestr=filestr[whitecount:]
        
        for i in range(len(filestr)):
            if filestr[i] in "\n":
                self.linenum += 1
        
        for i in range(len(filestr)):
            if filestr[i] in "//":
                commentstart = i    
            if filestr[i] in "\n" and i > commentstart:
                commentend = i
        filestr = filestr[:commentstart] + filestr[commentend:]
        
        for i in range(len(filestr)):
            if filestr[i] in "/*":
                commentstart = i
            if filestr[i] in "*/":
                commentend = i
        filestr = filestr[:commentstart] + filestr[commentend:]

        print "line",self.linenum
        print "start",commentstart
        print "end",commentend
        
        return filestr
        
    def istoken(self, filestr):
        line=[]
        for i in range(len(filestr)):
            if filestr[i] in symbols:
                filestr = filestr[i:]
                line.append('symbol')
                line.append(str(i))
                line.append(self.linenum)
                return line

    def isint(self, filestr):
        line=[]
        number = ''
        for i in range(len(filestr)):
            if filestr[i].isdigit():
                number = number + filestr[i]
                filestr = filestr[i:]
                if int(number) > 32767:
                    return "Error: Number too large"

            elif not filestr[i].isdigit() and number != '':
                line.append('integer')
                line.append(int(number))
                line.append(linenum)
                return line
                
            elif not filestr[i].isdigit():
                return False

    def isconst(self, filestr):
        firstq=0
        nextq=0
        stringconst=""
        for i in range(len(filestr)):
            if filestr[i] == '"':
                firstq=i
            if filestr[i] =='"' and i>firstq:
                nextq=i
            if filestr[i] =='\n' and i>firstq and i<nextq:
                return "error: couldn't find string end"
            for i in range(len(filestr[firstq:nextq])):
                stringconst+=filestr[i]
            return stringconst
                
    def keyandid(self):
        pass
                
#part two code generation



def main():
    filestr = ""
    fin = open("Main.jack","r")
    fout = open("Main.xml","w")
    line = fin.read().replace('\r\n', '\n').replace('\r', '\n') 
    filestr += line
    jack=JackTokenizer(filestr)
    jack.gettoken(filestr)
    
main()





            
            
