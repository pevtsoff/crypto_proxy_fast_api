from pymemcache.client import base

from ..settings import settings

mc_client = base.Client((settings.memcached_host, settings.memcached_port))
