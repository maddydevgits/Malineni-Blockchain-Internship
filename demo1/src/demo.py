from web3 import Web3,HTTPProvider
import json

blockchain='http://127.0.0.1:8545'

web3=Web3(HTTPProvider(blockchain))
web3.eth.defaultAccount=web3.eth.accounts[0]

artifact_path="../build/contracts/demo.json"
caddr='0x924863f7F8522ed7Fe82622507ae1C195DBB90d7'

with open (artifact_path) as f:
    contract_json=json.load(f)
    contract_abi=contract_json['abi']

contract=web3.eth.contract(address=caddr,abi=contract_abi)
m=contract.functions.hello().call()
print(m)

