import pandas as pd

# Define the dataset directly
data = {
    'title': ['Video A', 'Video B', 'Video C', 'Video D', 'Video E'],
    'views': [12000, 34000, 56000, 78000, 15000],
    'likes': [400, 1200, 2100, 3300, 800],
    'dislikes': [30, 60, 120, 90, 50],
    'comment_count': [50, 230, 340, 500, 150]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Calculate totals
total_views = df['views'].sum()
total_likes = df['likes'].sum()
total_dislikes = df['dislikes'].sum()
total_comments = df['comment_count'].sum()

# Display results
print(f"Total Views: {total_views}")
print(f"Total Likes: {total_likes}")
print(f"Total Dislikes: {total_dislikes}")
print(f"Total Comments: {total_comments}")
