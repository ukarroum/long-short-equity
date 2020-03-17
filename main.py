from DataLoad.QuandlAssetLoader import QuandlAssetLoader
from features_extraction import features_extraction

loader = QuandlAssetLoader()

X = loader.get_asset("EURONEXT/BNP")

X = features_extraction.get_assets_price_features(X)

y = features_extraction.get_return_to_volatility(X, 5)
print(X)
