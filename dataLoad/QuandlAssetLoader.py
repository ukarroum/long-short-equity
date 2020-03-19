""" load_data.py : A python Script the get the necessary data from Quandl """

import quandl

import config
from dataLoad.AssetLoader import AssetLoader


class QuandlAssetLoader(AssetLoader):
    def __init__(self):
        self.cac40_assets_names = ["AC", "AI", "ALU", "ALO", "MT",
                                   "CS", "BNP", "EN", "CAP", "CA",
                                   "ACA", "BN", "DEXB", "AIR", "EDF",
                                   "EI", "GSZ", "OR", "LG",
                                   "LR", "MMB", "MC", "ML", "RI",
                                   "UG", "RNO", "SGO", "SAN",
                                   "SU", "GLE", "STM", "TEC", "FP",
                                   "UL", "VK", "VIE", "DG", "VIV"]

    def get_asset(self, symbol):
        df = quandl.get(symbol, authtoken=config.API_KEY)

        return df

    def get_cac40_assets(self):
        return self.get_multiple_assets(["EURONEXT/" + symbol for symbol in self.cac40_assets_names])