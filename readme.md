# Overview
This simple solution is a demo of the caching proxy server for the Cloud Flare API 
for gettings Etherium blocks by number. It uses Memcached as a prodaction ready LRU cache container. 

# Install Locally
```angular2html
poetry run install
```

# Start
1. Clone repo
2. Run
```angular2html
./deploy_local build
./deploy_local up
```

# Usage
1.Get block by number:
```
curl localhost:8000/cf_proxy/block/0x200100

{"jsonrpc":"2.0","id":1,"result":{"difficulty":"0x3a52bfb78228","extraData":"0x7777772e62772e636f6d","gasLimit":"0x47e7bb","gasUsed":"0x157c7b","hash":"0x9fa4387b9a9e4de91f11f1cdf1c35eef4fe4d38e4548d581183743a2f6dee23a","logsBloom":"0x00000000000000000000000000000040000000000008000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000800000000000000000000000000000000000002000000000000010000000000000000010000000000000000000000000010000000000001000000001000004000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000400000000000000000000000000000000000000000000000000000000000000000010000000000008000000000000000000002000000000000000000000000000000000000000000000000","miner":"0xbcdfc35b86bedf72f0cda046a3c16829a2ef41d1","mixHash":"0x532afe7bd8356e2535ad94e5fa0c7ec19d2ddd32743f5d1a1866ad1d3bf337c7","nonce":"0x20d6ee6aaae8684b","number":"0x200100","parentHash":"0xefcc465cfc0da8ede3a6c04bc745821a4e51bae38018f79b5560bab124759e25","receiptsRoot":"0xea31c790190ab6e003d4d596c00ed71c7ff68cfadc2ea2405a6a69ba6f298c2f","sha3Uncles":"0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347","size":"0x449","stateRoot":"0x641ab19d17ef1a9decd3a1d2a92bc25665cc5bccf515672c579b525463c1a2ea","timestamp":"0x57b64432","totalDifficulty":"0x2afdab622997c6aad","transactions":[{"blockHash":"0x9fa4387b9a9e4de91f11f1cdf1c35eef4fe4d38e4548d581183743a2f6dee23a","blockNumber":"0x200100","from":"0xea674fdde714fd979de3edf0f56aa9716b898ec8","gas":"0x15f90","gasPrice":"0x4a817c800","hash":"0xcdd27f81861499544068fb317fdb67c8ae574cda90669f3caeff857f825812b4","input":"0x","nonce":"0x66eb2","to":"0x3345ba1634ba3ec5c530362f2806b312f7f11e28","transactionIndex":"0x0","value":"0xdecf1ee9fdf350c","type":"0x0","v":"0x1b","r":"0x6e169e5e8958e2a8de02972b32755b49f1ff8c5c532ae8dc3088384530f805e2","s":"0x5cba3c5555670dc9b75357bb660ce69c8b4b89713ae3828421a72792f95d0811"},{"blockHash":"0x9fa4387b9a9e4de91f11f1cdf1c35eef4fe4d38e4548d581183743a2f6dee23a","blockNumber":"0x200100","from":"0x2a65aca4d5fc5b5c859090a6c34d164135398226","gas":"0x15f90","gasPrice":"0x4a817c800","hash":"0x69d872683bf5310157c7e7a54deebae1e2acbfa302389b724712685d150ba984","input":"0x","nonce":"0x11c8e9","to":"0xd8f5be01b66a5fbd858cd8d3f9d21d4c559d1335","transactionIndex":"0x1","value":"0xe1e44479118d000","type":"0x0","v":"0x1c","r":"0x9e450f15def879405361ae5d026302746bd5a80e82df05118a0cf2a97ecdd573","s":"0x3792af3dfc1b0ec62a369a92e5eeef05d0b6ed25af278ecc885dd2536aab1ebd"},{"blockHash":"0x9fa4387b9a9e4de91f11f1cdf1c35eef4fe4d38e4548d581183743a2f6dee23a","blockNumber":"0x200100","from":"0xea674fdde714fd979de3edf0f56aa9716b898ec8","gas":"0x15f90","gasPrice":"0x4a817c800","hash":"0x622d25e7495a167ca6b9d55581a6be40c75d6958f8ea3c19948261e077a12359","input":"0x","nonce":"0x66eb3","to":"0x58e9c068c3a92801b0c1fe16a21c882aaf33403b","transactionIndex":"0x2","value":"0xde113e7cce5fc5c","type":"0x0","v":"0x1c","r":"0xcc736235a6a4871c40b7c5c2061446dcb2109d772ce448bdfd4a78b6eb277f7","s":"0x7bf0f517c55069195cfa9ffb5ef301ffb521199aef6681d6a46c64b84898960c"},{"blockHash":"0x9fa4387b9a9e4de91f11f1cdf1c35eef4fe4d38e4548d581183743a2f6dee23a","blockNumber":"0x200100","from":"0x2a65aca4d5fc5b5c859090a6c34d164135398226","gas":"0x15f90","gasPrice":"0x4a817c800","hash":"0x89eeded251fc46aa36488a20195f256fff48837b52367e1afb3f1d184eda10dc","input":"0x","nonce":"0x11c8ea","to":"0xc963534aa8fe98bc6c3ee4ca3fd01fc9b1cb90a3","transactionIndex":"0x3","value":"0xe1ae698d47f5400","type":"0x0","v":"0x1b","r":"0xbcbe57d671593d58957f955ddea9a3c162bdbe97b85d9646819b58b6c28a44e4","s":"0x5432a0c2875663b656295b8e11a5f3c8df80b51e58b1cefe539149efc6485a92"},{"blockHash":"0x9fa4387b9a9e4de91f11f1cdf1c35eef4fe4d38e4548d581183743a2f6dee23a","blockNumber":"0x200100","from":"0x61727f495f6bcaa392abbfde17cc7fb88ee45934","gas":"0x200b20","gasPrice":"0x4a817c800","hash":"0xbc9044a4a018315a3aed7b66c99f8c4b6fcc6569d7edfd4c40947e471cfa424b","input":"0x61461954","nonce":"0x9e4","to":"0x098c3da29fad5375da9bf983e07ab5732ddfc396","transactionIndex":"0x4","value":"0x0","type":"0x0","v":"0x1c","r":"0xff24f4cae93b10bed2fab7fad10a91b070e4c3a837ca6fa4e385ae128ff644e9","s":"0x423c05b02cb3a10d90c6373f74b3ee3fa7acd61483f5de90df61d2092fafa3ba"}],"transactionsRoot":"0x3a4933a4963fdf8d39e5ccb49269d963b9986e2aa939f590126f04603cf87278","uncles":[]}}
```

2.Get Transaction by index
```angular2html
curl localhost:8000/cf_proxy/block/0x200100/txs/1

{"blockHash":"0x9fa4387b9a9e4de91f11f1cdf1c35eef4fe4d38e4548d581183743a2f6dee23a","blockNumber":"0x200100","from":"0x2a65aca4d5fc5b5c859090a6c34d164135398226","gas":"0x15f90","gasPrice":"0x4a817c800","hash":"0x69d872683bf5310157c7e7a54deebae1e2acbfa302389b724712685d150ba984","input":"0x","nonce":"0x11c8e9","to":"0xd8f5be01b66a5fbd858cd8d3f9d21d4c559d1335","transactionIndex":"0x1","value":"0xe1e44479118d000","type":"0x0","v":"0x1c","r":"0x9e450f15def879405361ae5d026302746bd5a80e82df05118a0cf2a97ecdd573","s":"0x3792af3dfc1b0ec62a369a92e5eeef05d0b6ed25af278ecc885dd2536aab1ebd"}
```

3.Get Transaction by hash
```angular2html
curl localhost:8000/cf_proxy/block/0x200100/txs/0x69d87

{"blockHash":"0x9fa4387b9a9e4de91f11f1cdf1c35eef4fe4d38e4548d581183743a2f6dee23a","blockNumber":"0x200100","from":"0x2a65aca4d5fc5b5c859090a6c34d164135398226","gas":"0x15f90","gasPrice":"0x4a817c800","hash":"0x69d872683bf5310157c7e7a54deebae1e2acbfa302389b724712685d150ba984","input":"0x","nonce":"0x11c8e9","to":"0xd8f5be01b66a5fbd858cd8d3f9d21d4c559d1335","transactionIndex":"0x1","value":"0xe1e44479118d000","type":"0x0","v":"0x1c","r":"0x9e450f15def879405361ae5d026302746bd5a80e82df05118a0cf2a97ecdd573","s":"0x3792af3dfc1b0ec62a369a92e5eeef05d0b6ed25af278ecc885dd2536aab1ebd"}
```

Original Test Assignment
https://gist.github.com/mandrigin/9e46e8f8df3c9feb0b8bd12e7bbd9d7a