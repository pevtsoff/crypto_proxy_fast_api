__package__ = "crypto_proxy"
import uvicorn

from .settings import settings

uvicorn.run(
    "crypto_proxy.app:app",
    host=settings.server_host,
    port=settings.server_port,
    reload=True,
)
