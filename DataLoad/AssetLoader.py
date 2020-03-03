""" AssetLoader.py : A python Script the get the necessary assets data """

from abc import ABC, abstractmethod


class AssetLoader(ABC):
    @abstractmethod
    def get_asset(self, symbol):
        pass

    def get_multiple_assets(self, symbols):
        return {symbol: self.get_asset(symbol) for symbol in symbols}
