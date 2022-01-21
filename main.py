import pandas as pd
import matplotlib.pyplot as plt
pd.options.display.max_columns = None

years = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
durations = [103, 101, 99, 100, 100, 95, 95, 96, 93, 90]

# A dictionary with the two lists
movie_dict = {
    'years': years,
    'durations': durations
}
durations_df = pd.DataFrame(movie_dict)
print(durations_df)


def show_graph():
    fig = plt.figure()
    plt.plot(durations_df['years'], durations_df['durations'])
    plt.title('Netflix Movie Durations 2011-2020')
    plt.show()


netflix_df = pd.read_csv("/home/sergij/PycharmProjects/Investigating_Netflix_Movies_and_Guest_Stars_in_The_Office/datasets/netflix_data.csv")

# Subset the DataFrame for type "Movie"
netflix_df_movies_only = netflix_df[netflix_df['type'] == 'Movie']
# Select only the columns of interest
netflix_movies_col_subset = netflix_df_movies_only[['title', 'country', 'genre', 'release_year', 'duration']]


def show_scatter():
    fig = plt.figure(figsize=(12,8))
    plt.scatter(netflix_movies_col_subset['release_year'], netflix_movies_col_subset['duration'])
    plt.title("Movie Duration by Year of Release")
    plt.show()


short_movies = netflix_movies_col_subset[netflix_movies_col_subset['duration'] < 60]
print(short_movies.head(20))


colors = []
for index, row in netflix_movies_col_subset.iterrows():
    if row['genre'] == 'Children':
        colors.append('red')
    elif row['genre'] == 'Documentaries':
        colors.append('blue')
    elif row['genre'] == 'Stand-Up':
        colors.append('green')
    else:
        colors.append('black')

# Set the figure style and initalize a new figure
plt.style.use('fivethirtyeight')
fig = plt.figure(figsize=(12,8))

plt.scatter(netflix_movies_col_subset['release_year'], netflix_movies_col_subset['duration'], color=colors)
plt.title('Movie duration by year of release')
plt.xlabel('Release year')
plt.ylabel('Duration (min)')
plt.show()
