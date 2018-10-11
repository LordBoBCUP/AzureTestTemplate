from plug.indexer import PersistToFileMixin
from plug.indexer import RunnerIndexer


class AddressToTransactionIndexer(PersistToFileMixin, RunnerIndexer):

    fqdn = "plug_demo.indexer.AddressToTransactionIndexer"

    def update(self, transaction_hash, transaction):
        for address in transaction.proofs:
            if address not in self:
                self[address] = []
            self[address].append(transaction_hash)

    def remove(self, key, value=None):
        if value is None:
            del self[key]
        else:
            self[key].remove(value)
