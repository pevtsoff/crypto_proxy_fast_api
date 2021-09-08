from pydantic import BaseSettings


class Settings(BaseSettings):
    server_host: str = "0.0.0.0"
    server_port: int = 8000
    log_level: str = "DEBUG"
    cf_url = "https://cloudflare-eth.com"
    memcached_host: str = "memcached"
    memcached_port: int = 11211


settings = Settings(_env_file="/app/.env", _env_file_encoding="UTF-8")
