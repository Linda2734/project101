import random
response = input("press y to roll and n to exit: ")

    
while(response=="y"):
    no = random.randint(1,6)
    if(no==1):
        print("*")
        
    elif(no==2):
        print("*  ")
        print("   ")
        print("  *")
        
    elif(no==3):
        print("*  ")
        print(" *  ")
        print("  *")
        
    elif(no==4):
        print("*  *")
        print("    ")
        print("*  *")
        
    elif(no==5):
        print("*  *")
        print("  *   ")
        print("*  *")
        
    elif(no==6):
        print("*  *")
        print("*  *")
        print("*  *")
        
    response = input("press y to roll again and n to exit: ")
        
    if(response=="n"):
        print("The program has ended")
        
    

    


        
   
    
    
        

    
