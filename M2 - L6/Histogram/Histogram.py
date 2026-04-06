import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
daily = pd.read_csv(
    r"C:\Users\Admin\Desktop\GEG-AI-Training\M2 - L6\Bitcoin Historical Data Daily.csv"
)

weekly = pd.read_csv(
    r"C:\Users\Admin\Desktop\GEG-AI-Training\M2 - L6\Bitcoin Historical Data Weekly.csv"
)

monthly = pd.read_csv(
    r"C:\Users\Admin\Desktop\GEG-AI-Training\M2 - L6\Bitcoin Historical Data Monthly.csv"
)

# Function to clean price column
def clean_price(df):
    df["Price"] = df["Price"].str.replace(",", "", regex=False).astype(float)
    return df

daily = clean_price(daily)
weekly = clean_price(weekly)
monthly = clean_price(monthly)

# Create figure
plt.figure(figsize=(15,5))

# Daily histogram
plt.subplot(1,3,1)
plt.hist(daily["Price"], bins=30)
plt.title("Daily Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")

# Weekly histogram
plt.subplot(1,3,2)
plt.hist(weekly["Price"], bins=30)
plt.title("Weekly Price Distribution")
plt.xlabel("Price")

# Monthly histogram
plt.subplot(1,3,3)
plt.hist(monthly["Price"], bins=20)
plt.title("Monthly Price Distribution")
plt.xlabel("Price")

plt.tight_layout()

# Save chart
plt.savefig(
r"C:\Users\Admin\Desktop\GEG-AI-Training\M2 - L6\bitcoin_histograms.png",
dpi=300
)

plt.show()