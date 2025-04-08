def Maximum(value1, value2):
    if value1 > value2:
        return value1
    else:
        return  value2

def main():
    print("Enter first number : ")
    no1 = input()

    print("Enter second number : ")
    no2 = input()

    ans = Maximum(int(no1),int(no2))

    print("Largest number is ",ans)

if __name__ == "__main__":
    main()