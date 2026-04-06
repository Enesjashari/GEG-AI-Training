import pandas as pd
import mplfinance as mpf

# Load dataset
# df = pd.read_csv(r"C:\Users\Admin\Desktop\GEG-AI-Training\M2 - L5\Bitcoin Historical Data Daily.csv")
df = pd.read_csv(r"C:\Users\Admin\Desktop\GEG-AI-Training\M2 - L5\Bitcoin Historical Data Weekly.csv")
# df = pd.read_csv(r"C:\Users\Admin\Desktop\GEG-AI-Training\M2 - L5\Bitcoin Historical Data Monthly.csv")

# Convert Date
df["Date"] = pd.to_datetime(df["Date"], format="%m/%d/%Y")

# Remove commas
cols = ["Price","Open","High","Low"]
for c in cols:
    df[c] = df[c].str.replace(",", "").astype(float)

# Rename Price → Close
df = df.rename(columns={"Price":"Close"})

# Sort by date
df = df.sort_values("Date")

# Set index
df.set_index("Date", inplace=True)

# Candlestick + Moving Averages
mpf.plot(
    df,
    type="candle",
    style="yahoo",
    # mav=(20,50),   # Daily
    mav=(4,12),   # Weekly
    # mav=(3,5),   # Monthly
    title="Bitcoin Candlestick with Moving Averages",
    ylabel="Price",
    figsize=(10,6)
)