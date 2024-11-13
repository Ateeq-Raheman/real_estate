import frappe
from erpnext.erpnext.accounts.doctype.sales_invoice.sales_invoice import SalesInvoice
from pycoingecko import CoinGeckoAPI


class SalesInvoice(SalesInvoice):
    """
         Inherit core sales invoice and extend it.    
    """

    def get_crypto_prices(self):
        """
            cg = CoinGeckoAPI()
            Get grand_total in BTC , ETH
        """
        print("Hello, getting Crypto Prices")