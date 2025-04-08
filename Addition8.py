print("Application for the addition with module")

import AddModule

def main():
    print("Value of  __name__ from main is ",__name__)

    print("Enter the first number : ")
    no1 = input()
    print("Enter second number : ")
    no2 = input()

    Sum = AddModule.Addition(no1,no2)

    print("Addition is ",Sum)

if __name__ == "__main__":
    main()