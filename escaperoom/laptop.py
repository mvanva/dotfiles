def main():
    i = 0;
    while (i < 3):
        combination = input('What is the password?\n')
        if (combination == "password"):
            print("Take card #8\n")
            return;
        else:
            print("Incorrect, try again (lowercase).\n")
            i = i+1
    print("Take card #29\n")
    return;

if __name__ == "__main__":
    main()
