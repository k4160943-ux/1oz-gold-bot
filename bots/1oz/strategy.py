class GoldStrategy:
    def __init__(self):
        self.last_price = None

    def generate_signal(self, tick):
        price = tick.get("price")

        if self.last_price is None:
            self.last_price = price
            return None

        # placeholder logic
        if price > self.last_price:
            signal = "BUY"
        elif price < self.last_price:
            signal = "SELL"
        else:
            signal = None

        self.last_price = price
        return signal
