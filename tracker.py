import pandas as pd
import csv
from datetime import datetime
from input import*

class CSV:
    FORMAT="%d-%m-%Y"
    
    CSV_FILE="finance_data.csv"
    COLUMNS=["date","amount","category","description"]
    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df=pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE,index=False)
    
    @classmethod
    def add_entry(cls,date,amount,category,description):
        new_entry={
            "date":date,
            "amount":amount,
            "category":category,
            "description":description
         }
        with open(cls.CSV_FILE, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("Entry added successfully!")

    
    @classmethod
    def get_transactions(cls,start_date,end_date):
        df=pd.read_csv(cls.CSV_FILE)
        df["Date"] = pd.to_datetime(df["Date"],format=CSV.FORMAT)
        start_date = datetime.strptime(start_date,CSV.FORMAT)
        end_date = datetime.strptime(end_date,CSV.FORMAT)

        mask= (df["Date"] >= start_date) & (df["Date"] <= end_date)
        filtered_df= df.loc[mask]

        if filtered_df.empty:
            print("No transations are found.")

        else:
            print(
                f"Transactions from {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)}"
            )
            print(filtered_df.to_string(index=False, formatters={"Date": lambda x: x.strftime(CSV.FORMAT)}))

            total_income = filtered_df[filtered_df["category"] == "Income"]["amount"].sum()
            total_expense = filtered_df[filtered_df["category"] == "Expense"]["amount"].sum()
            print("\nSummary: ")
            print(f"Total Income: 💲{total_income :.2f}")
            print(f"Total Expense: 💲{total_expense :.2f}")
            print(f"Net Savings: 💲{(total_income-total_expense) :.2f} ")

        return filtered_df
            

def add():
    CSV.initialize_csv()
    date=get_date("Enter the date of the transaction(dd-mm-yyyy) or enter today's date:",allow_default=True)
    amount=get_amount()
    category=get_category()
    description=get_description()
    CSV.add_entry(date,amount,category,description)

def plot_transaction():  #left for further implementation (create a plot using MATPLOTLIB)
    pass 


def main():
    while True:
        print("\n1. Add a new transaction")
        print("2. view transation and summary within a date range")
        print("3. Exit")
        print("\n")
        choice = input("Select Your choice(1-3): ")


        if choice == "1":
            add()
        
        elif choice == "2":
            start_date=get_date("Enter the start date (dd-mm-yyyy): ")
            end_date=get_date("Enter the end date (dd-mm-yyyy): ")
            df=CSV.get_transactions(start_date,end_date)


        elif choice == "3":
            print("Exiting....")
            break


        else:
            print("Invalid Input")


if __name__=="__main__":
    main()

