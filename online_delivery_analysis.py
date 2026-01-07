import pandas as pd

df = pd.read_csv("dataset .csv")
df = df[['Has Online delivery', 'Aggregate rating']].dropna()
df['Has Online delivery'] = df['Has Online delivery'].replace({
    'Yes': 1,
    'No': 0
})

delivery_counts = df['Has Online delivery'].value_counts()
total_restaurants = delivery_counts.sum()
online_delivery_percentage = (delivery_counts.get(1, 0) / total_restaurants) * 100
no_delivery_percentage = (delivery_counts.get(0, 0) / total_restaurants) * 100

print(f"\nPercentage of Restaurants with Online Delivery: {online_delivery_percentage:.2f}%")
print(f"Percentage of Restaurants without Online Delivery: {no_delivery_percentage:.2f}%")

average_ratings = (
    df.groupby('Has Online delivery')['Aggregate rating']
    .mean()
)

print("\nAverage Ratings Comparison:\n")
print(average_ratings)

summary_df = pd.DataFrame({
    'Category': ['With Online Delivery', 'Without Online Delivery'],
    'Percentage (%)': [
        round(online_delivery_percentage, 2),
        round(no_delivery_percentage, 2)
    ],
    'Average Rating': [
        round(average_ratings.get(1, 0), 2),
        round(average_ratings.get(0, 0), 2)
    ]
})

summary_df.to_csv(
    "output/online_delivery_analysis.csv", index=False
)

print("\nResults saved to output/online_delivery_analysis.csv")
