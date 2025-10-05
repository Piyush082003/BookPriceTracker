import pandas as pd
import matplotlib.pyplot as plt

# Load Excel file
df = pd.read_excel("books_data.xlsx")

# ✅ Clean Rating Text → Convert to Numbers
rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
df["Rating_Num"] = df["Rating"].map(rating_map)

# ✅ Clean Price Column (remove “Â”, “£”, whitespace)
df["Price_Num"] = (
    df["Price"]
    .astype(str)
    .str.replace("Â", "", regex=False)
    .str.replace("£", "", regex=False)
    .str.strip()
    .astype(float)
)

# -----------------------------
# 📈 1. Bar Chart: Books per Rating
# -----------------------------
rating_counts = df["Rating_Num"].value_counts().sort_index()

plt.figure(figsize=(6, 4))
plt.bar(rating_counts.index, rating_counts.values)
plt.xlabel("Book Rating (1–5 Stars)")
plt.ylabel("Number of Books")
plt.title("Books Count by Rating")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.savefig("books_by_rating.png", dpi=300, bbox_inches="tight")
plt.show()

# -----------------------------
# 🥧 2. Pie Chart: Stock Availability
# -----------------------------
availability_counts = df["Availability"].value_counts()

plt.figure(figsize=(5, 5))
availability_counts.plot.pie(autopct="%1.1f%%", startangle=90)
plt.title("Book Stock Availability")
plt.ylabel("")
plt.savefig("stock_availability.png", dpi=300, bbox_inches="tight")
plt.show()

# -----------------------------
# 💰 3. Histogram: Price Distribution
# -----------------------------
plt.figure(figsize=(6, 4))
plt.hist(df["Price_Num"], bins=15, edgecolor="black")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")
plt.title("Book Price Distribution")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.savefig("price_distribution.png", dpi=300, bbox_inches="tight")
plt.show()

print("✅ All charts saved successfully!")
