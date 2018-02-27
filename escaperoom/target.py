def main():
    i = 0;
    while (i < 3):
        combination = input('Who will Suzanne attack? (FIRST LAST)\n')
        if (combination == "ZOE WALKER"):
            print("Take card #23\n")
            return;
        else:
            print("Incorrect, try again.\n")
            i = i+1
    print("Take card #5\n")
    return;

if __name__ == "__main__":
    main()
