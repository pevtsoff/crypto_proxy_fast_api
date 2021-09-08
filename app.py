from fastapi import FastAPI

from crypto_proxy.api import router

app = FastAPI(
    title="Cloudflare ETH Proxy Server",
    description="Cloudflare proxy server for the ETH API with LRU cache",
    version="1.0.0.",
)
app.include_router(router)
