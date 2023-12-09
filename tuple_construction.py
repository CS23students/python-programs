def search(things):
    s=input("Enter the searching thing:")
    for i in things:
        if s==i:
            print("The thing is available")
            break
        else:
            print("The thing is not available")
            break
def menu(things,count,price,gst):
    print("*"*30)
    print("Things\tCount\tRate\tGST")
    print("_"*30)
    i=0
    while i<len(things):
        print(things[i],"\t",count[i],"\t",price[i],'\t',gst[i])
        i=i+1
def purchase(a,b,c,d,e,f,g,h):
    p=input("Enter a needed thing:")
    for i in range(len(a)):
        if(p==a[i] and b[i]>0):
            n=int(input("Enter No of things:"))
            f.append(p)
            b[i]=n
            e[i]+=n
            print('Item purchased')
            c[i]=e[i]*h[i]
            d[i]=(g[i]*e[i])+c[i]
    return p,c,d,e,f
def billing(a,b,c,d):
    print("*"*75)
    print("Things\t\tCount\t\tRate\t\tCost")
    print("_"*75)
    i=0
    while i<len(a):
        print(a[i],"\t\t",b[i],"\t\t",c[i],"\t\t",d[i])
        i=i+1
    print("_"*75)
    sum=0
    for i in d:
        sum=sum+i
    print("Total:\t",sum)
def Insert(things,password,count):
    b=int(input("Enter the password:"))
    if b==password:
        s=input("Enter the inserting thing:")
        w=int(input("Enter the No of things:"))
        for i in range(len(things)):
            if s==things[i]:
                count[i]+=w
        print("Things Inserted")
things=("Bricks","Cement","TMT")
count=(950,1000,500)
price=(1000,2500,5500)
gst=(450,800,1000)
purchased_item=[0,0,0]
bill=[0,0,0]
bill2=[0,0,0]
user_name=["abc","tmg"]
password=123
pc_list=[]
y=1
while y==1:
    n=int(input("Enter your choice:"))
    purchased_item.append(0)
    bill.append(0)
    bill2.append(0)
    things=list(things)
    count=list(count)
    price=list(price)
    gst=list(gst)
    if n==1:
        search(things)
    elif n==2:
        menu(things,count,price,gst)
    elif n==3:
        purchase(things,count,bill,bill2,purchased_item,pc_list,gst,price)
    elif n==4:
        billing(pc_list,purchased_item,bill,bill2)
    elif n==5:
        Insert(things,password,count)
    y=int(input("Do you want to continue(0/1):"))
    things=tuple(things)
    count=tuple(count)
    price=tuple(price)
    gst=tuple(gst)
