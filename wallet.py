#create a wallet
#take the number of people
#maintain the amount given by each user
#add the transactions
#split the transactions based on the selected option(equal split or individual split)
#record how much was deducted from each user

from tracker import*

class Wallet():
    def __init__(self,split_name,participants):
        self.split_name=split_name
        self.participants=participants
        print(
            f"The name of the Split is {self.split_name} and there are {self.participants} people in the group"
             )
        print("Creating wallet for the current Requirement.........")



    def names_of_people(self):
        self.names=[]
        for i in range (0, self.participants):
            name=input("Enter the name of participants: ")
            self.names.append(name)
        print(self.names)



    def add_amount_into_wallet(self):
        pool_amount=0
        for name in self.names:
            individual_amount=int(input(f"enter the amount contibuted by {name}: "))
            pool_amount+=individual_amount
        print(pool_amount,": is the total amount in the wallet")    


            
    
        

        
W1 = Wallet("kukke Ride",4)
W1.names_of_people()
W1.add_amount_into_wallet()
