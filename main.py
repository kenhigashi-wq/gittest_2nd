#Hols the entire user interface

chars = []

def main():
    choice = input("Select 1 to create a character and 2 ro exit")

    if choice == "1":
        chars.append(charCreator())
    else:
        pass

main()