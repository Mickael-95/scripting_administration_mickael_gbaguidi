# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def is_year_leap(arg):
    if arg % 4 == 0 and arg % 100 != 0 or arg % 400 == 0:
        print("Année bissextile!")
    else:
        print("Année non bissextile!")

while True:
    year: int = input("Entrez une année pour savoir si elle est bisextile : ")
    if year == "x":
        exit()
    int_year = int(year)
    is_year_leap(int_year)