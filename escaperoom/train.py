def main():
    i = 0;
    while (i < 3):
        combination = input('Where will Suzanne attack? (PLACENAME)\n')
        if (combination == "DISNEYLANDANAHEIM"):
            print("Take card #3\n")
            return;
        else:
            print("Incorrect, try again.\n")
            i = i+1
    print("Take card #26\n")
    return;

if __name__ == "__main__":
    main()
