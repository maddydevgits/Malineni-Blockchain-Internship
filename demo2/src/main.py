from web3 import Web3,HTTPProvider 

import json # for loading abi through json 

blockchain='http://127.0.0.1:8545'

web3=Web3(HTTPProvider(blockchain))

web3.eth.defaultAccount=web3.eth.accounts[0]

caddr='0x44de7ffD520fEA099Ab2622Cba88C53388EfF9A5'

with open('../build/contracts/demo2.json') as f:
    contract_json=json.load(f)
    contract_abi=contract_json['abi']

contract=web3.eth.contract(address=caddr,abi=contract_abi)
k=input('enter a message to store')
tx_hash=contract.functions.insertmessage(k).transact()
web3.eth.waitForTransactionReceipt(tx_hash)

m=contract.functions.viewmessage().call()
print(m)

print(tx_hash)