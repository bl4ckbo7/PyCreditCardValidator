#!/Users/blackbot/Python/Python35-32/python

#Program: Credit Card Number Checker
#Coded by: bl4ckbo7
#Build: 1.0.2017
#e-mail: bl4ckbo7@protonmail.com

import random, os, sys
from sys import argv
from random import randrange
from time import sleep

print("\n\n")
    
#capturing the card details
cardNumber = int(input("Enter the Card Number(16 digits Only): "))

#evaluates the last digit in the card number
lastDigit = cardNumber%10
    
#this function inspects the syntax of the Credit Card Number
def validateCard(cardNumber):  
    if not(len(str(cardNumber)) == 16):
        print("\n\n[Error] Invalid Card Number, Check the Card Number Correctly!")
        sys.exit(0)
        
print("\n\n[Info] Checking Card Number Validity (Stage 1)", end="")
sleep(2) 
print(".", end="") 
sleep(2) 
print(".", end="") 
sleep(2) 
print(".", end="") 
sleep(2) 
print(".", end="")

validateCard(cardNumber)

print("\n[Info] Analyzing Credit Card details", end="")
sleep(2) 
print(".", end="") 
sleep(2) 
print(".", end="") 
sleep(2) 
print(".", end="") 
sleep(2) 
print(".", end="")

def cardInfo(cardNumber, lastDigit):
    #counts the length of the card Number
    cardLength = len(str(cardNumber))
    
    BIN = ""
    accNo = ""
    
    #calculates the BIN
    for i in range(0,6):        
        BIN += str(cardNumber)[i]
    
    #evaluates the Account Number
    for j in range(6,15):
        accNo += str(cardNumber)[j]
        
    print("\n\nCard Details --------------------", end="\n")
    print("\nCard Number", cardNumber, end="\n", sep=" : ")
    print("Card Length", cardLength, end="\n", sep=" : ")
    print("Check Digit" , lastDigit, end="\n", sep=" : ")
    print("BIN", BIN, end="\n", sep="          : ")
    print("Account Number", accNo, end="\n", sep=" : ")
    print("\n-------------------------------------", end="\n\n")
    
cardInfo(cardNumber, lastDigit)
    

def cardValid(cardNumber, lastDigit):
    
    evenDigits = ""
    num = []
    
    for k in range(0, 15, 2):
        evenDigits += str(cardNumber)[k]
        
    checksum = 0
    i, k, multi = 0, 0, 0
    
    for i in range(0, 8): 
        num += [int(evenDigits[i])]
        i+=1
        
    while k<8:
        multi = (num[k] * 2)
        if multi>9:
            largeNum = 0
            largeNum = multi-9
            checksum += largeNum
            pass
        else:
            checksum += multi
        k+=1
    
    print("Checksum", checksum, end="\n", sep=" : ")

    print("\n[Info] Checking Card Number Validity (Stage 2)", end="")
    sleep(2) 
    print(".", end="") 
    sleep(2) 
    print(".", end="") 
    sleep(2) 
    print(".", end="") 
    sleep(2) 
    print(".", end="")
    sleep(2)
    print(".", end="")
    
    checkProduct = checksum * 9
    if int(str(checkProduct)[2]) == lastDigit:
        print("\n\n[Info] Card is VALID!")
        pass
    else:
        print("\n\n[Info] Card is INVALID!")
            
cardValid(cardNumber, lastDigit)