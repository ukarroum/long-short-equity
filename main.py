from dataLoad.QuandlAssetLoader import QuandlAssetLoader
from features_extraction import features_extraction

loader = QuandlAssetLoader()

X = loader.get_asset("EURONEXT/BNP")

X, y = features_extraction.get_featuress(X, 5)

print(X)
