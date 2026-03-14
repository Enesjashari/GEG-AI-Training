# import pandas as pd
# import matplotlib.pyplot as plt

# # Load dataset
# df = pd.read_csv(r"C:\Users\Admin\Desktop\GEG-AI-Training\M2 - L6\Bitcoin Historical Data Daily.csv")

# # Convert Date
# df["Date"] = pd.to_datetime(df["Date"], format="%m/%d/%Y")

# # Clean numbers
# df["Price"] = df["Price"].str.replace(",", "").astype(float)

# # Sort ascending
# df = df.sort_values("Date")

# # Bollinger settings
# window = 20
# num_std = 2

# # Calculate indicators
# df["SMA"] = df["Price"].rolling(window).mean()
# df["STD"] = df["Price"].rolling(window).std()

# df["Upper_Band"] = df["SMA"] + (df["STD"] * num_std)
# df["Lower_Band"] = df["SMA"] - (df["STD"] * num_std)

# # Plot
# plt.figure(figsize=(12,6))

# plt.plot(df["Date"], df["Price"], label="Price")
# plt.plot(df["Date"], df["SMA"], label="20 Day SMA")
# plt.plot(df["Date"], df["Upper_Band"], label="Upper Band")
# plt.plot(df["Date"], df["Lower_Band"], label="Lower Band")

# plt.fill_between(df["Date"], df["Upper_Band"], df["Lower_Band"], alpha=0.2)

# plt.title("Bitcoin Bollinger Bands")
# plt.xlabel("Date")
# plt.ylabel("Price")
# plt.xticks(rotation=45)
# plt.legend()

# plt.tight_layout()

# # Save image locally
# plt.savefig(r"C:\Users\Admin\Desktop\GEG-AI-Training\M2 - L6\daily_bollinger_bands_chart.png")

# plt.show()





# import pandas as pd
# import matplotlib.pyplot as plt

# # Load dataset
# df = pd.read_csv(
#     r"C:\Users\Admin\Desktop\GEG-AI-Training\M2 - L6\Bitcoin Historical Data Weekly.csv"
# )

# # Convert date
# df["Date"] = pd.to_datetime(df["Date"], format="%m/%d/%Y")

# # Clean price column
# df["Price"] = df["Price"].str.replace(",", "", regex=False).astype(float)

# # Sort ascending
# df = df.sort_values("Date").reset_index(drop=True)

# # Bollinger settings
# window = 20
# num_std = 2

# # Calculate indicators
# df["SMA"] = df["Price"].rolling(window=window).mean()
# df["STD"] = df["Price"].rolling(window=window).std()

# df["Upper_Band"] = df["SMA"] + (num_std * df["STD"])
# df["Lower_Band"] = df["SMA"] - (num_std * df["STD"])

# # Remove rows where SMA is NaN (first 19 rows)
# df = df.dropna()

# # Plot
# plt.figure(figsize=(12,6))

# plt.plot(df["Date"], df["Price"], label="Price")
# plt.plot(df["Date"], df["SMA"], label="20 Week SMA")
# plt.plot(df["Date"], df["Upper_Band"], label="Upper Band")
# plt.plot(df["Date"], df["Lower_Band"], label="Lower Band")

# plt.fill_between(
#     df["Date"],
#     df["Upper_Band"],
#     df["Lower_Band"],
#     alpha=0.15
# )

# plt.title("Bitcoin Bollinger Bands (Weekly)")
# plt.xlabel("Date")
# plt.ylabel("Price")

# plt.xticks(rotation=45)
# plt.legend()

# plt.tight_layout()

# # Save chart
# plt.savefig(
#     r"C:\Users\Admin\Desktop\GEG-AI-Training\M2 - L6\weekly_bollinger_bands_chart.png",
#     dpi=300
# )

# plt.show()



import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(
    r"C:\Users\Admin\Desktop\GEG-AI-Training\M2 - L6\Bitcoin Historical Data Monthly.csv"
)

# Convert date
df["Date"] = pd.to_datetime(df["Date"], format="%m/%d/%Y")

# Clean price column
df["Price"] = df["Price"].str.replace(",", "", regex=False).astype(float)

# Sort ascending
df = df.sort_values("Date").reset_index(drop=True)

# Bollinger settings
window = 20
num_std = 2

# Calculate indicators
df["SMA"] = df["Price"].rolling(window=window).mean()
df["STD"] = df["Price"].rolling(window=window).std()

df["Upper_Band"] = df["SMA"] + (num_std * df["STD"])
df["Lower_Band"] = df["SMA"] - (num_std * df["STD"])

# Remove rows where SMA is NaN
df = df.dropna()

# Plot
plt.figure(figsize=(12, 6))

plt.plot(df["Date"], df["Price"], label="Price")
plt.plot(df["Date"], df["SMA"], label="20 Month SMA")
plt.plot(df["Date"], df["Upper_Band"], label="Upper Band")
plt.plot(df["Date"], df["Lower_Band"], label="Lower Band")

plt.fill_between(
    df["Date"],
    df["Upper_Band"],
    df["Lower_Band"],
    alpha=0.15
)

plt.title("Bitcoin Bollinger Bands (Monthly)")
plt.xlabel("Date")
plt.ylabel("Price")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

# Save chart
plt.savefig(
    r"C:\Users\Admin\Desktop\GEG-AI-Training\M2 - L6\Bollinger Bands Chart\monthly_bollinger_bands_chart.png",
    dpi=300
)

plt.show()