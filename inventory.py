from abc import ABC, abstractmethod


class InventoryServices(ABC):  # abstract --> this class is going to hold only -- abstract methods--> methods without body -> just

    @abstractmethod
    def add_product(self):
        pass

    @abstractmethod
    def delete_product(self):
        pass

    @abstractmethod
    def search_product(self):
        pass

    @abstractmethod
    def update_product(self):
        pass

    @abstractmethod
    def product_in_price_range(self):
        pass
    @abstractmethod
    def maxPriceProd(self):
        pass

    @abstractmethod
    def minPriceProd(self):
        pass

    @abstractmethod
    def discounted_price(self):
        pass

    @abstractmethod
    def list_product(self):
        pass