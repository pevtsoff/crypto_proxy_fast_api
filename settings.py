import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    server_host: str = os.getenv("HOST", "0.0.0.0")
    server_port: int = os.getenv("PORT", 8000)
    log_level: str = os.getenv("LOG_LEVEL", "DEBUG")
    cf_url = os.getenv("CLOUD_FLARE_URL", "https://cloudflare-eth.com")
    memcached_host: str = os.getenv("MEMCACHED_HOST", "memcached")
    memcached_port: int = os.getenv("MEMCACHED_PORT", 11211)


settings = Settings()
