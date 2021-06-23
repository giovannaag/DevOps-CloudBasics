import unittest
import movies_analysis


class TestsMoviesAnalysis(unittest.TestCase):

    def test_select_movies(self):
        movies_dataframe = movies_analysis.select_movies()
        self.assertFalse(movies_dataframe.empty)

    def test_select_cast(self):
        movies_dataframe = movies_analysis.select_movies()
        cast_movie_dataframe = movies_analysis.select_cast(movies_dataframe)
        self.assertFalse(cast_movie_dataframe.empty)

    def test_top10_actors(self):
        top10_actors = movies_analysis.top10_actors()
        self.assertEqual(len(top10_actors), 10)


