from brownie import SimpleStorage
from scripts.helpful_scripts import get_account


def test_deploy():
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 0
    assert starting_value == expected


def test_store():
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})
    expected = 15
    transaction = simple_storage.store(expected, {"from": account})
    transaction.wait(1)
    final_value = simple_storage.retrieve()
    assert final_value == expected
