from .strategy import GoldStrategy
from .roll_logic import get_active_contract

class OneOzGoldBot:
    def __init__(self, config):
        self.config = config
        self.strategy = GoldStrategy()
        self.contract = get_active_contract()

    def on_market_data(self, tick):
        signal = self.strategy.generate_signal(tick)
        return signal

    def on_heartbeat(self):
        # health checks, roll checks, etc.
        pass
