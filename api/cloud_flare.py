from typing import Union

from fastapi import APIRouter

from ..models.cloud_flare import CFEtheriumBlockResponse, CFTransaction
from ..services.cloud_flare import BlockService

router = APIRouter(prefix="/cf_proxy", tags=["proxy"])


# localhost:8000/cf_proxy/block/0x200100
# localhost:8000/cf_proxy/block/0x20013
@router.get("/block/{block_number}", response_model=CFEtheriumBlockResponse)
def get_block(block_number: str = "latest"):
    return BlockService.get_block_by_number(block_number)


# localhost:8000/cf_proxy/block/0x200100/txs/1
@router.get("/block/{block_number}/txs/{tx_id}", response_model=CFTransaction)
def get_transaction(block_number: str = "latest", tx_id: Union[int, str] = None):
    return BlockService.get_transaction_for_block(block_number, tx_id)
