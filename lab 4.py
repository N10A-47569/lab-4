menu = ['Interactive','Recursive','Exit']

while True:
    print ("\n1. Interactive", "\n2. Recursive", "\n3. Exit", "\n")
    
    wybor = int(input("Twój wybór: "))
    
    opcja = list(range(1, 4))
    if wybor in opcja:
        
        if wybor == 2: 
            nterms = int(input("How many terms? "))
            n1, n2 = 0, 1
            count = 0
            if nterms <= 0:
                print("Please enter a positive integer")
            elif nterms == 1:
                print("Fibonacci sequence upto",nterms,":")
                print(n1)
            else:
                print("Fibonacci sequence:")
            while count < nterms:
                print(n1)
                nth = n1 + n2
                n1 = n2
                n2 = nth
                count += 1
        if wybor == 3:
            print("\nDo widzenia!")
            quit(0)


        if wybor == 1:
           a = 0
           b = 1
           n=int(input("Enter the number of terms in the sequence: "))
           print(a,b,end=" ")
           while(n-2):
               c=a+b
               a,b = b,c
               print(c,end=" ")
               n=n-1
        
    else:
        print ("Niepoprawna komenda!")
