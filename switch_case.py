binary = 0
while(binary != 1):
    val = 0
    string = ""

    print ("To check value currently stored sentence press 1\n")
    print("To add new words press 2\n")

    def switch(val):
        global string
        if (val == 1):
            if(len(string)== 0):
                print("Empty\n")
            else:
                print(string)
        elif (val == 2):
            str2 = input("Enter the sentence without <space> at the begining\n\t: ")
            str3 =" "
            string += str3
            string+=str2
        else:
            print("Not a Valid choice")

    val = int(input('Enter Your Choice\n\t: '))

    switch(val)
    print("To exit press 1 or press 0")
    binary = int(input())
