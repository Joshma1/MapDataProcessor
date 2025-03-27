import json
import pandas as pd

# Sample JSON data
locations_json = [
    {"id": "loc_01", "latitude": 37.7749, "longitude": -122.4194},
    {"id": "loc_04", "latitude": 27.8749, "longitude": 122.4194},
    {"id": "loc_05", "latitude": 57.2749, "longitude": -112.4344},
    {"id": "loc_06", "latitude": 14.0522, "longitude": -119.2531},
    {"id": "loc_07", "latitude": 64.0522, "longitude": -108.2330},
    {"id": "loc_02", "latitude": 34.0522, "longitude": -118.2437},
    {"id": "loc_08", "latitude": 24.0522, "longitude": -168.2197},
    {"id": "loc_03", "latitude": 40.7128, "longitude": -74.0060}
]

metadata_json = [
    {"id": "loc_01", "type": "restaurant", "rating": 4.5, "reviews": 120},
    {"id": "loc_04", "type": "restaurant", "rating": 4.1, "reviews": 500},
    {"id": "loc_05", "type": "restaurant", "rating": 3.7, "reviews": 110},
    {"id": "loc_02", "type": "hotel", "rating": 4.2, "reviews": 200},
    {"id": "loc_06", "type": "hotel", "rating": 4.0, "reviews": 700},
    {"id": "loc_07", "type": "hotel", "rating": 2.0, "reviews": 900},
    {"id": "loc_03", "type": "cafe", "rating": 4.7, "reviews": 150},
    {"id": "loc_08", "type": "cafe", "rating": 4.5, "reviews": 750}
]

# Convert JSON data to DataFrames
locations_df = pd.DataFrame(locations_json)
metadata_df = pd.DataFrame(metadata_json)

# Merge the data on 'id'
merged_df = pd.merge(locations_df, metadata_df, on="id", how="outer")

# Count valid points per type
valid_points_count = merged_df["type"].value_counts()

# Calculate average rating per type
average_rating = merged_df.groupby("type")["rating"].mean()

# Identify the location with the highest number of reviews
highest_reviews_location = merged_df.loc[merged_df["reviews"].idxmax()]

# Identify locations with incomplete data
incomplete_data = merged_df[merged_df.isnull().any(axis=1)]

# Print results
print("Valid Points Count Per Type:")
print(valid_points_count)
print("\nAverage Rating Per Type:")
print(average_rating)
print("\nLocation with the Highest Number of Reviews:")
print(highest_reviews_location)
print("\nLocations with Incomplete Data:")
print(incomplete_data)