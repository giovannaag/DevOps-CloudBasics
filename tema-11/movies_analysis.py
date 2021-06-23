import pandas as pd
import datetime

last10years = datetime.datetime.now().year - 10


def select_movies():
    movies_dataframe = pd.read_csv('datasets/title.basics/data.tsv', sep='\t',
                                   usecols=['tconst', 'titleType', 'startYear'], dtype='unicode')

    movies_dataframe['startYear'] = pd.to_numeric(movies_dataframe['startYear'], errors='coerce')

    movies_dataframe = movies_dataframe[(movies_dataframe['titleType'] == 'movie') &
                                        (movies_dataframe['startYear'] >= last10years)]

    return movies_dataframe


def select_cast(movies_dataframe):
    cast_dataframe = pd.read_csv('datasets/title.principals/data.tsv', sep='\t',
                                 usecols=['tconst', 'nconst', 'category'], dtype='unicode')

    cast_dataframe = cast_dataframe[(cast_dataframe['category'] == 'actress') |
                                    (cast_dataframe['category'] == 'actor')]

    cast_movie_dataframe = pd.merge(movies_dataframe, cast_dataframe, how='inner', on=['tconst'])

    return cast_movie_dataframe


def top10_actors():
    movies_dataframe = select_movies()
    cast_dataframe = select_cast(movies_dataframe)

    names_dataframe = pd.read_csv('datasets/name.basics/data.tsv', sep='\t',
                                  usecols=['nconst', 'primaryName'], dtype='unicode')

    top10_actors_dataframe = pd.DataFrame(cast_dataframe['nconst'].value_counts().index[0:10], columns=['nconst'])

    top10_actors = pd.merge(names_dataframe, top10_actors_dataframe, how='inner', on=['nconst'])

    return top10_actors['primaryName'].to_list()