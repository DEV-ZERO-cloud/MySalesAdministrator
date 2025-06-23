class StockRegister:
    def __init__(self, id: int, date: str, id_store_start: str, id_store_end: str, id_product: str, quantity: int):
        self._id = id
        self._date = date
        self._id_store_start = id_store_start
        self._id_store_end = id_store_end
        self._id_product = id_product
        self._quantity = quantity

    # Getter and Setter for id
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    # Getter and Setter for date
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value

    # Getter and Setter for id_store_start
    @property
    def id_store_start(self):
        return self._id_store_start

    @id_store_start.setter
    def id_store_start(self, value):
        self._id_store_start = value

    # Getter and Setter for id_store_end
    @property
    def id_store_end(self):
        return self._id_store_end

    @id_store_end.setter
    def id_store_end(self, value):
        self._id_store_end = value

    # Getter and Setter for id_product
    @property
    def id_product(self):
        return self._id_product

    @id_product.setter
    def id_product(self, value):
        self._id_product = value

    # Getter and Setter for quantity
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value