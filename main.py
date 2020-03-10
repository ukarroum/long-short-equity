from DataLoad.QuandlAssetLoader import QuandlAssetLoader
from features_extraction import features_extraction

loader = QuandlAssetLoader()

X = loader.get_asset("EURONEXT/BNP")

X = features_extraction.get_assets_price_features(X)
print(X)
