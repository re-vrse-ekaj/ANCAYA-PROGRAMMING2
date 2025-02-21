dami = int(input("Enter a number of contacts: "))
address_book = {}

for i in range (1,dami+1):

    name = input("enter your name: ")
    number = int(input("enter your number: "))
    address_book.update({name:number})
print(address_book)

sear = input("Lookup name: ")

if sear in address_book:
    print(f"number: {number}")
else:
    print("name not found")            