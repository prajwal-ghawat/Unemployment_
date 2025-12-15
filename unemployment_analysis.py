import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Use a clean style
plt.style.use("ggplot")

# Load dataset
df = pd.read_csv(r"D:\Oasis_Infobyte_Projects\Unemployment-Analysis-with-Python-main\Unemployment_in_India_cleaned.csv", parse_dates=["Date"]
)

print(df.head())


# ===================== TIME TREND ANALYSIS =====================

plt.figure(figsize=(12, 6))
sns.lineplot(data=df.sort_values("Date"), x="Date", y="Estimated Unemployment Rate (%)", color="darkred", linewidth=2.5 )

plt.title("Trend of Unemployment Rate in India Over the Years")
plt.xlabel("Timeline")
plt.ylabel("Unemployment Percentage")
plt.xticks(rotation=45)
plt.grid(True, linestyle=":", alpha=0.6)
plt.tight_layout()
plt.show()


# ===================== REGION-WISE ANALYSIS =====================

region_avg = (
    df.groupby("Region")["Estimated Unemployment Rate (%)"]
      .mean()
      .sort_values(ascending=False)
)

plt.figure(figsize=(12, 7))
region_avg.plot(kind="bar", color="teal", edgecolor="black")

plt.title("Regional Comparison of Average Unemployment Rate")
plt.ylabel("Average Unemployment (%)")
plt.xlabel("Region")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# ===================== MONTH-WISE ANALYSIS =====================

month_avg = df.groupby("Month_Name")["Estimated Unemployment Rate (%)"].mean()

# Correct calendar order
month_order = ["Jan","Feb","Mar","Apr","May","Jun",
               "Jul","Aug","Sep","Oct","Nov","Dec"]

month_avg = month_avg.reindex(month_order)

plt.figure(figsize=(10, 6))
month_avg.plot(kind="bar", color="slateblue", edgecolor="black")

plt.title("Monthly Average Unemployment Rate in India")
plt.ylabel("Unemployment Rate (%)")
plt.xlabel("Month")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# ===================== CORRELATION HEATMAP =====================

plt.figure(figsize=(8, 6))
sns.heatmap(
    df[[
        "Estimated Unemployment Rate (%)",
        "Estimated Employed",
        "Estimated Labour Participation Rate (%)"
    ]].corr(),
    annot=True,
    cmap="YlOrRd",
    linewidths=0.5
)

plt.title("Relationship Between Employment Indicators")
plt.tight_layout()
plt.show()
