# x = int(input("Enter x:"))
# y = int(input("Enter y:"))
# sum = x + y
# print('sum : ', sum)

# count = 0
# while (count < 9):
#    print ('The count is:', count)
#    count = count + 1

# print ("Good bye!")
# ==================================
# tup3 = "a", "b", "c", "d";
# for letter in 'Python':     # First Example
#    print ('Current Letter :', letter)

# fruits = ['banana', 'apple',  'mango']
# for index in range(len(fruits)):
#    print ('Current fruit : ', fruits[index])

# print ("Good bye!")
# ==================================

for num in range(10,21):  #to iterate between 10 to 20
   for i in range(2,num): #to iterate on the factors of the number
      if num%i == 0:      #to determine the first factor
         j=num/i          #to calculate the second factor
         print ('%d equals %d * %d' % (num,i,j))
         break #to move to the next number, the #first FOR
   else:                  # else part of the loop
      print (num, 'is a prime number')

i = 2
while(i < 100):
   j = 2
   while(j <= (i/j)):
      if not(i%j): break
      j = j + 1
   if (j > i/j) : print (i, " is prime")
   i = i + 1

print ("Good bye!")
# ==================================

# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append((1,2,3,4));
   print ("Values inside the function: ", mylist)
   return

# Now you can call changeme function
mylist = [10,20,30]
print (mylist)
changeme( mylist );
print ("Values outside the function: ", mylist)

# ==================================
#!/usr/bin/python

str = input("Enter your input: ");
print ("Received input is : ", str)

# ==================================

# x = int(input("Enter x:"))
# y = int(input("Enter y:"))
# z = "sum = " 

# sum = x + y
# # print(z)
# # print(z[0])   # prints "H"
# # print(z[1]) # prints "e"

# # print(z[0:2]) # prints "He"
# # print(z[2:4]) # prints "ll"
# # print(z[6:])  # prints "Python"
# print("sum = " + str(sum))

# ==================================

# s = "Hello PytHon"
 
# print(s + ' ' + s) # print concatenated string.
# print(s.replace('H','T')) # print a string with a replaced word
 
# # convert string to uppercase
# g = s[0:2].upper()
# print(g)
 
# # convert to lowercase
# h = s[3:].lower()
# print(h)

# ==================================

# sentence = "The cat is brown"
# q = "cat"
 
# if q in sentence:
#     print('strings equal')
 
# if q == sentence:
#     print(q + " found in " + sentence)

# str1 = "The word \"computer\" will be \tin quotes."
# print(str1)

# ==================================
# l = [ "Drake", "Derp", "Derek", "Dominique" ]
 
# print (l)                # prints all elements
# l.sort()    # sorts the list in alphabetical order
# print (l)     # prints all elements

# l.append("Victoria")   # add element.
# print (l)                # print all elements
# l.remove("Derp")       # remove element.
# l.remove("Drake")      # remove element.
# print (l)   
# Info = ("Diana", 32, "New York")
# print(Info[0])
# print(Info[1])

# ==================================

# #!/usr/bin/env python
 
# name,age,country,career = ('Diana',32,'Canada','CompSci')
# print(name + str(age))

# x = (3,4,5,6)
# x = x + (1,2,3)
# print(x)

# ==================================

# listNumbers = [6,3,7,4]
# x = tuple(listNumbers)
# print(x)

# person = ('Diana','Canada','CompSci')
# s = ' '.join(person)
# print(person)
# print(s)
# # ==================================

# person = ('Alison','Victoria','Brenda','Rachel','Trevor')
# person = tuple(sorted(person))
# print(person)

# # ==================================

# words = {}
# words["Hello"] = "Bonjour"
# words["Yes"] = "Oui"
# words["No"] = "Non"
# words["Bye"] = "Au Revoir"
 
# print (words)            # print key-pairs.
# del words["Yes"]       # delete a key-pair.
# print (words)            # print key-pairs.
# words["Yes"] = "Oui!"  # add new key-pair.
# print (words)  

# if true:
#     print(words)