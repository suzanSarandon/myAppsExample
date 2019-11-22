def get_tax_rate(product_type):
    if product_type == "book" :
        product_fpa = 0.06
    elif product_type == "bread" :
        product_fpa = 0.13
    elif product_type == "other":
        product_fpa = 0.24
    return product_fpa

i = 0
accountz=[]

def handle_sale(): 
    customer_sale_balance = 0.00
    while(True):
        product_type = input ("Type? ")
        if product_type=="none":
            break
        product_count = int (input ("How many? "))
        product_price = float (input("How much? "))
        product_fpa = get_tax_rate (product_type)
        customer_sale_balance+=float(product_count*(product_price*product_fpa+product_price))
    return customer_sale_balance
       
avg_customers_balance = 0.00
max_customer_balance = 0.00
min_customer_balance = 0.00
customer_sale_balance=0.00

while(True):
    answer = input("More (y/n)? ")
    if answer =="n":   
        break
    if answer == "y":
        i+=1
        customer_sale_balance = handle_sale()
        accountz.append(customer_sale_balance)
        print("##")
        accountz.sort
        min_customer_balance=min(accountz)
        max_customer_balance=max(accountz)
        avg_customers_balance=sum(accountz)/len(accountz)    
    print ("##")
    print ("Customer", str(i)," sale  {:.2f}" .format(customer_sale_balance))
    

print("##")
print("Total customers", i)
print("##")
print("Total sales {:.2f}" .format(sum(accountz)))
print("##")
print("Max sale {:.2f}" .format(max_customer_balance))
print("##")
print("Min sale {:.2f}" .format(min_customer_balance))
print("##")
print("Average sale {:.2f}" .format(avg_customers_balance))
print("##")
if len(accountz) %2 !=0:
    print("Median sale {:.2f}"  .format(int(accountz[len(accountz)/2])))
else:
    median=(int(accountz[int(len(accountz)/2)]+int(accountz[int(len(accountz)/2-1)])))
    print("Median sale {:.2f}"  .format(median))



   

