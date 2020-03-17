def remove_incomplete_dates(X):
    """
    This function removes all incomplete dates
    An incomplete date is basicaly any date for which we have a missing value for at least one asset

    :param X : the dataset, a dictionarry """