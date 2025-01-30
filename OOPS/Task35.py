# TASK 35: Create an abstract class 'PaymentMethos' with an abstract method 'ProcessPayment' and also two concrete classes 'CreditCardPayment' and 'PaypalPayment'.

from abc import ABC,abstractmethod
class PaymentMethod(ABC):
    
    @abstractmethod
    def ProcessPayment(self,amount):
        pass
        
class CreditCardPayment(PaymentMethod):
    def __init__(self,name):
        self.name=name
        
    def ProcessPayment(self,amount):
        self.amount=amount
        print(f"Processing payment of {self.amount} from {self.name}'s PayPal account.")
        
class PayPalPayment(PaymentMethod):
    def __init__(self,name):
        self.name=name
    
    def ProcessPayment(self,amount):
        self.amount=amount
        print(f"Processing payment of {self.amount} from {self.name}'s credit card.")
    
credit=CreditCardPayment("Anjana")
credit.ProcessPayment(10000)
paypal=PayPalPayment("Anjana")
paypal.ProcessPayment(10000)