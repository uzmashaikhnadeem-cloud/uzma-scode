EXPENSE=[ ]
print("WELCOME TO EXPENSE TRACKER")
print("========MENU========")
print("1.Add Expenses")
print("2.View the information")
print("3.view total spending")
print("4.EXIT")
print("====================")
while True:
    type=int(input("Type a choice here:"))

    # for 1.add expense
    if type==1:
        date=input("📅Enter the date of shopping=")
        category=input("🧾hich category of shopping=")
        discription=input("📌📋Write something about the item=")
        amount=float(input("💸Enter the stuff's amount="))

        dict={"date":date,
            "category":category,        # if is emmbeded in dictionary
            "discription":discription,
            "amount":amount}
        
        EXPENSE.append(dict)                  #dictionary is embedded in expense list above
                                                # dic is made  to embedde items inf in keyword for view and total
                                          
     # view information
    elif type==2:
        if len(EXPENSE)==0:
            print("No information recorded 🤷‍♀️ = do shopping and come")  
    # no sense of elif type>=5 here it wont response     
        else:
            i=1
            for (a) in (EXPENSE):       # in expense in type1 input will save the the choise:1 continoiusly
                                        # inorder to add it to like 1,2,3(i+=1) in choice 2
                print(f"{i}.Total stuff's you have 🛒 purchased=>📅:{a["date"]},🧾:{a["category"]},📌📋:{a["discription"]},💸:{a["amount"]}")
                i+=1
   # total spendind             
    elif type==3:
        if len(EXPENSE)==0:
            print("No information recorded 🤷‍♀️ = do 🛒 Shopping and Come")        
        else:
            T=0
            for b in EXPENSE:
                T+=b["amount"]
            print(f":::>Your total amount=💸{T}")
    elif type == 4:
        print("|THANK-U💛, HOPE YOU LIKE OUR SERVICE|")
        break        
    else:
        print("incorrect choice of ❌❌option")     




