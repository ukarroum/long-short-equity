import pandas as pd


def get_featuress(df_assets, nb_days_window=5):
    """ Return a matrix of features
        each row represent an asset and each column represent a feature

        :param df_assets : Dataframe containing basic assets information (like closing price)
        :param nb_days_window : int Number days to use for sliding window
        :return X : features dataframe
    """

    X = get_assets_price_features(df_assets, nb_days_window)

    y = get_return_to_volatility(X, nb_days_window)

    return X, y


def get_assets_price_features(df_assets, nb_days_window):
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


def get_return_to_volatility(X, nb_days_end_period):
    """ Rank the assets based on their future performance at after nb_end_period.

        :param X : the input Dataset, this is pandas dataframe.
        :param nb_days_end_period : Number of days to the end of the hedging period, please note thet
                                    the days in question are business days which mean friday + 2 = tuesday and not sunday

        :return Y : A vector of returns to volatility for each asset after nb_days_end_period days

        """
    
    y = ((X.Last.shift(-nb_days_end_period) - X.Last)/X.Last ) / X.price_change_1.rolling(nb_days_end_period).std(ddof=0).shift(-nb_days_end_period)

    return y.dropna()
