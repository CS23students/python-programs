# Operations on dictionary
word = {'new': 'புதிய','play': 'விளையாடு'}
print ('Options \n 1. Insert \n 2. Search \n 3. Correction')
op='y'
while (op == 'y'):
     ch=int (input ('Enter choice:'))
     def insert (w):
         key = input('Enter the word :')
         words = input('Enter the word meaning:')
         w[key] = words
         print ("word \t Meaning")
         for i in word:
              print (i,'\t-',w[i])
     def search (w):
         k = input ('Enter the Word:')
         for i in w:
             if (i ==k): 
                 print ('The word Meaning: \n', i ,'-',w[i] )
                 break
         else: 
             print ("The word not present in dictionary")
     def correction (w):
         K = input('Enter the word :') 
         words = input ('Enter the word meaning:')
         w[K] =words
         print ('Meaning wrong so correct meaning')
         for i in word:
             if (i ==K): 
                 print (i,'-', w[i])
     if ch ==1: 
         insert (word)
     elif ch==2: 
         search (word)
     elif ch==3: 
         correction (word)
     op = input ('Do you want to continue (y/n):')