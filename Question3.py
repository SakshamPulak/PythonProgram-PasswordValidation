PasswordList = ["PulaK@1129@","SakshaM@2570","VermA@1129$","abc@1129A","ABC123456@$"]
Choice='n'
while Choice=='n':
    UserName = input("Choose UserName : ")
    print ("Use Name is free; Do you want to continue")
    Choice=input("y/n : ")
    
print ("")
print ("----------------------------------------")
print ("Password Criteria")
print ("1. At least 1 letter between [a-z] ")
print ("2. At least 1 number between [0-9] ")
print ("3. At least 1 letter between [A-Z] ")
print ("4. At least 1 character from [$#@] ")
print ("5. Minimum length of password : 6 ")
print ("6. Maximum length of password : 12")
print ("----------------------------------------")

LowerCase, UpperCase, SpecialCharcter, Digit = 0, 0, 0, 0
Password="False"
while Password=="False":
    print ("")
    InputPassword = input("Enter password : ")
    LengthOfPassword = len(InputPassword)

    if (LengthOfPassword < 6):
        for i in InputPassword: 

            if (i.islower()): 
                LowerCase+=1            
            if (i.isupper()): 
                UpperCase+=1            
            if (i.isdigit()): 
                Digit+=1            
            if(i=='@'or i=='$' or i=='#'): 
                SpecialCharcter+=1

    if (LengthOfPassword > 12):
        for i in InputPassword: 

            if (i.islower()): 
                LowerCase+=1            
            if (i.isupper()): 
                UpperCase+=1            
            if (i.isdigit()): 
                Digit+=1            
            if(i=='@'or i=='$' or i=='#'): 
                SpecialCharcter+=1

    if (LengthOfPassword >= 6 and LengthOfPassword <=12): 
        for i in InputPassword: 

            if (i.islower()): 
                LowerCase+=1            
            if (i.isupper()): 
                UpperCase+=1            
            if (i.isdigit()): 
                Digit+=1            
            if(i=='@'or i=='$' or i=='#'): 
                SpecialCharcter+=1

    if (LengthOfPassword >= 6 and LengthOfPassword <=12):
        if (LowerCase==0 or UpperCase==0 or SpecialCharcter==0 or Digit==0):
            if (LowerCase==0):
                print ("Use At least 1 letter between [a-z]")            
            if (UpperCase==0):
                print ("Use At least 1 letter between [A-Z]")        
            if (Digit==0):
                print ("Use At least 1 letter between [0-9]")
            if (SpecialCharcter==0):
                print ("Use At least 1 letter between [@,#,$]")

    if (LengthOfPassword >= 6 and LengthOfPassword <=12):        
        if (LowerCase>=1 and UpperCase>=1 and SpecialCharcter>=1 and Digit>=1):
            print("Valid Password")
            if (InputPassword in PasswordList):
                PasswordChoice= input("Want to continue with this password (y/n) : ")
                if PasswordChoice=="y":
                    print("Registration Done")
                    Password="True"
                    break
                else :
                    continue
            else :
                print ("")
                print ("This password is new and not present in password list")
                PasswordChoice= input("Want to continue with this password (y/n) : ")
                if PasswordChoice=="y":
                    print("Registration Done")
                    Password="True"
                    break
                else :
                    continue
            

    if not (LengthOfPassword >= 6 and LengthOfPassword <=12): 
        ("Invalid Password")
        if (LowerCase==0):
            print ("Use At least 1 letter between [a-z]")            
        if (UpperCase==0):
            print ("Use At least 1 letter between [A-Z]")        
        if (Digit==0):
            print ("Use At least 1 letter between [0-9]")
        if (SpecialCharcter==0):
            print ("Use At least 1 letter between [@,#,$]")            
        if (LengthOfPassword < 6 or LengthOfPassword > 12 ):
            print ("Length of password must be between (6 and 12)")

    LowerCase=0
    UpperCase=0
    SpecialCharcter=0
    Digit=0
    
    

                

        
    
 
    
