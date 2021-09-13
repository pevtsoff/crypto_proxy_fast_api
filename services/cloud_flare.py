import json

import requests
from fastapi import HTTPException

from crypto_proxy.loggers import logger

from ..models.cloud_flare import CFRequest
from ..settings import settings
from .memcache_api import mc_client


class BlockService:
    @classmethod
    def get_block_by_number(cls, block_number):
        if block_number == "latest":
            block_number = cls.get_latest_block_number()

        request_json = CFRequest(id=1, params=[block_number, True])
        logger.debug(request_json)

        return cls.make_cf_request(request_json)

    @classmethod
    def get_transaction_for_block(cls, block_number, tr_id):
        if block_number == "latest":
            block_number = cls.get_latest_block_number()

        request_json = CFRequest(id=1, params=[block_number, True])
        logger.debug(request_json)
        transactions = cls.make_cf_request(request_json)["result"].get("transactions", [])

        if tr_id.__class__ == int:
            return cls.get_transaction_by_id(transactions, tr_id)
        else:
            return cls.get_transaction_by_hash(transactions, tr_id)

    @classmethod
    def make_cf_request(cls, data):
        try:

            block_number = data.params[0]
            cache = mc_client.get(block_number)
            parsed_result = cls._get_cf_block_data(block_number, cache, data)

            return parsed_result

        except HTTPException as e:
            logger.exception(e)
            raise

        except KeyError as e:
            logger.exception(e)
            raise HTTPException(status_code=400, detail=f"Wrong json response arrived from CloudFlare: {e}") from e

        except Exception as e:
            logger.exception(e)
            raise HTTPException(
                status_code=400, detail=f"Error occured when trying to read block info from CloudFLare: {e}"
            ) from e

    @classmethod
    def get_transaction_by_hash(cls, trxs: list, hash: str):
        try:
            transaction = next(filter(lambda x: hash in x["hash"], trxs))

        except StopIteration as e:
            logger.exception(e)
            raise HTTPException(status_code=404, detail=f'Transaction "{hash}" does not exist in the block response')

        else:
            return transaction

    @classmethod
    def get_transaction_by_id(cls, trxs: list, index: int):
        try:
            return trxs[index]

        except IndexError as e:
            logger.exception(e)
            raise HTTPException(
                status_code=404, detail=f'Transaction with index "{index}" does not exist in the block response'
            )

    @classmethod
    def get_latest_block_number(cls, block_number="latest"):
        request = CFRequest(id=1, method="eth_blockNumber", params=[])
        logger.debug("requesting latest blocl number with params: '%s'", request)

        result = requests.post(
            url=settings.cf_url, headers={"Content-Type": "application/json"}, data=request.json()
        ).json()
        logger.debug("latest blocknumber response: %s", result["result"])

        return result["result"]

    @classmethod
    def _get_cf_block_data(cls, block_number, cache, data):
        if not cache:
            result = requests.post(url=settings.cf_url, headers={"Content-Type": "application/json"}, data=data.json())

            result.raise_for_status()
            logger.debug("doing a request to cache for block number %s", block_number)
            mc_client.set(block_number, result.text)
            logger.debug(result.text)

            result_text = result.text

        else:
            result_text = cache

        parsed_result = json.loads(result_text)

        if parsed_result.get("result") is None:
            raise HTTPException(status_code=404, detail=f"Block #{block_number}  not found")
        else:
            return parsed_result
