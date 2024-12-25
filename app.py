import os
import platform
import pandas as pd
from enum import Enum

class Actions(Enum):
    Highest_Price = 1
    Average_Price = 2
    Amount_of_Ideal_Cut_Diamonds = 3
    How_Many_Different_Colors_And_What_Are_They = 4
    Median_Carat_of_Premium_Cut_Diamonds = 5
    Average_Carat_for_Every_Cut = 6
    Average_Price_for_Every_Color = 7
    Exit = 8

diamonds = pd.read_csv("diamonds.txt")

def clear_terminal():
    if platform.system()== 'Windows':
        os.system("cls")
    else:
        os.system("clear")

# 1 highest price
def highest_price(df):
    return df['price'].max()

# 2 avg price
def avg_price(df):
    return df['price'].mean()
	
# 3 how many of ideal cut
def amount_of_cut(df, type):
    return len(df[df['cut'] == type])

# 4 how many different colors + what are all colors
def different_colors(df):
	return df['color'].unique()

def printing_colors(df):
    colors = different_colors(df)
    print(f"The number of different colors is: {len(colors)}")
    print("The different colors are:")
    for color in colors:
        print(color)

# 5 median of carat only for premium cut!
def median_carat_of_cut(type):
	return diamonds[diamonds['cut'] == type]['carat'].median()

# 6 avg carat for each cut
def avg_carat_for_every_cut(df):
    return df.groupby('cut')['carat'].mean()

def printing_avg_carats_for_every_cut(df):
    averages = avg_carat_for_every_cut(df)
    for cut, avg in averages.items():
        print(f"the average carat for {cut} is {avg}")

# 7 avg price for each color
def avg_price_for_each_color(df):
    return df.groupby('color')['price'].mean()

def printing_avg_price_for_each_color(df):
    averages = avg_price_for_each_color(df)
    for color, avg in averages.items():
        print(f"the average price for a diamond in the color {color} is {avg}")

# menu, main and entry point from this point on
def menu():
    for act in Actions:
        print(f"{act.value} - {act.name}")
    return input("your selection: ")

def main():
    while True:
        user_selection = Actions(int(menu()))
        clear_terminal()
        if user_selection == Actions.Highest_Price: print(highest_price(diamonds))
        elif user_selection == Actions.Average_Price: print(avg_price(diamonds))
        elif user_selection == Actions.Amount_of_Ideal_Cut_Diamonds: print(amount_of_cut(diamonds,"Ideal"))
        elif user_selection == Actions.How_Many_Different_Colors_And_What_Are_They: printing_colors(diamonds)
        elif user_selection == Actions.Median_Carat_of_Premium_Cut_Diamonds: print(median_carat_of_cut("Premium"))
        elif user_selection == Actions.Average_Carat_for_Every_Cut: printing_avg_carats_for_every_cut(diamonds)
        elif user_selection == Actions.Average_Price_for_Every_Color: printing_avg_price_for_each_color(diamonds)
        elif user_selection == Actions.Exit: exit()
        else: print("wrong key. try again please.")

if __name__ == "__main__":
	main()