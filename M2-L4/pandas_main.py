import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"C:\Users\User\Desktop\GEG-AI-Training\M2-L4\Bitcoin Historical Data Monthly.csv")

# Convert Date (US format)
df["Date"] = pd.to_datetime(df["Date"], format="%m/%d/%Y")

# Remove commas and convert Price to float
df["Price"] = df["Price"].str.replace(",", "").astype(float)

# Sort by date (your dataset is descending)
df = df.sort_values("Date")

# Plot
plt.figure(figsize=(10,6))
plt.plot(df["Date"], df["Price"], marker="o")

plt.title("Stock Price Over Time| Period Monthly")
plt.xlabel("Date")
plt.ylabel("Price")

plt.grid(True)

plt.show()



# Duke perdor line chart shfaq diagramin e BTC , timeframe = Daily,weekly , monthly , period 1 year 