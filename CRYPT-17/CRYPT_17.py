from mnemonic import Mnemonic
from web3 import Web3

mnemo = Mnemonic("english")
words = mnemo.generate(strength=256)
seed = mnemo.to_seed(words, passphrase="")

MAIN_NET_HTTP_ENDPOINT = "<add your mainnet endpoint URL here>"
w3 = Web3(Web3.HTTPProvider(MAIN_NET_HTTP_ENDPOINT))

account = w3.eth.account.privateKeyToAccount(seed[:32])

private_key = account.pricateKey
Public_key = account.address





