import pytest
from plug.registry import Registry

from plug_demo import error
from plug_demo.balance import BalanceModel
from plug_demo.balance import BalancePlugin
from plug_demo.balance import BalanceTransfer


@pytest.fixture
def state_slice_factory(registry, state_factory, state_slice_factory):
    def factory(transaction):
        state = state_factory(registry)
        return state_slice_factory(state, [transaction])
    return factory


async def test_balance_transfer(transaction_factory, state_slice_factory, alice, bob):
    """
    Transferring a balance between two accounts
    """
    transaction = transaction_factory(amount=20)
    state_slice = state_slice_factory(transaction)

    transaction.verify(state_slice)
    transaction.apply(state_slice)

    all_balances = state_slice[BalanceModel.fqdn]
    assert all_balances[bob.address].balance == 80
    assert all_balances[alice.address].balance == 120


def test_balance_plugin():
    """
    Setting up demo
    """
    registry = Registry().with_default()

    BalancePlugin.setup(registry)

    assert registry[BalanceTransfer.fqdn] == BalanceTransfer
    assert registry[BalanceModel.fqdn] == BalanceModel


async def test_balance_transfer_invalid_amount(transaction_factory, state_slice_factory, alice, bob):
    """
    Trying to transfer an invalid amount raises an error
    """
    transaction = transaction_factory(amount=-20)
    state_slice = state_slice_factory(transaction)

    with pytest.raises(error.InvalidAmountError) as exc:
        transaction.verify(state_slice)

    assert str(exc.value) == "Cannot send 0 or less"
    all_balances = state_slice[BalanceModel.fqdn]
    assert all_balances[bob.address].balance == 100
    assert all_balances[alice.address].balance == 100


async def test_balance_transfer_not_enough_money(transaction_factory, state_slice_factory, alice, bob):
    """
    Trying to transfer more than what we have raises an error
    """
    transaction = transaction_factory(amount=9999)
    state_slice = state_slice_factory(transaction)

    with pytest.raises(error.NotEnoughMoneyError) as exc:
        transaction.verify(state_slice)

    assert str(exc.value) == "Not enough money"
    all_balances = state_slice[BalanceModel.fqdn]
    assert all_balances[bob.address].balance == 100
    assert all_balances[alice.address].balance == 100
