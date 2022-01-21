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
print(netflix_movies_col_subset.head())
