# Library Management
books=[]
books_count=[]
issue_bookcount=[]
print("Choice: \n1.Insert \n2.Display \n3.Search \n4.Lend Book \n5.Return \n6.Total Books in Library")
ch="y"
while ch=="y":
    choice=int(input("Enter your Choice: "))
    if choice==1:
        book=input("Enter your Book Name: ")
        books.append(book)
        count=int(input("Enter your Book Count: "))
        books_count.append(count)
        issue_bookcount.append(0)
        print("***** Books Inserted *****")
    elif choice==2:
        print("Display the List of Books")
        print("Books Name \t Books Available \t Book Issued")
        i=0
        while (i<len(books)):
             print(books[i],'\t\t', books_count[i], '\t\t', issue_bookcount[i])
             i+=1
    elif choice==3:
        Book=input("Search your Book Name: ")
        for i in range (len(books)):
            if Book==books[i]:
                print("Books Availabe")
                break
            else:
                print("Book Not Available")
    elif choice==4:
        lend=input("Enter Lend Book Name: ")
        for i in range (len(books)):
            if (lend==books[i] and books_count[i] >0):
                books_count[i]-=1
                issue_bookcount[i]+=1
                print("Book issued")
                break
            else:
                print("Book Not Available")
    elif choice==5:
        ren=input("Enter return Book Name: ")
        for i in range (len(books)):
            if (ren==books[i] and books_count[i]>0):
                books_count[i]+=1
                issue_bookcount[i]-=1
                print("Book Returned Successfully")
                break
            else:
                print("This book is not issued by Library")
    elif choice==6:
        total=0
        issue_total=0
        for i in books_count:
             total+=i
        for j in issue_bookcount:
            issue_total+=j
        print("Total Books Available in Library:", total)
        print("Total Books issued:", issue_total)
    ch=input("Do you want to continue (y/n): ")
    print("\n   \n")
            
        
