from typing import List

from pydantic import BaseModel, Field

"""
    This file describes models for the cloudflare etherium block response:
    Block 
    {
        "jsonrpc": "2.0",
        "id": 64,
        "result": {
            "difficulty": "0x746ef15b66",
            "extraData": "0x476574682f76312e302e302f6c696e75782f676f312e342e32",
            "gasLimit": "0x1388",
            "gasUsed": "0x0",
            "hash": "0xd6bb42034740c5d728e774e43a01f26222e0fcc279c504ca5963dc34fe70f392",
            "logsBloom": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
            "miner": "0xf927a40c8b7f6e07c5af7fa2155b4864a4112b13",
            "mixHash": "0x975da446e302e6da6cedb3fbaa763c3c203ae88d6fab4924e2a3d34a568c4361",
            "nonce": "0x88a7f12f49151c83",
            "number": "0x2244",
            "parentHash": "0x067fd84ecdbc7491bf5ec7d5d4ead361b1f590eec74797a7f90b4a7d7004a48d",
            "receiptsRoot": "0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421",
            "sha3Uncles": "0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347",
            "size": "0x21b",
            "stateRoot": "0x828dade2067283e370993ec6a1bda0e65c1310e404a6d5bbb030b596eb80017c",
            "timestamp": "0x55bb040f",
            "totalDifficulty": "0x5c328da43525d",
            "transactions": [],
            "transactionsRoot": "0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421",
            "uncles": []
        }
    }

    Transaction:
    {
        "blockHash": "0x9fa4387b9a9e4de91f11f1cdf1c35eef4fe4d38e4548d581183743a2f6dee23a",
        "blockNumber": "0x200100",
        "gas": "0x15f90",
        "gasPrice": "0x4a817c800",
        "hash": "0x69d872683bf5310157c7e7a54deebae1e2acbfa302389b724712685d150ba984",
        "input": "0x",
        "nonce": "0x11c8e9",
        "to": "0xd8f5be01b66a5fbd858cd8d3f9d21d4c559d1335",
        "transactionIndex": "0x1",
        "value": "0xe1e44479118d000",
        "type": "0x0",
        "v": "0x1c",
        "r": "0x9e450f15def879405361ae5d026302746bd5a80e82df05118a0cf2a97ecdd573",
        "s": "0x3792af3dfc1b0ec62a369a92e5eeef05d0b6ed25af278ecc885dd2536aab1ebd"
    }
"""


class CFTransaction(BaseModel):
    blockHash: str
    blockNumber: str
    fr: str = Field(alias="from")
    gas: str
    gasPrice: str
    hash: str
    input: str
    nonce: str
    to: str
    transactionIndex: str
    value: str
    type: str
    v: str
    r: str
    s: str


class CFEtheriumBlock(BaseModel):
    difficulty: str
    extraData: str
    gasLimit: str
    gasUsed: str
    hash: str
    logsBloom: str
    miner: str
    mixHash: str
    nonce: str
    number: str
    parentHash: str
    receiptsRoot: str
    sha3Uncles: str
    size: str
    stateRoot: str
    timestamp: str
    totalDifficulty: str
    transactions: List[CFTransaction]
    transactionsRoot: str
    uncles: List[str]


class CFEtheriumBlockResponse(BaseModel):
    jsonrpc: str
    id: int
    result: CFEtheriumBlock


class CFRequest(BaseModel):
    """model for CloudFlare getBlockByNumber request"""

    jsonrpc: str = "2.0"
    method: str = "eth_getBlockByNumber"
    params: List
    id: int
