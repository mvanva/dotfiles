def main():
    i = 0;
    while (i < 3):
        combination = input('What is the combination?\n')
        if (combination == "013088"):
            print("Take card #7\n")
            return;
        else:
            print("Incorrect, try again.\n")
            i = i+1
    print("Take card #15\n")
    return;

if __name__ == "__main__":
    main()
