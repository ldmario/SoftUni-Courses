class Account:
    def __init__(self, id: int, balance: int, pin: int):
        self.id = id
        self.balance = balance
        self.pin = pin

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def pin(self):
        return self.__pin
    
    @pin.setter
    def pin(self, value):
        self.__pin = value

    def get_id(self, pin: int):
        if pin == self.__pin:
            return self.__id
        return "Wrong pin"

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.__pin:
            self.pin = new_pin
            return "Pin changed"
        return "Wrong pin"
