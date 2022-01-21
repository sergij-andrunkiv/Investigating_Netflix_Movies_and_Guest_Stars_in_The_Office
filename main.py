import pandas

years = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
durations = [103, 101, 99, 100, 100, 95, 95, 96, 93, 90]

# A dictionary with the two lists
movie_dict = {
    'years': years,
    'durations': durations
}

durations_df = pandas.DataFrame(movie_dict)
