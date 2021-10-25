"""new-acc.py."""
from xrpl.clients import JsonRpcClient
from xrpl.core import keypairs
seed = keypairs.generate_seed()
public, private = keypairs.derive_keypair(seed)
test_account = keypairs.derive_classic_address(public)
print({'publicKey': test_account, 'seed': seed})
print('ADDRESS: {}'.format(test_account))
print('PUBLIC: {}'.format(public))
print('PRIVATE: {}'.format(private))
print('SEED: {}'.format(seed))
