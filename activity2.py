
tuple_ko = ("zeus","posiedon", "hades")         #this is the tuple
print(f"This is the current tuple: {tuple_ko}")

def main(tuple_ko): #def main then connect it to the tupless
    while True:             #naka loop for the attempts and error-handling
            try:
                listahan = list(tuple_ko)           #turning the tuple into a list
                listahan[0] = input("Enter to modify the 1st element of the tuple: ")
                tuple_ko = tuple(listahan)
                print(f"This is the modified tuple: {tuple_ko}")
                break
            except(ValueError, KeyError, KeyboardInterrupt, EOFError):
                print("Error: Tuples are immutable.")
main(tuple_ko)