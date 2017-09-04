#!/usr/bin/python
import os
from os import system
import sys
import APlanguage as AP

identifiers= {}     #Identifiers dictionary
def Translator(f, outcode ):
    i=1
    ch=f.read(1)
    while ch != "":
        word=""
        number=""
        x=0
        #Checking if the character is an alpha or underscore
        if isAlpha(ch) or ch == 'ـ':
            while (ch!="" and (isAlpha(ch) or ord(ch) == 1600 or isDig(ch)) ):
                #Checking if the character is Arabic underscore
                if ord(ch) == 1600:
                    ch=chr(95)
                    word+=ch
                    ch=f.read(1)
                else:
                    word+=ch
                    ch=f.read(1)
            #Check if the word is a keyword
            if word in AP.keywords :
                tr= AP.keywords.get(word)
                outcode.write(tr)
            #Check if the word is in the math library
            elif word in AP.math :
                tr= AP.math.get(word)
                outcode.write(tr)
            #Else find it in the identifiers list or create a new one
            else :
                if word in identifiers:
                    ident= identifiers.get(word)
                    outcode.write(ident+" ")
                else:
                    identifiers[word]= "idn"+str(i)
                    outcode.write("idn"+str(i))
                    i=i+1
        #Checking if the character is a # symbol "comment"
        elif ord(ch)== 35:
            outcode.write("#" + f.readline())
            ch=f.read(1)
        #Checking if the character is a whitespace
        elif ord(ch)== 32:
            outcode.write(ch)
            ch=f.read(1)
        #Checking if the character is an Arabic representation of a comma and rewrite it into English comma
        elif ord(ch)== 1548:
            outcode.write(chr(44))
            ch=f.read(1)
        #Checking if the character is an Arabic representation of a modulus operator and rewrite it into English
        elif ord(ch)== 1642:
            outcode.write(chr(37))
            ch=f.read(1)
        #Checking if the character is an Arabic representation of double quote as a string literal
        elif (ord(ch)== 8220 or ord(ch)== 8221 or ord(ch)== 34):
            word+=chr(34)
            ch=f.read(1)
            while (ch!="" and ord(ch)!= 8220):
                if ord(ch)== 8221:
                    break
                elif ord(ch)== 34:
                    break
                #Checking if the character inside string literal is an escape character
                elif ord(ch)== 47:
                    ch=f.read(1)
                    if ord(ch)== 1587:
                        word+=chr(92)
                        ch='n'
                    elif ord(ch)== 1605:
                        word+=chr(92)
                        ch='t'
                    elif (ord(ch)== 8220 or ord(ch)== 8221):
                        word+=chr(47)
                        break
                    else:
                        word+=chr(47)
                #Checking if the character inside string literal is a curly brace for formatting
                elif ord(ch)== 123:
                    word+=ch
                    ch=f.read(1)
                    while ( ch!="" and ord(ch)!= 125):
                        if isDig(ch):
                            for x in range(0,10):
                                if ord(ch) == (ord('٠')+x):
                                    word+=str(x)
                            ch=f.read(1)
                        elif ord(ch)== 125:
                            break
                        elif ord(ch)==8234 or ord(ch)==8236:
                            ch=f.read(1)
                        elif ord(ch)== 1589:
                            word+='d'
                            ch=f.read(1)
                        elif ord(ch)== 1581:
                            word+='f'
                            ch=f.read(1)
                        elif ord(ch)== 1606:
                            word+='s'
                            ch=f.read(1)
                        else:
                            word+=ch
                            ch=f.read(1)
                word+=ch
                ch=f.read(1)
            word+=chr(34)
            #Check if the word is a keyword (for reserved words between quotation like "r" and "w")
            if word in AP.keywords :
                tr= AP.keywords.get(word)
                outcode.write(tr)
                ch=f.read(1)
            #Check if the word is a math library word (for reserved words between quotation like "inf")
            elif word in AP.math :
                tr= AP.math.get(word)
                outcode.write(tr)
                ch=f.read(1)
            #If the word is not a keyword nor a math library word, writ it into the file as it is
            else:
                outcode.write(word)
                ch=f.read(1)
        #Checking if the character is a digit and translate it into English
        elif isDig(ch):
            while (ch!="" and (isDig(ch) or ord(ch)== 44)):
                number+=ch
                ch=f.read(1)
            for num in number:
                for x in range(0,10):
                    if ord(num) == (ord('٠')+x):
                        outcode.write(str(x))
                if ord(num)== 44:
                    outcode.write(chr(46))
        #writing everything else to the file
        else:
            outcode.write(ch)
            ch=f.read(1)
#The function that checks if the character is an Arabic alphabet or not
def isAlpha(c):
    if ord(c) in range(1569,1595) or ord(c) in range(1601,1611) :
        return True
    else:
        return False
#The function that checks if the character is a digit alphabet or not
def isDig(n):
    if ord(n) in range(1632,1642):
        return True
    else:
        return False

#The main function of the Arabic-Python Code Translation System
#Has as an argument the Arabic-Python code written by the user, received from the GUI module
def main (incode):
    #Creating the output file (the translated code)
    outcode = open( "Ecode.py", "w")
    #Sending the input Arabic code to the system interpreter
    Translator(incode,outcode)
    outcode.close()

    #Running the output Python code
    system('python3.6 Ecode.py 2> outputGUI.txt | tee outcopy.tmp')
    os.remove('outcopy.tmp')

    #Checking the output for errors and translate them
    if os.stat('outputGUI.txt').st_size > 1:
        out2 = open('outputGUI.txt', 'r')
        firstLine = out2.readline()
        if 'Traceback' in firstLine:
            lineNo=out2.readline().replace(',','').split()
            print("هناك خطأ في السطر رقم ", lineNo[3])
            for line in out2:
                for errword in line.replace(':','').split():
                    if errword in AP.errors:
                        print (AP.errors.get(errword))
                        break
        elif 'line' in firstLine:
            out2.seek(0)
            lineNo=out2.readline().replace(',','').split()
            print("هناك خطأ في السطر رقم ", lineNo[3])
            for line in out2:
                for errword in line.replace(':','').split():
                    if errword in AP.errors:
                        print (AP.errors.get(errword))
                        break
        out2.close()
    #os.remove('outputGUI.txt')
    #os.remove('Ecode.py')
