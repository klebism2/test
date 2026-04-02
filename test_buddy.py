import pytest
from buddy import BuddySystem


def test_add_user():
    bs = BuddySystem()
    bs.add_user("alice")
    assert "alice" in bs.users()


def test_pair_and_get_buddy():
    bs = BuddySystem()
    bs.pair("alice", "bob")
    assert bs.get_buddy("alice") == "bob"
    assert bs.get_buddy("bob") == "alice"


def test_auto_registers_users_on_pair():
    bs = BuddySystem()
    bs.pair("alice", "bob")
    assert "alice" in bs.users()
    assert "bob" in bs.users()


def test_no_self_buddy():
    bs = BuddySystem()
    with pytest.raises(ValueError, match="own buddy"):
        bs.pair("alice", "alice")


def test_already_paired_raises():
    bs = BuddySystem()
    bs.pair("alice", "bob")
    with pytest.raises(ValueError, match="already has a buddy"):
        bs.pair("alice", "carol")


def test_get_buddy_unknown_user():
    bs = BuddySystem()
    with pytest.raises(KeyError):
        bs.get_buddy("nobody")


def test_unpair():
    bs = BuddySystem()
    bs.pair("alice", "bob")
    bs.unpair("alice")
    assert bs.get_buddy("alice") is None
    assert bs.get_buddy("bob") is None


def test_unpair_then_repair():
    bs = BuddySystem()
    bs.pair("alice", "bob")
    bs.unpair("alice")
    bs.pair("alice", "carol")
    assert bs.get_buddy("alice") == "carol"


def test_list_pairs():
    bs = BuddySystem()
    bs.pair("alice", "bob")
    bs.pair("carol", "dave")
    pairs = bs.list_pairs()
    assert len(pairs) == 2
    assert ("alice", "bob") in pairs or ("bob", "alice") in pairs
    assert ("carol", "dave") in pairs or ("dave", "carol") in pairs


def test_unpaired_user_not_in_list_pairs():
    bs = BuddySystem()
    bs.add_user("alice")
    assert bs.list_pairs() == []
