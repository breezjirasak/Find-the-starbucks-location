import pandas as pd


class Data:
    def __init__(self, dataframe):
        """ to create dataframe

        :param dataframe: Dataframe
        """
        self.df = pd.read_csv(dataframe)

        # replace the NaN with No postcode
        self.df['Postcode'] = self.df['Postcode'].fillna('No postcode')

    def get_column(self, dataframe, column):
        """ to duplicated column that you need

        :param dataframe: Dataframe
        :param column: Column
        :return: list of column that you need
        """

        df = dataframe
        country = df[column].duplicated(keep='first')
        df = df[~country]
        return list(df.sort_values(column)[column])

    def filter(self, v1, v2, dataframe):
        """ To filter value

        :param v1: Column
        :param v2: Value that you want to filter
        :param dataframe: Dataframe
        :return: Dataframe
        """
        new = dataframe[dataframe[v1] == v2]
        return new

    def get_avg(self, dataframe, column):
        """ To compute average of column that you need

        :param dataframe: Dataframe
        :param column: Column
        :return: Average as float
        """
        return dataframe[column].mean()
