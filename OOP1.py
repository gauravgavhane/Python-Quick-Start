class Arithmatic:
    def __init__(self,A,B):
        print("Inside init method")
        self.No1 = A
        self.No2 = B

    def Addition(self):
        Ans = self.No1 + self.No2
        return Ans

    def Subtraction(self):
        Ans = self.No1 - self.No2
        return Ans

def main():
    print("Inside main method")

    obj = Arithmatic(11,20)
    Output = obj.Addition()
    print("Addition is ", Output)
    Output = obj.Subtraction()
    print("Subtraction is ",Output)


if __name__ == "__main__":
    print("Inside starter")
    main()