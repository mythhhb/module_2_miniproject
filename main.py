print("========SMART CANTEEN=======")
print("1. Veg Sandwich : ₹60\n" \
"2. Masala Dosa - ₹80\n" \
"3. Chole Rice - ₹90\n" \
"4. Paneer Roll - ₹100\n" \
"5. Tea - ₹20\n")
stotal = 0
flaf = 0
while True:
    ch = int(input("choose item number: "))
    
    if ch  <=0 or ch>5:
       print("invalid choice")
       flag = 1
       break
       
        
    qt = int(input("enter quantity(1-10): "))      
    if qt<=0 or qt>10:
       print("Quantity must be positive or less then 10")
       flag  = 1
       break
    if ch == 1:
        print("ADDED: Veg Sandwich x",qt,"=","₹",float(60*qt))
        stotal +=float(60*qt)
    elif ch == 2:
            print("ADDED: Masala Dosa  x",qt,"=","₹",float(80*qt))
            stotal +=float(80*qt)
    elif ch == 3:
            print("ADDED: Chole Rice  x",qt,"=","₹",float(90*qt))
            stotal +=float(90*qt)
    elif ch == 4:
            print("ADDED: Panner Roll x",qt,"= ₹",float(100*qt))
            stotal +=float(100*qt)
    elif ch == 5:
            print("ADDED: Tea x",qt,"= ₹",float(20*qt))
            stotal +=float(20*qt)


    yn= input("Add another item? (y/n) : ").lower()
    if yn=="n":
               break

    
if flag==0:
       print("========RECEIPT========")
       if stotal>500:
          print("subtotal: ","₹",stotal,
             "\n discount: ","₹", (stotal*10)/100,
             "\ntotal: ","₹", stotal-(stotal*10)/100)
          print("THANK YOU")
       elif stotal>250:
          print("subtotal: ","₹", stotal,
             "\n discount: ","₹", (stotal*5)/100,
             "\ntotal: ","₹", stotal-(stotal*5)/100)
          print("THANK YOU")

       else:
          print("subtotal: ","₹", stotal,
             "\ndiscount: ","₹", 0,
             "\ntotal: ","₹", stotal)
       print("THANK YOU")