from .strategy import GoldStrategy

class OneOzGoldBot:
    def __init__(self, config, logger=None):
        self.config = config
        self.logger = logger
        self.strategy = GoldStrategy()
        self.contract = config["symbol"]

    def on_market_data(self, tick):
        signal = self.strategy.generate_signal(tick)
        if self.logger and signal:
            self.logger.info(f"Contract: {self.contract} | Signal: {signal}")
        return signal

    def on_heartbeat(self):
        # later: health checks, PnL snapshots, etc.
        pass
