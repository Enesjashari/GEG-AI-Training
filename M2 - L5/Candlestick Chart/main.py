import pandas as pd
import mplfinance as mpf

# Load dataset
# df = pd.read_csv(r"C:\Users\Admin\Desktop\GEG-AI-Training\M2 - L5\Bitcoin Historical Data Weekly.csv")
# df = pd.read_csv(r"C:\Users\Admin\Desktop\GEG-AI-Training\M2 - L5\Bitcoin Historical Data Daily.csv")
df = pd.read_csv(r"C:\Users\Admin\Desktop\GEG-AI-Training\M2 - L5\Bitcoin Historical Data Monthly.csv")

# Convert Date
df["Date"] = pd.to_datetime(df["Date"], format="%m/%d/%Y")

# Remove commas from numeric columns
cols = ["Price","Open","High","Low"]
for c in cols:
    df[c] = df[c].str.replace(",", "").astype(float)

# Rename Price → Close
df = df.rename(columns={"Price":"Close"})

# Sort by date
df = df.sort_values("Date")

# Set Date index
df.set_index("Date", inplace=True)

# Candlestick chart
mpf.plot(
    df,
    type="candle",
    style="yahoo",
    title="Bitcoin Candlestick Chart (Weekly)",
    ylabel="Price",
    figsize=(10,6)
)




# Donwload Boeing stock data Time Frame 1 Y |  Monthly , Weekly , Daily
# Krijoni Line Chart dhe CandleStick Chart per te vizualizuar te dhenat e Boeing stock data

# 10 Minuta
