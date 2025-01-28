import redis
import logging


class RedisHandler(logging.Handler):
    def __init__(self, host, port, key):
        super().__init__()
        self.redis = redis.Redis(host=host, port=port)
        self.key = key

    def emit(self, record):
        self.redis.rpush(self.key, self.format(record))