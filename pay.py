"""pay.py."""
# python3 pay.py ssBiCoPZx6LZQH7w95M9HZF7t4Vg6 40 r2CSyAQoA2zPsHx6KPNSPAfBwRcX2eZPf # noqa 401

import os
import sys
import time

from xrpl.clients import WebsocketClient
from xrpl.ledger import get_latest_validated_ledger_sequence
from xrpl.utils import xrp_to_drops
from xrpl.models.transactions import Payment
from xrpl.account import get_next_valid_seq_number
from xrpl.wallet import Wallet
from xrpl.transaction import (
    send_reliable_submission,
    safe_sign_and_autofill_transaction,
    get_transaction_from_hash
)

w3 = WebsocketClient('wss://hooks-testnet.xrpl-labs.com')

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__)))

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print(
            "Usage: python3 pay.py <source family seed> \
            <amount xrp> <destination account>"
        )
        sys.exit()

    secret = sys.argv[1]
    wallet = Wallet(secret, 0)
    account = wallet.classic_address
    amount = int(sys.argv[2])
    dest = sys.argv[3]

    with w3 as client:
        print('CONNECTED')
        current_validated_ledger = get_latest_validated_ledger_sequence(w3)
        sequence = get_next_valid_seq_number(dest, w3)
        drop_value = xrp_to_drops(float(amount))
        built_transaction = Payment(
            account=account,
            amount=drop_value,
            destination=dest,
            # invoice_id=invoice_id,
        )

        # print(built_transaction)
        signed_tx = safe_sign_and_autofill_transaction(
            transaction=built_transaction,
            wallet=wallet,
            client=w3,
        )
        response = send_reliable_submission(signed_tx, w3)
        tx_result = response.result['meta']['TransactionResult']
        print(
            '{} The transaction was applied. \
            Only final in a validated ledger.'.format(tx_result)
        )

        for i in range(5):
            print('{} ...'.format(i))
            time.sleep(1)
        hook_tx = get_transaction_from_hash(response.result["hash"], w3)
        print('CLOSING...')
        client.close()
