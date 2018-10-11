import plug.state
import plug.util
import pytest
from plug.key import ED25519SigningKey
from plug.model import NonceModel
from plug.proof import SingleKeyProof
from plug.registry import Registry
from plug.transaction import Transaction

from plug_demo.balance import BalanceModel
from plug_demo.balance import BalanceTransfer


class User:
    def __init__(self, signing_key, nonce=0):
        self.signing_key = signing_key
        self.nonce = nonce
        self.address = plug.util.plug_address(signing_key)


@pytest.fixture
def alice():
    return User(ED25519SigningKey.new())


@pytest.fixture
def bob():
    return User(ED25519SigningKey.new())


@pytest.fixture
def state_factory(bob, alice):
    def factory(registry):
        state_dict = {
            BalanceModel.fqdn: {
                bob.address: {"balance": 100},
                alice.address: {"balance": 100},
            },
            NonceModel.fqdn: {},
        }

        return plug.state.generate_initial_state(
            state_dict,
            plug.state.Namespace,
            registry,
        )
    return factory


@pytest.fixture
def registry():
    registry = Registry().with_default()
    registry.register(BalanceModel)
    registry.register(BalanceTransfer)
    return registry


@pytest.fixture
def state_slice_factory():
    def factory(state, transactions, block=None):
        return plug.util.prepare_state_slice(state, transactions, block=block)
    return factory


@pytest.fixture
def proof_factory():
    def factory(transform, user):
        challenge = transform.hash(plug.hash.sha256)
        proof = SingleKeyProof(user.address, user.nonce, challenge, network_id="demo.test")
        proof.sign(user.signing_key)
        return proof
    return factory


@pytest.fixture
def transaction_factory(proof_factory, alice, bob):
    def factory(amount):
        transform = BalanceTransfer(
            sender=bob.address,
            receiver=alice.address,
            amount=amount,
        )
        proof = proof_factory(transform, bob)
        return Transaction(transform, {proof.address: proof})
    return factory
