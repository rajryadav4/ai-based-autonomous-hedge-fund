from kiteconnect import KiteConnect
from config import CONFIG

class TradingBot:
    def __init__(self):
        self.kite = KiteConnect(api_key=CONFIG["ZERODHA_API_KEY"])
        self.kite.set_access_token(CONFIG["ZERODHA_ACCESS_TOKEN"])
    
    def execute_order(self, symbol, transaction_type, quantity):
        return self.kite.place_order(
            variety=self.kite.VARIETY_REGULAR,
            exchange=self.kite.EXCHANGE_NSE,
            tradingsymbol=symbol,
            transaction_type=transaction_type,
            quantity=quantity,
            order_type=self.kite.ORDER_TYPE_MARKET,
            product=self.kite.PRODUCT_MIS
        )
