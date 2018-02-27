def main():
    i = 0;
    while (i < 3):
        combination = input('What is the password?\n')
        if (combination == "enigmamachine"):
            print("Take card #14\n")
            return;
        else:
            print("Incorrect, try again (lowercase).\n")
            i = i+1
    print("Take card #30\n")
    return;

if __name__ == "__main__":
    main()
