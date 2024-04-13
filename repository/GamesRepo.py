import json

from components.fast_api import GetGamesFilters
from components.spark_client import spark


class GamesRepo:
    @staticmethod
    def generate_filters(filters: GetGamesFilters):
        filter_claueses = []
        for dev in filters.devs:
            filter_claueses.append(f'Team ILIKE "%{dev}%"')
        for genre in filters.genres:
            filter_claueses.append(f'Genres ILIKE "%{genre}%"')
        if filters.rating != None:
            filter_claueses.append(f'Rating > "{filters.rating}"')
        if years := filters.years:
            if years.start:
                filter_claueses.append(f'Release_Date > "{years.start}"')
            if years.end:
                filter_claueses.append(f'Release_Date < "{years.end}"')
        if len(filter_claueses) > 0:
            return ' WHERE ' + ' AND '.join(filter_claueses)
        return ''

    @staticmethod
    def df_to_json(df):
        df = df.toPandas()
        return json.loads(df.drop('_c0', axis=1).to_json(orient='records'))

    @classmethod
    def get_games(cls, filters):
        query = "SELECT * FROM games"
        query += cls.generate_filters(filters)
        return cls.df_to_json(spark.sql(query))

    @classmethod
    def update_game(cls, title, update_data):
        query = " UPDATE games SET "
        set_clauses = []
        for key, value in update_data.items():
            set_clauses.append(f'{key} = "{value}"')
        query += ', '.join(set_clauses)
        query += f' WHERE title == "{title}"'
        spark.sql(query)

    @classmethod
    def get_recommendations(cls, user, filters):
        query = "SELECT * FROM games"
        for genre in user.genres:
            if genre not in filters.genres:
                filters.genres.append(genre.name)
        query += cls.generate_filters(filters)
        query += ' ORDER BY Rating DESC LIMIT 10'
        return cls.df_to_json(spark.sql(query))

