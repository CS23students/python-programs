n=int(input("Enter the total no. of products: "))
name=[]
price=[]
quantity=[]
total=0
for i in range (1,n+1):
    a=input("Enter product name: ")
    name.append(a)
    b=int(input("Enter price"))
    price.append(b)
    c=int(input("Enter quantity: "))
    quantity.append(c)
    total+=b*c
gst=0
print("Product",'\t',"Quantity",'\t',"price",'\t',"GST")
for i in range (0,n):
    s=(price[i]*0.18)*quantity[i]
    print(name[i],'\t', quantity[i],'\t', price[i],'\t', s)
    gst+=s
print("Total Amount: ", total+gst)
