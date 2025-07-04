from abc import ABC, abstractmethod


class PaymentGateway(ABC):
    @abstractmethod
    def processPayment(self, amount):
        pass


class Invoice(ABC):
    @abstractmethod
    def generateInvoice(self):
        pass


class PayUGateway(PaymentGateway):
    def processPayment(self, amount):
        print(f"Paying {amount} With PayUGateway")


class RazorPayGateway(PaymentGateway):
    def processPayment(self, amount):
        print(f"Paying {amount} With RazorPayGateway")


class PayPalGateway(PaymentGateway):
    def processPayment(self, amount):
        print(f"Paying {amount} With PayPalGateway")


class StripeGateway(PaymentGateway):
    def processPayment(self, amount):
        print(f"Paying {amount} With StripeGateway")


class GSTInvoice(Invoice):
    def generateInvoice(self):
        print("Generating GST Invoice")


class USInvoice(Invoice):
    def generateInvoice(self):
        print("Generating US Invoice")


class RegionFactory(ABC):
    @abstractmethod
    def create_gateway(self, name):
        pass

    def create_invoice(self):
        pass


class IndiaFactory(RegionFactory):
    def create_gateway(self, name):
        if name == "RazorPay":
            return RazorPayGateway()
        elif name == "PayU":
            return PayUGateway()
        raise "Invalid Gateway For India"

    def create_invoice(self):
        return GSTInvoice()


class USFactory(RegionFactory):
    def create_gateway(self, name):
        if name == "PayPal":
            return PayPalGateway()
        elif name == "Stripe":
            return StripeGateway()
        raise "Invalid Gateway For US"

    def create_invoice(self):
        return USInvoice()


class CheckoutService:
    def __init__(self, factory, gateway_name):
        self.factory = factory.create_gateway(gateway_name)
        self.invoice = factory.create_invoice()

    def complete_order(self, amount):
        self.factory.processPayment(amount)
        self.invoice.generateInvoice()


if __name__ == "__main__":
    india_payment = CheckoutService(IndiaFactory(), "RazorPay")
    india_payment.complete_order(100)

    us_payment = CheckoutService(USFactory(), "PayPal")
    us_payment.complete_order(300)
