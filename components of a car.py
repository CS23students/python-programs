# Components of car
comp=['tyre','glass','light']
comp_count=[10,20,30]
comp_rate=[2000,3000,4000]
gst=[100,200,300]
purchased_item=[]
bill=[]
bill2=[]
pc_list=[]
ch='y'
while ch=='y':
    print('\nchoice:\n1.Search\n2.Display\n3.Purchasing\n4.Bill\n5.Admin\n6.Total Components')
    choice=int(input('Enter choice: '))
    purchased_item.append(0)
    bill.append(0)
    bill2.append(0)
    if choice==1:
        search=input('Enter comp: ')
        for i in range(len(comp)):
            if search==comp[i]:
                print('available')
                break
        else:
            print('not available')
    elif choice==2:
        print('Component comp_count\t comp_rate')
        for i in range(len(comp)):
            print(comp[i],'\t ',comp_count[i],'\t\t',comp_rate[i])
    elif choice==3:
        n=input('Enter any components: ')
        m=int(input("Enter no. of components: "))
        pc_list.append(n)
        for i in range(len(comp)):
            if n==comp[i] and comp_count[i]>0:
                comp_count[i]=m
                purchased_item[i]+=m
                print('item Purchased')
                bill[i]=purchased_item[i]+comp_rate[i]
                bill2[i]=(gst[i]+purchased_item[i]+bill[i])
    elif choice==4:
        print('comp\t purchased_item\t rate\t\t+gst')
        i=0
        while i<len(pc_list):
            print(pc_list[i],'\t',purchased_item[i],'\t\t',bill[i],'\t\t',bill2[i])
            i=i+1
        sum=0
        for i in bill2:
            sum=sum+i
        print('\t\t\t Total: \t',sum)
    elif choice==5:
        user_name=['Elon','musk']
        password=[1234,4321]
        un=input('Enter username: ')
        pw=int(input('Enter password: '))
        for i in range(len(user_name)):
            for j in range(len(password)):
                 if (un==user_name[i] and pw==password[j]):
                    print('verified')
                    insert=input('Add any additional components: ')
                    insert_count=int(input('Enter count: '))
        for i in range(len(comp)):
            if insert==comp[i]:
              comp_count[i]+=insert_count
        print('item inserted')
    elif choice==6:
        total=0
        result=0
        print('comp \t purchase_item')
        i=0
        s=len(comp)
        while i<s:
            print(comp[i],'\t',purchased_item[i])
            i=i+1
        for i in comp_count:
            total=total+i
        print('Components count: ',total)
        for j in purchased_item:
            result+=j
        print('total purchased item: ',total)
        print('-'*50)
    ch=input('Enter y/n: ')
        

                                                





























                    
                
                
   
