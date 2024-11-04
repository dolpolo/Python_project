# Import Libraries 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import plotly.express as px 
import plotly.io as pio
from pathlib import Path
import os


# ==============================
# IMPORT DATSETS FOR TRUMP/BIDEN
# ==============================

# Define the base path
base_path = Path("C:/Users/Davide/Desktop/Alma Mater/SECOND YEAR/PYTHON/Python_project")
# Change the working directory
os.chdir(base_path)

# Define the full path to the CSV file for Trump and Biden
csv_path_trump = base_path / "data" / "hashtag_donaldtrump.csv"
csv_path_biden = base_path / "data" / "hashtag_joebiden.csv"

# Print the current working directory
print("Current Working Directory:", Path.cwd())

# Load the CSV files with pandas:
## trump 
try:
    trump = pd.read_csv(csv_path_trump, encoding="utf-8", engine='python', on_bad_lines='skip')
    print("First 5 rows of the DataFrame:")
    print(trump.head())
except Exception as e:
    print("Error loading the file:", e)

## biden 
try:
    biden = pd.read_csv(csv_path_biden, encoding="utf-8", engine='python', on_bad_lines='skip')
    print("First 5 rows of the DataFrame:")
    print(biden.head())
except Exception as e:
    print("Error loading the file:", e)



# ==============================
# DATA DESCRIPTION AND MERGING
# ==============================

### trump 

# Perform descriptive analysis
print("\nDescriptive Analysis:")
print(trump.head(10))  # Show first 10 rows
print("DataFrame Info:")
trump.info()  # Display DataFrame info
print("Statistical Description:")
print(trump.describe())  # Get statistical description of numeric columns
print("Shape of DataFrame:", trump.shape)  # Show shape of the DataFrame
print("Columns in DataFrame:", trump.columns)  # List column names
print("Data Types of Columns:")
print(trump.dtypes)  # Print data types of each column

# Get the data type of the 'tweet' column
tweet_type = trump['tweet'].dtype
print(f"\nThe data type of the 'tweet' column is: {tweet_type}")

# Check for missing values in the DataFrame
print("Missing values in each column:")
print(trump.isnull().sum())  # Show number of missing values per column
missing_tweets = trump['tweet'].isna().sum()
print(f"\nNumber of missing tweets: {missing_tweets}")  # Count missing tweets

# Drop rows with missing values in the 'tweet' column
trump = trump.dropna(subset=['tweet'])
print("DataFrame after dropping missing tweets:")
print(trump.head())  # Display the first few rows of the cleaned DataFrame


### biden

# Perform descriptive analysis
print("\nDescriptive Analysis:")
print(biden.head(10))  # Show first 10 rows
print("DataFrame Info:")
biden.info()  # Display DataFrame info
print("Statistical Description:")
print(biden.describe())  # Get statistical description of numeric columns
print("Shape of DataFrame:", biden.shape)  # Show shape of the DataFrame
print("Columns in DataFrame:", biden.columns)  # List column names
print("Data Types of Columns:")
print(biden.dtypes)  # Print data types of each column

# Get the data type of the 'tweet' column
tweet_type = biden['tweet'].dtype
print(f"\nThe data type of the 'tweet' column is: {tweet_type}")

# Check for missing values in the DataFrame
print("Missing values in each column:")
print(biden.isnull().sum())  # Show number of missing values per column
missing_tweets = biden['tweet'].isna().sum()
print(f"\nNumber of missing tweets: {missing_tweets}")  # Count missing tweets

# Drop rows with missing values in the 'tweet' column
biden = biden.dropna(subset=['tweet'])
print("DataFrame after dropping missing tweets:")
print(biden.head())  # Display the first few rows of the cleaned DataFrame


# creating a new column 'candidate' to differentiate between tweets of Trump and Biden upon concatination 
trump['candidate'] = 'trump'
biden['candidate'] = 'biden'

# combining the dataframes 
data = pd.concat([trump, biden]) 

# FInal data shape 
print('Final Data Shape :', data.shape) 


# ==============================
# DATA CLEANING (USA tweets)
# ==============================

# Reimposta l'indice come numerico
data.reset_index(inplace=True)  
data.iloc[971060:971080, 22]
data.loc[971060:971080, 'candidate']

# Since we are interested in USA we just keep the tweets correspondig to Country USA
data['country'].unique()
data['country'].value_counts()
data['country'] = data['country'].replace({'United States of America': "US",'United States': "US"}) 
data = data[data['country'] == 'US']

# Keep just a tweeter for each user_ID assuming he is coeherent with is political ideas (pro Trump or pro Biden)
data.drop_duplicates(subset=['user_id'])
data.shape

data.to_csv('data/data.csv', index=False)




# ==============================
# EXPLANATORY ANALYSIS
# ==============================

### Group the data by 'candidate' and count the number of tweets for each candidate 
tweets_count = data.groupby('candidate')['tweet'].count().reset_index() 

# Interactive bar chart 
fig_tweets = px.bar(tweets_count, x='candidate', y='tweet', color='candidate', 
color_discrete_map={'Trump': 'pink', 'Biden': 'blue'}, 
labels={'candidate': 'Candidates', 'tweet': 'Number of Tweets'}, 
title='Tweets for Candidates') 

# Show the chart 
pio.show(fig_tweets)

### Group the data by 'candidate' and count the number of likes for each candidate 
likes_comparison = data.groupby('candidate')['likes'].sum().reset_index() 
fig_likes = px.bar(likes_comparison, x='candidate', y='likes', color='candidate', 
color_discrete_map={'Trump': 'blue', 'Biden': 'green'}, 
labels={'candidate': 'Candidate', 'likes': 'Total Likes'}, 
title='Comparison of Likes') 

# Update the layout with a black theme 
# fig_likes.update_layout(plot_bgcolor='black', 
# paper_bgcolor='black', font_color='white') 

# Show the chart 
pio.show(fig_likes)

# Top10 states tweets Counts 
top20states = data.groupby('state_code')['tweet'].count().sort_values(ascending=False).reset_index().head(20) 
 
# Interactive bar chart 
fig_tweet_bystates = px.bar(top20states, x='state_code', y='tweet', 
template='plotly_dark', 
color_discrete_sequence=px.colors.qualitative.Dark24_r, 
title='Top10 states tweets') 

# To view the graph 
pio.show(fig_tweet_bystates)

# the number of tweets done for each candidate by all the states. 
tweet_df = data.groupby(['state_code', 'candidate'])['tweet'].count().reset_index() 

# Candidate for top 20 state_code tweet 
tweeters = tweet_df[tweet_df['state_code'].isin(top20states.state_code)] 

# Plot for tweet counts for each candidate in the top 20 state_code 
fig_state_tweet = px.bar(tweeters, x='state_code', y='tweet', color='candidate', 
                         labels={'state_code': 'state_code', 'tweet': 'Number of Tweets', 
                                 'candidate': 'Candidate'}, 
                                 itle='Tweet Counts for Each Candidate in the Top 10 Countries',
                                 template='plotly_dark', 
                                 barmode='group') 

# Show the chart 
pio.show(fig_state_tweet) 

### same for the likes
# Imposta il renderer per visualizzare i grafici direttamente
pio.renderers.default = "notebook"  # Usa "notebook" o "jupyterlab"

# Raggruppa il numero totale di 'likes' per ogni stato
likes_per_state = data.groupby('state_code')['likes'].sum().reset_index()

# Ordina i risultati per 'likes' in ordine decrescente
likes_per_state = likes_per_state.sort_values(by='likes', ascending=False)

# Crea un grafico a barre per il numero di 'likes' per ogni stato
fig_state_likes = px.bar(likes_per_state, x='state_code', y='likes', 
                          labels={'state_code': 'State Code', 'likes': 'Number of Likes'}, 
                          title='Total Likes by State', 
                          template='plotly_dark', 
                          barmode='group')

# Mostra il grafico
# fig_state_likes.show()