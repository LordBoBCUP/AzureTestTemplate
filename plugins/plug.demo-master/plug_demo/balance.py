from dataclasses import dataclass
from plug.abstract import Model
from plug.abstract import Plugin
from plug.abstract import Transform

from plug_demo import error


@dataclass
class BalanceModel(Model):
    fqdn = "plug_demo.balance.BalanceModel"
    balance: int = 100000

    @classmethod
    def default_factory(cls):
        return cls()

    @staticmethod
    def pack(registry, obj):
        return {
            "balance": obj.balance,
        }

    @classmethod
    def unpack(cls, injector, payload):
        return cls(payload["balance"])


@dataclass
class BalanceTransfer(Transform):
    fqdn = "plug_demo.balance.BalanceTransfer"
    sender: str
    receiver: str
    amount: int

    def required_authorizations(self):
        return {self.sender}

    def required_keys(self):
        return {self.sender, self.receiver}

    @staticmethod
    def required_models():
        return {BalanceModel.fqdn}

    def verify(self, state):
        balances = state[BalanceModel.fqdn]

        if self.amount <= 0:
            raise error.InvalidAmountError("Cannot send 0 or less")

        if balances[self.sender].balance < self.amount:
            raise error.NotEnoughMoneyError("Not enough money")

    def apply(self, state):
        balances = state[BalanceModel.fqdn]
        balances[self.sender].balance -= self.amount
        balances[self.receiver].balance += self.amount

    @staticmethod
    def pack(registry, obj):
        return {
            "sender": obj.sender,
            "receiver": obj.receiver,
            "amount": obj.amount,
        }

    @classmethod
    def unpack(cls, injector, payload):
        return cls(
            sender=payload["sender"],
            receiver=payload["receiver"],
            amount=payload["amount"],
        )


class BalancePlugin(Plugin):
    @classmethod
    def setup(cls, registry):
        registry.register(BalanceModel)
        registry.register(BalanceTransfer)
