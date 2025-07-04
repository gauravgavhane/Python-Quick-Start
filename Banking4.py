# Instance variable : Name, Amount, Address, AccountNo
# Instance method : CreateAccount(), DisplayAccountInfo()
# Class variable : Bank_Name ,ROI_On_FD
# Class method : DisplayBankInformation
# Static method : DisplayKYCInfo

class Bank_Account:
    Bank_Name = "HDFC bank PVT LTD"
    ROI_On_FD = 6.7

    def __init__(self):
        self.Name = ""
        self.Amount = 0
        self.Address = ""
        self.AccountNo = 0

    def CreateAccount(self):
        print("Enter your name : ")
        self.Name = input()

        print("Enter your initial amount : ")
        self.Amount = int(input())

        print("Enter your Address : ")
        self.Address = input()

        print("Enter your Account Number : ")
        self.AccountNo = int(input())

    def DisplayAccountInfo(self):
        print("-------- Your Account information is as below --------")
        print("Name of Account Holder : ", self.Name)
        print("Account Number : ", self.AccountNo)
        print("Address of Account Holder : ", self.Address)
        print("Current Amount in account : ", self.Amount)

    @classmethod
    def DisplayBankInformation(cls):
        print("Welcome to banking console")
        print("Name of our bank is : ", cls.Bank_Name)
        print("Rate of intrest we offer on fixed deposit is : ", cls.ROI_On_FD)

    @staticmethod
    def DisplayKYCInfo():
        print("Please consider below KYC information")
        print("According to the rules of Government of India you have to submit below documents")
        print("1 : Clear and recent passport size photo")
        print("2 : Photo of aadhar card")
        print("3 : Photo of PAN card")


def main():
    Bank_Account.DisplayKYCInfo()

    print("Name of bank : ", Bank_Account.Bank_Name)
    print("Rate of Intrest on Fixed deposit : ", Bank_Account.ROI_On_FD)

    Bank_Account.DisplayBankInformation()

    User1 = Bank_Account()
    User2 = Bank_Account()

    print("Creating the first account")
    User1.CreateAccount()

    print("Creating the second account")
    User2.CreateAccount()

    User1.DisplayAccountInfo()
    User2.DisplayAccountInfo()


if __name__ == "__main__":
    main()