Tshirt=0
Trousers=0
Scarf=0
Smartphone=0
iPad=0
Laptop=0
Eggs=0
Chocolate=0
Juice=0
Milk=0
   

def get_bulk_input():

    global Tshirt
    global Trousers
    global Scarf
    global Smartphone
    global iPad
    global Laptop
    global Eggs
    global Chocolate
    global Juice
    global Milk

    print('_'*70)
    print("\nENTER ITEM AND QUANTITIES")
    print('_'*70)
    itemValue=[Tshirt,Trousers,Scarf,Smartphone,iPad,Laptop,Eggs,Chocolate,Juice,Milk]
    item=["Tshirt","Trousers","Scarf","Smartphone","iPad","Laptop","Eggs","Chocolate","Juice","Milk"]

    while(True):
        lst=list(map(int, input("Enter code and quantity (leave blank to stop): ").split()))
        if lst==[]:
            break
        else:
            I1=lst[0]
            I2=lst[1]
            if (-1< I1<= 10 )& (0<I2<5000):
                print("You added ",end='')
                print(lst[1],end='')
                print(" ",end='')
                print(item[lst[0]])
                if I1==0:
                    Tshirt=Tshirt+I2
                if I1==1: 
                    Trousers=Trousers+I2
                if I1==2:
                    Scarf = Scarf +I2
                if I1==3:
                    Smartphone=Smartphone+I2
                if I1==4: 
                    iPad =iPad+I2
                if I1==5: 
                    Laptop=Laptop+I2
                if I1==6:
                    Eggs=Eggs+I2
                if I1==7:
                    Chocolate=Chocolate+I2
                if I1==8: 
                    Juice=Juice+I2
                if I1==9: 
                    Milk=Milk+I2
            else:
                print("Invalid quantity. Try again.")
    

    return itemValue

def print_order_details(quantities):
    global Tshirt
    global Trousers
    global Scarf
    global Smartphone
    global iPad
    global Laptop
    global Eggs
    global Chocolate
    global Juice
    global Milk
    print('_'*70)
    print("\n ORDER DETAILS")
    print('_'*70)
            
    print("\n")
    n=1
    if quantities[0]>0:
        print("[",end ='')
        print(n,end ='')
        print("] ",end ='')
        print("Tshirt X ",end ='')
        print(Tshirt,end ='')
        print(" = Rs ",end ='')
        print("500*",end ='')
        print(Tshirt,end ='')
        print(" = Rs ",end ='')
        print(Tshirt*500,end ='')
        print("\n")
        n=n+1
    if quantities[1]>0:
        print("[",end ='')
        print(n,end ='')
        print("] ",end ='')
        print("Trousers X ",end ='')
        print(Trousers,end ='')
        print(" = Rs ",end ='')
        print("600*",end ='')
        print(Trousers,end ='')
        print(" = Rs ",end ='')
        print(Trousers*600,end ='')
        print("\n")
        n=n+1
    if quantities[2]>0:
        print("[",end ='')
        print(n,end ='')
        print("] ",end ='')
        print("Scarf X ",end ='')
        print(Scarf,end ='')
        print(" = Rs ",end ='')
        print("250*",end ='')
        print(Scarf,end ='')
        print(" = Rs ",end ='')
        print(Scarf*250,end ='')
        print("\n")
        n=n+1
    if quantities[3]>0:
        print("[",end ='')
        print(n,end ='')
        print("] ",end ='')
        print("Smartphone X ",end ='')
        print(Smartphone,end ='')
        print(" = Rs ",end ='')
        print("20000*",end ='')
        print(Smartphone,end ='')
        print(" = Rs ",end ='')
        print(Smartphone*20000,end ='')
        print("\n")
        n=n+1
    if quantities[4]>0:
        print("[",end ='')
        print(n,end ='')
        print("] ",end ='')
        print("iPad X ",end ='')
        print(iPad,end ='')
        print(" = Rs ",end ='')
        print("30000*",end ='')
        print(iPad,end ='')
        print(" = Rs ",end ='')
        print(iPad*30000,end ='')
        print("\n")
        n=n+1
    if quantities[5]>0:
        print("[",end ='')
        print(n,end ='')
        print("] ",end ='')
        print("Laptop X ",end ='')
        print(Laptop,end ='')
        print(" = Rs ",end ='')
        print("50000*",end ='')
        print(Laptop,end ='')
        print(" = Rs ",end ='')
        print(Laptop*50000,end ='')
        print("\n")
        n=n+1
    if quantities[6]>0:
        print("[",end ='')
        print(n,end ='')
        print("] ",end ='')
        print("Eggs X ",end ='')
        print(Eggs,end ='')
        print(" = Rs ",end ='')
        print("5*",end ='')
        print(Eggs,end ='')
        print(" = Rs ",end ='')
        print(Eggs*5,end ='')
        print("\n")
        n=n+1
    if quantities[7]>0:
        print("[",end ='')
        print(n,end ='')
        print("] ",end ='')
        print("Chocolate X ",end ='')
        print(Chocolate,end ='')
        print(" = Rs ",end ='')
        print("10*",end ='')
        print(Chocolate,end ='')
        print(" = Rs ",end ='')
        print(Chocolate*10,end ='')
        print("\n")
        n=n+1
    if quantities[8]>0:
        print("[",end ='')
        print(n,end ='')
        print("] ",end ='')
        print("Juice X ",end ='')
        print(Juice,end ='')
        print(" = Rs ",end ='')
        print("100*",end ='')
        print(Juice,end ='')
        print(" = Rs ",end ='')
        print(Juice*100,end ='')
        print("\n")
        n=n+1
    if quantities[9]>0:
        print("[",end ='')
        print(n,end ='')
        print("] ",end ='')
        print("Milk X ",end ='')
        print(Milk,end ='')
        print(" = Rs ",end ='')
        print("45*",end ='')
        print(Milk,end ='')
        print(" = Rs ",end ='')
        print(Milk*45,end ='')
        print("\n")
        n=n+1

        

def calculate_category_wise_cost(quantities):
    global Tshirt
    global Trousers
    global Scarf
    global Smartphone
    global iPad
    global Laptop
    global Eggs
    global Chocolate
    global Juice
    global Milk

   

    print('_'*70)
    print("\nCATEGORY-WISE COST")
    print('_'*70)
    Apparels= (Tshirt*500) +(Trousers*600)+(Scarf*250)
    Electronics=(Smartphone*20000)+(iPad*30000)+(Laptop*50000)
    Eatables=(Eggs*5)+(Milk*45)+(Juice*100)+(Chocolate*10)
    if Apparels>0:
        print("Apparels = Rs ",end='')
        print(Apparels)
    if Electronics>0:
        print("Electronics = Rs ",end='')
        print(Electronics)
    if Eatables>0:
        print("Eatables = Rs ",end='')
        print(Eatables)

    return Apparels,Electronics,Eatables



def get_discount(cost, discount_rate):
	'''
	Description: This is a helper function. DO NOT CHANGE THIS. 
	This function must be used whenever you are calculating discounts.
	
	Parameters: Takes 2 parameters:
	- cost: Integer
	- discount_rate: Float: 0 <= discount_rate <= 1

	Returns: The discount on the cost provided.
	'''
	return int(cost * discount_rate)


def calculate_discounted_prices(apparels_cost, electronics_cost, eatables_cost):
    print('_'*70)
    print("\n DISCOUNTS")
    print('_'*70)
    discounted_apparels_cost=0
    discounted_electronics_cost=0 
    discounted_eatables_cost=0
    aDiscount=0
    eleDiscount=0
    eatDiscount=0

    if apparels_cost==0:
        pass
    elif apparels_cost>=2000:
        aDiscount=get_discount(apparels_cost,0.1)
        discounted_apparels_cost = apparels_cost- aDiscount
        print("[APPAREL] Rs ",end='')
        print(apparels_cost,end='')
        print(" - ",end='')
        print("Rs ",end='')
        print(aDiscount,end='')
        print(" = Rs ",end='')
        print(discounted_apparels_cost)

    if electronics_cost==0:
        pass
    elif electronics_cost >=25000:
        eleDescount=get_discount(electronics_cost,0.1)
        discounted_electronics_cost=electronics_cost-eleDescount
        print("[ELECTRONICS] Rs ",end='')
        print(electronics_cost,end='')
        print(" - ",end='')
        print("Rs ",end='')
        print(eleDescount,end='')
        print(" = Rs ",end='')
        print(discounted_electronics_cost)

    if eatables_cost==0:
        pass
    elif eatables_cost>=500:
        eatDiscount=int(get_discount(eatables_cost,0.1))
        discounted_eatables_cost=eatables_cost-eatDiscount
        print("[EATABLES] Rs ",end='')
        print(eatables_cost,end='')
        print(" - ",end='')
        print("Rs ",end='')
        print(eatDiscount,end='')
        print(" = Rs ",end='')
        print(discounted_eatables_cost)

    totalDiscount= aDiscount+eleDiscount+eatDiscount
    totalCost=discounted_apparels_cost+ discounted_electronics_cost+ discounted_eatables_cost
    print("\n TOTAL DISCOUNT = Rs ",end='')
    print(totalDiscount)
    print(" TOTAL COST = Rs ",end='')
    print(totalCost)
    print("\n")


    return (discounted_apparels_cost, discounted_electronics_cost, discounted_eatables_cost)


def get_tax(cost, tax):
	'''
	Description: This is a helper function. DO NOT CHANGE THIS. 
	This function must be used whenever you are calculating discounts.
	
	Parameters: Takes 2 parameters:
	- cost: Integer
	- tax: 	Float: 0 <= tax <= 1

	Returns: The tax on the cost provided.
	'''
	return int(cost * tax)

def calculate_tax(apparels_cost, electronics_cost, eatables_cost):
    print('_'*70)
    print("\n TAX")
    print('_'*70)
    atax_apparels_cost=0
    atax_electronics_cost=0 
    atax_eatables_cost=0
    aTax=0
    eleTax=0
    eatTax=0

    if apparels_cost==0:
        pass
    else:
        aTax=get_tax(apparels_cost,0.1)
        atax_apparels_cost = apparels_cost- aTax
        print("[APPAREL] Rs ",end='')
        print(apparels_cost,end='')
        print(" - ",end='')
        print("Rs ",end='')
        print(aTax,end='')
        print(" = Rs ",end='')
        print(atax_apparels_cost)

    if electronics_cost==0:
        pass
    else:
        eleTax=get_tax(electronics_cost,0.15)
        atax_electronics_cost=electronics_cost-eleTax
        print("[ELECTRONICS] Rs ",end='')
        print(electronics_cost,end='')
        print(" - ",end='')
        print("Rs ",end='')
        print(eleTax,end='')
        print(" = Rs ",end='')
        print(atax_electronics_cost)

    if eatables_cost==0:
        pass
    else:
        eatTax=int(get_tax(eatables_cost,0.05))
        atax_eatables_cost=eatables_cost-eatTax
        print("[EATABLES] Rs ",end='')
        print(eatables_cost,end='')
        print(" - ",end='')
        print("Rs ",end='')
        print(eatTax,end='')
        print(" = Rs ",end='')
        print(atax_eatables_cost)

    totaltax= aTax+eleTax+eatTax
    totalCost=atax_apparels_cost+ atax_electronics_cost+ atax_eatables_cost
    print("\n TOTAL TAX = Rs ",end='')
    print(totaltax)
    print(" TOTAL COST = Rs ",end='')
    print(totalCost)
    print("\n")


    return (totalCost,totaltax)



def apply_coupon_code(total_cost):
	
    print('_'*70)
    print("\n COUPON CODE ")
    print('_'*70)
    total_coupon_discount=0
    while(True):
        code=input("Enter coupon code (else leave blank):")
        if code=="HELLE25":
            if total_cost>=25000:
                discount=0.25*total_cost
                if discount>5000:
                    total_coupon_discount=5000
                    break
                else:
                    total_coupon_discount=discount
                    break
        elif code=="CHILL50":
            if total_cost>=50000:
                discount=0.5*total_cost
                if discount>10000:
                    total_coupon_discount=10000
                    break
                else:
                    total_coupon_discount=discount
                    break
        elif code=="":
            break
        else:
            print("Invalid coupon code. Try again.")
    print("\n TOTAL COUPON DISCOUNT = Rs ",end='')
    print(total_coupon_discount)
    print(" TOTAL COST = Rs ",end='')
    total_cost_afterC=total_cost-total_coupon_discount
    print(total_cost_afterC)

    return (total_cost_afterC,total_coupon_discount)

    




order = b=get_bulk_input()

print_order_details(order)
a,b,c = calculate_category_wise_cost(order)

i,j,k = calculate_discounted_prices(a,b,c)
m,n=calculate_tax(i, j, k)
x,y=apply_coupon_code(m)



b=get_bulk_input()


