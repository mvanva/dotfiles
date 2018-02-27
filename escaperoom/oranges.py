def main():
    i = 0;
    while (i < 3):
        combination = input('When will Suzanne attack? (Month day)\n')
        if (combination == "June 7" or combination == "June 07"):
            print("Take card #6\n")
            return;
        else:
            print("Incorrect, try again.\n")
            i = i+1
    print("Take card #2\n")
    return;

if __name__ == "__main__":
    main()
