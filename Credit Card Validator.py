#!/Users/blackbot/Python/Python35-32/python

import random, os, sys
from sys import argv
from random import randrange, choice
from time import sleep

print("\n\n=======================================", end="\n")
print("Program : Credit Card Number Checker\nCoded by: bl4ckbo7\nBuild   : 1.1.2017\nE-mail  : bl4ckbo7@protonmail.com", end="\n")
print("=======================================", end="\n\n")

#MasterCard BINs begin here

#1. CRDB Bank TZ PLC
MC_CRDB = ["524281", "528648", "536608", "537029", "539943"]

#2. Barclays Bank Tanzania
MC_Barclays = ["512081"]

#3. National Bank of Commerce TZ PLC
MC_NBC = ["519257", "519611", "539593", "551259"]

#4. National Microfinance Bank TZ PLC
MC_NMB = ["516148", "516167", "516239", "527046", "527048"]

#5. EXIM Bank (Tanzania) LTD
MC_EXIM = ["516213", "525454", "525458", "529771", "534226", "534259", "552471", "554857"]

#6. United Bank of Africa PLC
MC_UBA = ["534404"]

#7. FBME Bank LTD
MC_FBME = ["522196", "552116"]

#MasterCard BINs end here

#VisaCard BINs begin here

#1. CRDB Bank TZ PLC
VC_CRDB = ["402662", "410773", "411699", "411748", "419837", "419838", "421760", "423212"]

#2. National Bank of Commerce Tanzania
VC_NBC = ["417441", "417442", "424426", "446991", "451378", "451379", "451380", "459257"]

#3. Stanbic Bank Tanzania LTD
VC_SB = ["431331", "431332", "431333", "444566", "446314"]

#4. Standard Chartered Bank TZ LTD
VC_SC = ["422128", "422802", "422806", "422807", "433816", "457878", "457879", "478680", "478681", "478682"]

#5. Diamond Trust Bank Tanzania LTD
VC_DTB = ["419827", "419828", "419829"]

#6. Barclays Bank TZ LTD
VC_BarclaysTZ = ["406982", "420564", "420572", "453183", "453184", "453185", "453186", "453187", "472911", "483969"]

#7. Barclays Bank
VC_Barclays = ["452217", "452218"]

#VisaCard BINs end here

    
def generator():
    randNum, choices, cardNumber, lastDigit, bankChoice, valid = "", "", 0, 0, "", False
    
    #generating begins here
    
    for r in range(0, 10):
        randNum += str(randrange(0, 9))
        r+=1
        
    '''[MC_CRDB+MC_Barclays+MC_EXIM+MC_NBC+MC_NMB+MC_FBME+MC_UBA]'''
    
    for b in range(1):
        bankChoice = choice((MC_CRDB, MC_Barclays, MC_EXIM, MC_FBME, MC_NBC, MC_NMB, MC_UBA))
    
    for i in range(1):
        choices = choice((bankChoice))
        
    #generating ends here
    
    #validating generated card number begins here

    cardNumber = choices + randNum
    lastDigit = int(cardNumber)%10
    
    print("\n\nCard Number", int(cardNumber), end="\n\n", sep=" : ")            
    
    
    while not valid:
    
        evenDigits = ""
        num = []
        
        for k in range(0, 15, 2):
            evenDigits += str(cardNumber)[k]
            
        i, k, multi, checksum = 0, 0, 0, 0
        
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
        
        #print("Checksum", checksum, end="\n\n", sep=" : ")
    
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
        print("100%", end="")    
        
        modulo = checksum % 10
        if modulo == lastDigit:
            print("\n\n[Info] Found Valid Card!")
            valid = True
            pass
        else:   
            valid = False
            
            cardNumber = 0
            randNum = ""
            
            
            for r in range(0, 10):
                randNum += str(randrange(0, 9))
                r+=1
                
            '''[MC_CRDB+MC_Barclays+MC_EXIM+MC_NBC+MC_NMB+MC_FBME+MC_UBA]'''
            
            for b in range(1):
                bankChoice = choice((MC_CRDB, MC_Barclays, MC_EXIM, MC_FBME, MC_NBC, MC_NMB, MC_UBA))
            
            for i in range(1):
                choices = choice((bankChoice))
                
            #generating ends here
            
            #validating generated card number begins here
        
            cardNumber = choices + randNum
            lastDigit = int(cardNumber)%10
            
            print("\n\nGenerating again.... Finding Valid Card Number...", end="\n\n", sep=" : ")            
    
    #validating generated Number ends here
    
    #card info analysis begins here
    
    #counts the length of the card Number
    cardLength = len(str(cardNumber))
    
    BIN, accNo, bank, cardBrand, MIN = "", "", "", "", ""
    
    #checks the MIN
    for m in range(0,2):
        MIN += str(cardNumber)[m]
    
    #calculates the BIN
    for i in range(0,6):        
        BIN += str(cardNumber)[i]
    
    #evaluates the Account Number
    for j in range(6,15):
        accNo += str(cardNumber)[j]
    
    k = 0
    
    #Card MIN ranges
    MC_MIN = list(range(51,55))
    VC_MIN = list(range(40,48))
    
    #1. Checks the card Brand
    while k < 4:
        
        if int(MIN) == MC_MIN[k]:
            #The Card is MasterCard
            cardBrand = "MASTERCARD"
            
            #2. Check the Bank Issuer
            
            #CRDB Bank TZ PLC
            for value in range(0, 5):
                if MC_CRDB[value] == BIN:
                    bank = "CRDB Bank TZ PLC"
                    pass
                value+=1
                
            #Barclays
            for value in range(0, 1):
                if MC_Barclays[value] == BIN:
                    bank = "Barclays Bank Tanzania"
                    pass
                value+=1
                
            #National Bank of Commerce TZ PLC
            for value in range(0, 4):
                if MC_NBC[value] == BIN:
                    bank = "National Bank of Commerce TZ PLC"
                    pass
                value+=1
                    
            #National Microfinance Bank TZ PLC
            for value in range(0, 5):
                if MC_NMB[value] == BIN:
                    bank = "National Microfinance Bank TZ PLC"
                    pass
                value+=1
                
            #EXIM Bank (Tanzania) LTD
            for value in range(0, 8):
                if MC_EXIM[value] == BIN:
                    bank = "EXIM Bank (Tanzania) LTD"
                    pass
                value+=1    
            
            #United Bank of Africa PLC
            for value in range(0, 1):
                if MC_UBA[value] == BIN:
                    bank = "United Bank of Africa PLC"
                    pass
                value+=1
                
            #FBME Bank LTD
            for value in range(0, 2):
                if MC_FBME[value] == BIN:
                    bank = "FBME Bank LTD"
                    pass
                value+=1
        k+=1
    
        pass
        
    t=0
    
    while t < 8:
        
        if int(MIN) == VC_MIN[t]:
            #The Card Brand is VisaCard
            cardBrand = "VisaCard"
            
            #2. Check the Bank Issuer
            
            #CRDB Bank TZ PLC
            for value in range(0, 8):
                if VC_CRDB[value] == BIN:
                    bank = "CRDB Bank TZ PLC"
                    pass
                value+=1
                
            #Barclays Bank TZ LTD
            for value in range(0, 10):
                if VC_BarclaysTZ[value] == BIN:
                    bank = "Barclays Bank Tanzania"
                    pass
                value+=1
                
            #National Bank of Commerce TZ PLC
            for value in range(0, 8):
                if VC_NBC[value] == BIN:
                    bank = "National Bank of Commerce TZ PLC"
                    pass
                value+=1
                    
            #Standard Chartered Bank TZ LTD
            for value in range(0, 10):
                if VC_SC[value] == BIN:
                    bank = "Standard Chartered Bank TZ LTD"
                    pass
                value+=1
                
            #Stanbic Bank Tanzania LTD
            for value in range(0, 5):
                if VC_SB[value] == BIN:
                    bank = "Stanbic Bank Tanzania LTD"
                    pass
                value+=1    
            
            #Diamond Trust Bank Tanzania LTD
            for value in range(0, 3):
                if VC_DTB[value] == BIN:
                    bank = "Diamond Trust Bank Tanzania LTD"
                    pass
                value+=1
                
            #Barclays Bank
            for value in range(0, 2):
                if VC_Barclays[value] == BIN:
                    bank = "Barclays Bank"
                    pass
                value+=1
        t+=1

    if len(str(bank))==0:    
        print("\n\nBank Card Issuer Not Found!")
        pass
    
    print("\n\n\nCard Number Details--------------------", end="\n")
    print("\nCard Number", cardNumber, end="\n", sep=" : ")
    print("Bank Issuing", bank, end="\n", sep=": ")
    print("Card Brand", cardBrand, end="\n", sep="  : ")
    print("Card Length", cardLength, end="\n", sep=" : ")
    print("Check Digit" , lastDigit, end="\n", sep=" : ")
    print("BIN", BIN, end="\n", sep="         : ")
    print("Account Number", accNo, end="\n", sep=" : ")
    
    print("\n-------------------------------------", end="\n\n")
    
    #generate card info analysis ends here
        
        

    
#this function inspects the syntax of the Credit Card Number
def validateCard(cardNumber):  
    if not ((len(str(cardNumber)) == 16) or (len(str(cardNumber)) == 19) or (len(str(cardNumber)) == 13)):
        print("\n\n[Error] Invalid Card Number, Check the Card Number Correctly!")
        sys.exit(0)


def cardInfo(cardNumber, lastDigit):
    #counts the length of the card Number
    cardLength = len(str(cardNumber))
    
    BIN, accNo, bank, cardBrand, MIN = "", "", "", "", ""
    
    #checks the MIN
    for m in range(0,2):
        MIN += str(cardNumber)[m]
    
    #calculates the BIN
    for i in range(0,6):        
        BIN += str(cardNumber)[i]
    
    #evaluates the Account Number
    for j in range(6,15):
        accNo += str(cardNumber)[j]
    
    k = 0
    
    #Card MIN ranges
    MC_MIN = list(range(51,55))
    VC_MIN = list(range(40,48))
    
    #1. Checks the card Brand
    while k < 4:
        
        if int(MIN) == MC_MIN[k]:
            #The Card is MasterCard
            cardBrand = "MASTERCARD"
            
            #2. Check the Bank Issuer
            
            #CRDB Bank TZ PLC
            for value in range(0, 5):
                if MC_CRDB[value] == BIN:
                    bank = "CRDB Bank TZ PLC"
                    pass
                value+=1
                
            #Barclays
            for value in range(0, 1):
                if MC_Barclays[value] == BIN:
                    bank = "Barclays Bank Tanzania"
                    pass
                value+=1
                
            #National Bank of Commerce TZ PLC
            for value in range(0, 4):
                if MC_NBC[value] == BIN:
                    bank = "National Bank of Commerce TZ PLC"
                    pass
                value+=1
                    
            #National Microfinance Bank TZ PLC
            for value in range(0, 5):
                if MC_NMB[value] == BIN:
                    bank = "National Microfinance Bank TZ PLC"
                    pass
                value+=1
                
            #EXIM Bank (Tanzania) LTD
            for value in range(0, 8):
                if MC_EXIM[value] == BIN:
                    bank = "EXIM Bank (Tanzania) LTD"
                    pass
                value+=1    
            
            #United Bank of Africa PLC
            for value in range(0, 1):
                if MC_UBA[value] == BIN:
                    bank = "United Bank of Africa PLC"
                    pass
                value+=1
                
            #FBME Bank LTD
            for value in range(0, 2):
                if MC_FBME[value] == BIN:
                    bank = "FBME Bank LTD"
                    pass
                value+=1
        k+=1
    
        pass
        
    t=0
    
    while t < 8:
        
        if int(MIN) == VC_MIN[t]:
            #The Card Brand is VisaCard
            cardBrand = "VisaCard"
            
            #2. Check the Bank Issuer
            
            #CRDB Bank TZ PLC
            for value in range(0, 8):
                if VC_CRDB[value] == BIN:
                    bank = "CRDB Bank TZ PLC"
                    pass
                value+=1
                
            #Barclays Bank TZ LTD
            for value in range(0, 10):
                if VC_BarclaysTZ[value] == BIN:
                    bank = "Barclays Bank Tanzania"
                    pass
                value+=1
                
            #National Bank of Commerce TZ PLC
            for value in range(0, 8):
                if VC_NBC[value] == BIN:
                    bank = "National Bank of Commerce TZ PLC"
                    pass
                value+=1
                    
            #Standard Chartered Bank TZ LTD
            for value in range(0, 10):
                if VC_SC[value] == BIN:
                    bank = "Standard Chartered Bank TZ LTD"
                    pass
                value+=1
                
            #Stanbic Bank Tanzania LTD
            for value in range(0, 5):
                if VC_SB[value] == BIN:
                    bank = "Stanbic Bank Tanzania LTD"
                    pass
                value+=1    
            
            #Diamond Trust Bank Tanzania LTD
            for value in range(0, 3):
                if VC_DTB[value] == BIN:
                    bank = "Diamond Trust Bank Tanzania LTD"
                    pass
                value+=1
                
            #Barclays Bank
            for value in range(0, 2):
                if VC_Barclays[value] == BIN:
                    bank = "Barclays Bank"
                    pass
                value+=1
        t+=1

    if len(str(bank))==0:    
        print("\n\nBank Card Issuer Not Found!")
        pass
    
    print("\n\n\nCard Number Details--------------------", end="\n")
    print("\nCard Number", cardNumber, end="\n", sep=" : ")
    print("Bank Issuing", bank, end="\n", sep=": ")
    print("Card Brand", cardBrand, end="\n", sep="  : ")
    print("Card Length", cardLength, end="\n", sep=" : ")
    print("Check Digit" , lastDigit, end="\n", sep=" : ")
    print("BIN", BIN, end="\n", sep="         : ")
    print("Account Number", accNo, end="\n", sep=" : ")
    
    print("\n-------------------------------------", end="\n\n")
    
    

def cardValid(cardNumber, lastDigit):
    
    evenDigits = ""
    num = []
    
    for k in range(0, 15, 2):
        evenDigits += str(cardNumber)[k]
        
    i, k, multi, checksum = 0, 0, 0, 0
    
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
    
    print("Checksum", checksum, end="\n\n", sep=" : ")

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
    print("100%", end="")    
    
    modulo = checksum % 10
    if modulo == lastDigit:
        print("\n\n[Info] Card is VALID!")
        pass
    else:
        print("\n\n[Info] Card is INVALID!")

#main function
def main():
    print("Select your choice here: ", end="\n")
    response = int(input("\t1) Generate Valid Random Card Numbers\n\t2) Check Validity of the Card Number\n\n"))
    
    if response == 1:
        generator()
    elif response == 2:
        
        #capturing the card details
        cardNumber = int(input("\nEnter the Card Number: "))
        
        #evaluates the last digit in the card number
        lastDigit = cardNumber%10
        
        print("\n\n[Info] Checking Card Number Validity (Stage 1)", end="")
        sleep(2) 
        print(".", end="") 
        sleep(2) 
        print(".", end="") 
        sleep(2) 
        print(".", end="") 
        sleep(2) 
        print(".", end="")
        print("100%", end="")
        
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
        print("100%", end="")    
        
        cardInfo(cardNumber, lastDigit)
    
        cardValid(cardNumber, lastDigit)
    else:
        print("Sorry, Wrong Input!")
    
main()
