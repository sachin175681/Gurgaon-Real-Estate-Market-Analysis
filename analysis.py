# ==========================
# Import Libraries
# ==========================
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data Loading and Initial Understanding
df = pd.read_csv("dataset.csv")
print(df.head())
print(df.shape)  #give row*coloumn

# Standardize Column Names
df.columns = df.columns.str.strip().str.lower().str.replace(" ","_").tolist()
print(df.columns)

# Convert Numeric Columns
df['price'] = df["price"].astype(str).str.replace(",","").astype(float)
df['area'] = df["area"].astype(str).str.replace(",","").astype(int)
df['rate_per_sqft'] = df["rate_per_sqft"].astype(str).str.replace(",","").astype(int)
print(df["rate_per_sqft"])


# Clean Categorical Columns
df["status"] = df["status"].str.strip().str.lower()
df['rera_approval'] = df['rera_approval'].str.strip().str.lower().map({'approved by rera': True, 'not approved by rera': False})
df['flat_type'] = df['flat_type'].str.strip().str.lower()

# Remove Duplicates
df = df.drop_duplicates()
print(df.info())


#1 Which is the costliest flat in the dataset?
costliest_flat = df.loc[df["price"].idxmax()]
# print(costliest_flat)

#2 Which locality has the highest average price?
highe_avg_price_locality = df.groupby("locality")["price"].mean().idxmax()
# print(highe_avg_price_locality)

#3 Which locality has the highest rate per square foot?
highestRatePerSQFT = df.groupby("locality")["rate_per_sqft"].mean().idxmax()
# print(highestRatePerSQFT)

#4  Ready-to-move vs Under-construction pricing
ready_to_move_avgPrice = df[df['status'] == 'ready to move']['price'].mean()
under_construction_avgPrice = df[df['status'] == 'under construction']['price'].mean()
if ready_to_move_avgPrice > under_construction_avgPrice:
    print("ready_to_move property has greater cost")
else:
    print("ready_to_move property has lower cost")
print(ready_to_move_avgPrice, under_construction_avgPrice)

# 5 rera approved has price premium?
rera_approval = df[df["rera_approval"]==True]["price"].mean()
rera_non_approval = df[df["rera_approval"]==False]["price"].mean()
if rera_approval > rera_non_approval:
    print("rera approval property has price premium")
else:
    print("rera approval property doesn't have price premium")

#6 area vs price 
sns.scatterplot(data=df, x='area', y='price')
plt.show()

#7 most expensive bhk bsed on sqft
expensive_bhk = df.groupby('bhk_count')['rate_per_sqft'].mean().idxmax()
print(f"Most expensive BHK (average price per sqft): {expensive_bhk}")

#8 most expensive flat type
most_expensive_flat = df.groupby('flat_type')['price'].mean().idxmax()
print(most_expensive_flat)

#9 top 5 builder
top_5_builder = df.groupby('company_name')['rate_per_sqft'].mean().sort_values(ascending=False).head(5)
print(top_5_builder)

#10 Are larger homes more expensive per sqft?
sns.scatterplot(x="area", y="rate_per_sqft", data=df)
plt.show()