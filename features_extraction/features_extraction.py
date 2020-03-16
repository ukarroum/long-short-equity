import pandas as pd


def get_featuress(df_assets):
    """ Return a matrix of features
        each row represent an asset and each column represent a feature

        :param df_assets : Dataframe containing basic assets information (like closing price)
        :return X : features dataframe
    """


def get_assets_price_features(df_assets, nb_days_window=5):
    """ Return features related to asset price change

        :param df_assets : Dataframe containing basic assets information (like closing price)
        :param nb_days_window : Number days to use for sliding window
        :return X : features dataframe
    """

    X = df_assets.copy()

    # Prices mouvement on n days

    for i in range(1, nb_days_window + 1):
        X["price_change_" + str(i)] = (X.Last - X.Last.shift(i))/X.Last

    return X.dropna()


def get_assets_rankings(X, nb_days_end_period=None, end_period=None, nb_long=5, nb_short=5):
    """ Rank the assets based on their future performance at end_period or after nb_end_period
    (starting from the first date). Please note that you can't specify both arguments

        :param X : the input Dataset, this is pandas dataframe.
        :param nb_days_end_period : Number of days (from the first date) to end of the hedging period
        :param end_period : the date of the end of hedging period.
        :param nb_long : The number of assets to long (the best ones)
        :param nb_short : The number of assets to short (the worst one), note that nb_long mayb be different

        :return Y : the label vector, i use the following convention :
                        1 - asset to long
                        -1 - asset to short
                        0 - middle of the table

        """
