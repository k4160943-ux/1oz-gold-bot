import time
import traceback

class Engine:
    def __init__(self, bot, logger, heartbeat_interval=1.0):
        self.bot = bot
        self.logger = logger
        self.heartbeat_interval = heartbeat_interval
        self.running = False

    def process_tick(self, tick):
        try:
            signal = self.bot.on_market_data(tick)
            if signal:
                self.logger.info(f"Signal: {signal} | Tick: {tick}")
                # later: route to execution layer
        except Exception as e:
            self.logger.error(f"Error in process_tick: {e}")
            self.logger.debug(traceback.format_exc())

    def heartbeat(self):
        try:
            self.bot.on_heartbeat()
        except Exception as e:
            self.logger.error(f"Error in heartbeat: {e}")
            self.logger.debug(traceback.format_exc())

    def run(self, tick_stream):
        """
        tick_stream: iterable/generator yielding dicts:
            {
                "timestamp": datetime,
                "price": float,
                "volume": float
            }
        """
        self.logger.info("Engine started")
        self.running = True

        for tick in tick_stream:
            if not self.running:
                break

            self.process_tick(tick)
            self.heartbeat()
            time.sleep(self.heartbeat_interval)

        self.logger.info("Engine stopped")

    def stop(self):
        self.running = False
