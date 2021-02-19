# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 07:54:10 2020

@author: ASUS
"""
from nltk.tokenize import sent_tokenize, word_tokenize, WordPunctTokenizer


responses=["Your welcome to Google Assistance ",
           "My name is Punnu Gullu","Sorry","Thanks","Out of range"]
# these for only element .....

def time():
    import datetime 
    current_time = datetime.datetime.now()
    print("Current time is :")
    print (current_time.hour,end="")
    print(":",end="")
    print (current_time.minute,end="")
    print(":",end="")
    print (current_time.second,end="")
    print(":",end="")
    print (current_time.microsecond)
    return 0

def date():
    import datetime 
    current_time = datetime.datetime.now()
    print("Current date is :") 
    print (current_time.day,end="")
    print (":",end="")
    print (current_time.month,end="")
    print (":",end="")
    print (current_time.year)
    return 0



def calender():
    import datetime 
    current_time = datetime.datetime.now()
    print("Current time is :")
    print (current_time.hour,end="")
    print(":",end="")
    print (current_time.minute,end="")
    print(":",end="")
    print (current_time.second,end="")
    print(":",end="")
    print (current_time.microsecond)
    
    print("Current date is :") 
    print (current_time.day,end="")
    print (":",end="")
    print (current_time.month,end="")
    print (":",end="")
    print (current_time.year)
    
    return 0
    
def fact(a):
    fact=1
    for i in range(1,a+1):
        fact=fact*i
    return fact

# these are for two elements ....

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def divide(a,b):
    return a/b
def hcf(a,b):
    H=a if a<b else b
    while H>=1:
        if a%H==0 and b%H==0:
            return H
        H-=1
def lcm(a,b):
    L=a if a>b else b
    while L<=a*b:
        if L%a==0 and L%b==0:
            return L
        L+=1
def end():
    print(responses[3])
    input("Press Enter key to exit")
    exit()    
def myname():
    print(responses[1])   
def sorry():
    print(responses[4])    
def inv():
    print("Mr.RAVI CHAUDHARY INVENTED ME")
       
# Now for three elements ........

def add1(a,b,c):
    return a+b+c
def sub1(a,b,c):
    return a-b-c
def mul1(a,b,c):
    return a*b*c
def divide1(a,b,c):
    return (a/b)/c    
commands={"NAME":myname,"END":end,"EXIT":end,"CLOSE":end,"INVENTED":inv}    
# main dictionary .....
ope={
     "ADDITION":add,"ADD":add,"PLUS":add,"SUM":add,"JODNA":add,"SUBTRACT":sub,"SUBTRACTION":sub,"DIFFERENCE":sub,
     "MINUS":sub,"MULTIPLY":mul,"PRODUCT":mul,"MULTIPLICATION":mul,"DIVISION":divide,"DIVIDE":divide,
     "LCM":lcm,"HCF":hcf
     }
ope1={
     "ADDITION":add1,"ADD":add1,"PLUS":add1,"SUM":add1,"SUBTRACT":sub1,"SUBTRACTION":sub1,"DIFFERENCE":sub1,
     "MINUS":sub1,"MULTIPLY":mul1,"PRODUCT":mul1,"MULTIPLICATION":mul1,"DIVISION":divide1,"DIVIDE":divide1,
     }
ope2={
     "FACT":fact,
     "FACTORIAL":fact,
     }

ope3={"TIME":time,"DATE":date,"CALENDER":calender,"TARIKH":date}

def ravi(text):
    l=[]
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return(l)
    
print("\t \t","*",responses[0],"*")
#print()
print("\t \t \t","*",responses[1],"*")
print()

li=[]
li1=[]
li2=[]
li3=[]

while True:
    text=input("Enter some text :")
    #sentence tokenizer
    #print("\n sentence tokenizer :")
    #print(sent_tokenize(input_text))
    li1=sent_tokenize(text)
    for i in li1:
        li.append(i)

    # word tokenizer
    #print("\n word tokenizer :")
    #print(word_tokenize(input_text))
    li2=word_tokenize(text)
    for i in li2:
        li.append(i)

    # wordpunct tokenizer
    #print("\n word punct tokenizer :")
    #print(WordPunctTokenizer().tokenize(input_text))
    li3=WordPunctTokenizer().tokenize(text)
    for i in li3:
        li.append(i)
        
    #print(li)
     
    for word in li:
    #for word in text.split(' '):
        l=ravi(text)
        #print(len(l))
        
        if word.upper() in ope3.keys():
            try:
                r=ope3[word.upper()]()
                #print(r)
            except:
                print("something wrong")
            finally:
                break
        
        if word.upper() in ope2.keys() and (len(l)+1==2):
            try:
                #l=ravi(text)
                #print(len(l))
                r=ope2[word.upper()](l[0])
                print(r)
            except:
                print("Something wrong")
            finally:
                break
        
        if word.upper() in ope.keys() and (len(l)+1==3):
            try:
                #l=ravi(text)
                #print(len(l))
                r=ope[word.upper()](l[0],l[1])
                print(r)
            except:
                print("Something wrong")
            finally:
                break
            
        if word.upper() in ope1.keys() and (len(l)+1==4):
            try:
                #l=ravi(text)
                #print(len(l))
                r=ope1[word.upper()](l[0],l[1],l[2])
                print(r)
            except:
                print("Something wrong")
            finally:
                break
        elif word.upper() in commands.keys():
            commands[word.upper()]()
            break
    else:
        sorry()    
    li=[] # this is because when i will append some words then in second itteration this will append all other
    #words of second text and will give answer accordingly