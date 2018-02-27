def main():
    i = 0;
    while (i < 3):
        combination = input('What is the combination?\n')
        if (combination == "898"):
            print("Take card #9\n")
            return;
        else:
            print("Incorrect, try again.\n")
            i = i+1
    print("Take card #33\n")
    return;

if __name__ == "__main__":
    main()
