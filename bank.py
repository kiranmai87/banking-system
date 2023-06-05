#open a new account
# Deposit amount
# Withdraw Amount
# Balance Enquiry
# Transfer money from one account to another account


#import datetime module to get the date of transaction
# import random module to get the transaction number
from datetime import (date,datetime)
import random

users={'ramesh@123':['1234','Ramesh',123456,100000],'suresh@1':['2345','Suresh babu',3456780,0],'kumar@12':['3456','Kumar',45678912,0]}
transaction={}  # empty dictionary  to add the transaction done

while True:
    print('''
            Press 1 to REGISTER
            Press 2 to LOGIN
            ''')
    action=input("Enter your option: ")

    #adding new user to the users list by taking input from user(username,password,name,account number)
    if action=='1':
        l=[]
        username=input("Enter your username: ")
        password=input("Enter your password: ")
        c_password=input("Re-type your password: ")
        name=input("Enter your name: ")
        acc_num=int(input("Enter your account number: "))
        balance=0
        l.append(password)
        l.append(name)
        l.append(acc_num)
        l.append(balance)
        
        if password==c_password:
            if username not in users:
                 users[username]=l
            else:print("Username already exists")
        else:print("password doesnot match with confirm pasword")
        #print(users)
    # login to the account with username and password by authenticating
    elif action=='2':
        
        username=input("Enter your username: ")
        password=input("Enter your password: ")
        if username in users and password==users[username][0]:
            print("Hello {},".format(users[username][1]))
            print("Account number: ",users[username][2])
        
    
            print('''
            Press 1 to deposit
            Press 2 to withraw
            Press 3 to Balance enquiry
            Press 4 to transfer money''')
            option=input("Enter your transaction: ")
        # deposit the amount to account and add the transaction into to empty dictionary
            if option=='1':
                
                l=[]
                print("your account balance is Rs.",users[username][3])
                deposit=float(input("Enter the amount: Rs."))
                x="Credit"
                users[username][3]+=deposit
                print("Your current account  balance is:  Rs.",users[username][3])
        # if username already exists append the tranactin list to username
                if username in transaction:
                    l.append(x)
                    l.append(deposit)
                    l.append(users[username][3])    
                    l.append(str(date.today())) 
                    l.append(str(datetime.now().strftime("%H:%M:%S")))                                  
                    transaction[username].append(l)
                else:                               # if username doesnot exist create usename in dictionary
                    l.append(x)
                    l.append(deposit)
                    l.append(users[username][3])
                    l.append(str(date.today()))  
                    l.append(str(datetime.now().strftime("%H:%M:%S")))                                          
                    transaction[username]=[l]
                
            elif option=='2':
                                
                print("Your account balance is :  Rs.",users[username][3])
                withdraw=float(input("Enter the amount to withdraw: Rs."))
                x="Debit"
                if withdraw <= users[username][3]:
                    users[username][3]-=withdraw
                    print("Your current account  balance is:  Rs.",users[username][3])
                    w=[]
                    if username in transaction:
                        w.append(x)
                        w.append(withdraw)
                        w.append(users[username][3])  
                        w.append(str(date.today())) 
                        w.append(str(datetime.now().strftime("%H:%M:%S")))                         
                        transaction[username].append(w)
                    else:
                        w.append(x)
                        w.append(withdraw)
                        w.append(users[username][3]) 
                        w.append(str(date.today()))
                        w.append(str(datetime.now().strftime("%H:%M:%S")))                       
                        transaction[username]=[w]
                        
                else:print("Insufficient funds")
             # print the transactions of the user  
            elif option=='3':
                print(45*'*','WELCOME TO INDIA BANK',40*'*')
                print('\n')
                print('NAME: ',users[username][1],50*" ",date.today(),2*" ",datetime.now().strftime("%H:%M:%S"))
                print('Account number: ',users[username][2])
                print(115*"_")
                print("DATE",15*" ","Transaction id",10*" ","Transaction",18*" ","Amount",18*" ","available bal")
                print("\n")
                print(115*"-")
                for i in range (len(transaction[username])-1,-1,-1):
                    print(transaction[username][i][3],12*" ",random.randint(1111111,1000000000),10*" ",transaction[username][i][0],17*" ","Rs.",transaction[username][i][1],17*" ","Rs.",transaction[username][i][2],"\n",transaction[username][i][4])
                print('\n')
                print(50*"-",'THANK YOU',50*'-')
                print(50*"*","VISIT AGAIN",50*"*")
            # transfer the amount from one user to another user and adding the transaction to transaction dictionary 
            elif option=='4':
                        t=[]
                        account=int(input("Enter the account number: "))
                        for i in users:
                            if  users[i][2]==account:
                                #print(i)
                                print('Name: ',users[i][1])
                                a=float(input("Enter the amount to transfer: Rs."))
                                x="Crdt from "+users[username][1]
                                if a < users[username][3]:
                                    users[i][3]+=a      #adding the transferred amount to entered account
                                    users[username][3]-=a   # deducting the transferred amount from the user
                                    if i in transaction:
                                        t.append(x)
                                        t.append(a)
                                        t.append(users[i][3])
                                        t.append(str(date.today())) 
                                        t.append(str(datetime.now().strftime("%H:%M:%S")))   
                                        transaction[i].append(t) 
                                    else:
                                        t.append(x)
                                        t.append(a)
                                        t.append(users[i][3])
                                        t.append(str(date.today())) 
                                        t.append(str(datetime.now().strftime("%H:%M:%S")))   
                                        transaction[i]=[t] 
                                    m="Dbt to "+users[i][1]
                                    u=[]
                                    if username in transaction:
                                        u.append(m)
                                        u.append(a)
                                        u.append(users[username][3])  
                                        u.append(str(date.today())) 
                                        u.append(str(datetime.now().strftime("%H:%M:%S")))                         
                                        transaction[username].append(u)
                                    else:
                                        u.append(m)
                                        u.append(a)
                                        u.append(users[username][3]) 
                                        u.append(str(date.today()))
                                        u.append(str(datetime.now().strftime("%H:%M:%S")))                       
                                        transaction[username]=[u]
                        
                                    #print(transaction)
                                    
                                else:print("You have not enough funds to transfer")
                                break
                            #else:print("Invaild account number")

        else:print("Invalid credentials")
    else:print("invaild option selected")



        