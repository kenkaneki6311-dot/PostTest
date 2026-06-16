from abc import ABC, abstractmethod

class payment(ABC):
    @abstractmethod
    def pay(self):
        pass

    @abstractmethod
    def receipt(self):
        pass

class Gpay:
    def pay(self):
        print(f"balance is deducted!")

    def receipt(self):
        print(f"balance is credited")

class Credit_card:
    def pay(self):
        print(f"Credit_card amount is deducted!")

    def receipt(self):
        print(f"Credit_card amount is credited!")

gpay = Gpay()
gpay.pay()
gpay.receipt()

credits = Credit_card()
credits.pay()
credits.receipt()