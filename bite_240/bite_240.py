""" 
Bite 240. Write tests for an Account class
"""
from account import Account
import pytest

# write your pytest functions below, they need to start with test_


@pytest.fixture
def single_account() -> Account:
    return Account(owner='john')


@pytest.mark.parametrize('account', [(Account('mark')), (Account('paul'))])
def test_new_account(account) -> None:
    assert account.amount == 0


@pytest.mark.parametrize('account, amount', [(Account('mark', 10), 10),
                                             (Account('paul', 1), 1)])
def test_new_account_with_amount(account, amount) -> None:
    assert account.amount == amount


def test_single_balance(single_account: Account) -> None:
    single_account.add_transaction(10)
    assert single_account.balance == 10
    # update
    single_account.add_transaction(5)
    assert single_account.balance == 15

    single_account.add_transaction(-5)
    assert single_account.balance == 10


def test_error_message(single_account) -> None:
    try:
        single_account.add_transaction('1')
    except ValueError as err:
        assert str(err) == 'please use int for amount'


def test_add_transaction_value_error(single_account: Account) -> None:
    with pytest.raises(ValueError):
        single_account.add_transaction(5.5)


def test_print(single_account) -> None:
    str_account = 'Account of john with starting amount: 0'
    repr_account = 'Account(\'john\', 0)'
    assert str(single_account) == str_account
    assert repr(single_account) == repr_account

    # JOIN

    joint_account = single_account + Account('jain')
    str_account = 'Account of john&jain with starting amount: 0'
    repr_account = 'Account(\'john&jain\', 0)'
    assert str(joint_account) == str_account
    assert repr(joint_account) == repr_account


def test_size(single_account) -> None:
    single_account.add_transaction(10)
    single_account.add_transaction(20)
    assert len(single_account) == 2

    # JOIN

    other_account = Account('jain')
    other_account.add_transaction(10)
    other_account.add_transaction(10)
    joint_account = single_account + other_account
    assert len(joint_account._transactions) == 4


def test_get_transaction(single_account) -> None:
    single_account.add_transaction(10)
    single_account.add_transaction(20)
    assert single_account[0] == 10
    assert single_account[1] == 20


def test_get_transaction_indexerror(single_account) -> None:
    with pytest.raises(IndexError):
        assert single_account[0] == 10


def test_compair(single_account) -> None:
    other = Account('jain')

    assert single_account == other
    assert single_account <= other

    single_account.add_transaction(1)
    assert single_account > other
    other.add_transaction(1)
    assert single_account >= other

    other.add_transaction(1)
    assert single_account < other
    single_account.add_transaction(1)
    assert single_account <= other


def test_add_accounts(single_account) -> None:
    other = Account('jain')
    joint_acc = single_account + other
    assert joint_acc.owner == 'john&jain'


def test_add_accounts_balance(single_account) -> None:
    single_account.add_transaction(10)
    other_account = Account('jain', 10)
    old_balance = single_account.balance + other_account.balance
    new_acc = single_account + other_account
    assert new_acc.balance == old_balance


def test_add_raise_error(single_account) -> None:
    with pytest.raises(AttributeError):
        new_acc = single_account + 'Account("jain", 100)'
