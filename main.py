from colorama import Fore
import numpy as np
import pandas as pnds
import matplotlib.pyplot as plt
import seaborn as sns

# get data path

data = input(Fore.GREEN + "Enter Data File Path: " + Fore.LIGHTGREEN_EX)

# check and load data

def check_is_found(type, path):
    if (type == "csv"):
        try:
            return pnds.read_csv(path)
        except FileNotFoundError:
            print(Fore.LIGHTRED_EX + "FILE NOT FOUND" + Fore.RESET)
    else:
        try:
            return pnds.read_excel(path)
        except FileNotFoundError:
            print(Fore.LIGHTRED_EX + "FILE NOT FOUND" + Fore.RESET)

if (data.endswith(".csv")):
    data = check_is_found("csv", data)
elif (data.endswith(".xlsx")):
    data = check_is_found("xlsx", data)
else:
    print(Fore.RED + "FILE TYPE INVAILD OR PATH NOT VAILD" + Fore.RESET)

# drop rows content null values

data = data.dropna()

# rename columns

data = data.rename(columns={"Year": "year", "Month": "month", "Total": "total", "Charter": "charter", "Scheduled": "scheduled"})

# generate charts

ybins = data["year"].max() - data["year"].min()
plt.hist(data["year"], bins=ybins, rwidth=0.9)
plt.title("Years")
plt.xlabel("Year")
plt.ylabel("Count")
plt.show()

plt.hist(data["month"], bins=12, rwidth=0.9)
plt.title("Months")
plt.xlabel("Month")
plt.ylabel("Count")
plt.show()

plt.hist(data["carriergroup"])
plt.title("Carrier Groups")
plt.xlabel("Groups")
plt.ylabel("Count")
plt.show()

plt.hist(data["scheduled"], rwidth=0.9)
plt.title("Scheduled")
plt.ylabel("Count")
plt.show()

plt.hist(data["charter"], rwidth=0.9)
plt.title("Charters")
plt.ylabel("Count")
plt.show()

plt.scatter(data["year"], data["total"])
plt.title("Totals In Years")
plt.xlabel("Years")
plt.ylabel("Count")
plt.show()

plt.scatter(data["month"], data["total"])
plt.title("Totals In Months")
plt.xlabel("Months")
plt.ylabel("Count")
plt.show()