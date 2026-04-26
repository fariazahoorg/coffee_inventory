import pandas as pd
# 1. Class
class Ingredient:
    def __init__(self,name,quantity):
        self.name = name
        self.quantity = quantity
    def use_item(self, amount):
        if amount > self.quantity:
            print("Not enough stock!")
        else:
            self.quantity -= amount
# 2. Load data
df = pd.read_csv("morning_stock.csv")
# Rename column
df = df.rename(columns={"Qty_kg": "Current Quantity"})
df["Current Quantity"] = df["Current Quantity"].astype(float)
# 3. Filter Coffee Beans
coffee_row = df[df["Ingredient"] == "Coffee Beans"]
if coffee_row.empty:
    print("Coffee Beans not found!")
else:
    name = coffee_row.iloc[0]["Ingredient"]
    quantity = coffee_row.iloc[0]["Current Quantity"]
    coffee = Ingredient(name,quantity )
    # 4. Use 2.5 kg
    coffee.use_item(2.5)
    # 5. Update dataframe
    df.loc[df["Ingredient"] == "Coffee Beans", "Current Quantity"] = coffee.quantity
    # Save file
    df.to_csv("evening_stock.csv", index=False)
    print(" Evening stock file created!")