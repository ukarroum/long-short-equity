import pandas as pd


def get_featuress(df_assets):
    """ Return a matrix of features
        each row represent an asset and each column represent a feature

        :param df_assets : Dataframe containing basic assets information (like closing price)
        :return X : features dataframe
    """


def get_assets_price_features(df_assets, nb_days=5):
    """ Return features related to asset price change

        :param df_assets : Dataframe containing basic assets information (like closing price)
        :param nb_days : Number days to use for sliding window
        :return X : features dataframe
    """

    X = df_assets.copy()

    # Prices mouvment on n days

    for i in range(1, nb_days + 1):
        X["price_change_" + str(i)] = (X.Last - X.Last.shift(i))/X.Last

    return X
