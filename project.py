j=input("enter y to continue: ")
# using while loop to repeat the process
while j=='y':
  # input from user to encrypt or decrypt the data
  a=input("Write encrypt or decrypt: ")
  # change the value of a into lower case
  # using if else loop to identify the input
  # encryption part
  if a.lower()=="encrypt":
    # take input from the user to encrypt the data
    b=input("type your message: ")
    # declaring a variable p
    p=''
    # using for loop to encrypt data
    for i in b:
      #c is the ascii value of every character from the input message
      c=ord(i)
      #convert c from integer to string and add to empty string p with "-" in end
      p=p+str(c)+"-"
    print(p)
    # decrypt part
  elif a.lower()=="decrypt":
    # taking encrypted message as input to decrypt 
    z=input("type your encrypted message: ")
    # spliting the string to remove "-" and make a list
    q=z.split("-")
    # removing the last empty string element in the list
    del q[-1]
    # declaring a variabe f 
    f=''
    #using for loop for decryption
    for j in q:
      # converting string j to integer and using "chr" function to find character affiliated to the ascii value 
      j=chr(int(j))
      f=f+j
    print(f)
  # if the input isn't encrypt or decrypt print invalid input 
  else:
    print("Invalid Input")
  j=(input("enter y to continue: "))
