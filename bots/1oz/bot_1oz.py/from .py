from .strategy import GoldStrategy
from .roll_logic import get_active_contract

class OneOzGoldBot:
    def __init__(self, config, logger=None):
        self.config = config
        self.logger = logger
        self.strategy = GoldStrategy()
        self.contract = get_active_contract()

    def on_market_data(self, tick):
        signal = self.strategy.generate_signal(tick)
        if self.logger and signal:
            self.logger.info(f"Contract: {self.contract} | Signal: {signal}")
        return signal

    def on_heartbeat(self):
        # later: roll checks, health checks, PnL snapshots, etc.
        pass
