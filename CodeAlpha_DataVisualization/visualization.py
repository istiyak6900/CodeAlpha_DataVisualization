import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("netflix_titles.csv")

# Set style
sns.set(style="darkgrid")

# -----------------------------
# 1. Movies vs TV Shows
# -----------------------------
plt.figure(figsize=(6,4))
sns.countplot(x='type', data=df)
plt.title("Movies vs TV Shows on Netflix")
plt.savefig("movies_vs_tvshows.png")
plt.show()

# -----------------------------
# 2. Top 10 Countries
# -----------------------------
top_countries = df['country'].value_counts().head(10)

plt.figure(figsize=(10,5))
top_countries.plot(kind='bar')
plt.title("Top 10 Countries with Most Netflix Content")
plt.xlabel("Country")
plt.ylabel("Count")
plt.savefig("top_countries.png")
plt.show()

# -----------------------------
# 3. Content Added Per Year
# -----------------------------
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['year_added'] = df['date_added'].dt.year

plt.figure(figsize=(10,5))
df['year_added'].value_counts().sort_index().plot(kind='line')
plt.title("Netflix Content Added Over Years")
plt.xlabel("Year")
plt.ylabel("Number of Shows")
plt.savefig("content_over_years.png")
plt.show()

print("Visualization project completed successfully!")