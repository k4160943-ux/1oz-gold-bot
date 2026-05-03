from datetime import datetime
from core.engine import Engine
from core.config_loader import load_config
from core.logger import create_logger
from bots.oz1.bot_1oz import OneOzGoldBot

def fake_tick_stream():
    price = 2400.0
    while True:
        yield {
            "timestamp": datetime.utcnow(),
            "price": price,
            "volume": 1
        }
        price += 0.5

def main():
    config = load_config("config/1oz.yaml")
    logger = create_logger("1oz")

    bot = OneOzGoldBot(config, logger=logger)
    engine = Engine(bot, logger, heartbeat_interval=1.0)

    engine.run(fake_tick_stream())

if __name__ == "__main__":
    main()
