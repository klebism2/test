class BuddySystem:
    """A simple buddy/pair system for matching users with buddies."""

    def __init__(self):
        self._pairs = {}  # user -> buddy (bidirectional)

    def add_user(self, user: str) -> None:
        """Register a user in the buddy system."""
        if user not in self._pairs:
            self._pairs[user] = None

    def pair(self, user1: str, user2: str) -> None:
        """Pair two users as buddies.

        Raises ValueError if either user already has a buddy.
        """
        if user1 not in self._pairs:
            self.add_user(user1)
        if user2 not in self._pairs:
            self.add_user(user2)

        if self._pairs[user1] is not None:
            raise ValueError(f"{user1} already has a buddy: {self._pairs[user1]}")
        if self._pairs[user2] is not None:
            raise ValueError(f"{user2} already has a buddy: {self._pairs[user2]}")
        if user1 == user2:
            raise ValueError("A user cannot be their own buddy")

        self._pairs[user1] = user2
        self._pairs[user2] = user1

    def get_buddy(self, user: str) -> str | None:
        """Return the buddy of the given user, or None if unpaired."""
        if user not in self._pairs:
            raise KeyError(f"Unknown user: {user}")
        return self._pairs[user]

    def unpair(self, user: str) -> None:
        """Remove the buddy pairing for a user."""
        if user not in self._pairs:
            raise KeyError(f"Unknown user: {user}")
        buddy = self._pairs[user]
        if buddy is not None:
            self._pairs[buddy] = None
        self._pairs[user] = None

    def list_pairs(self) -> list[tuple[str, str]]:
        """Return a list of (user, buddy) pairs (each pair listed once)."""
        seen = set()
        result = []
        for user, buddy in self._pairs.items():
            if buddy is not None and buddy not in seen:
                result.append((user, buddy))
            seen.add(user)
        return result

    def users(self) -> list[str]:
        """Return all registered users."""
        return list(self._pairs.keys())
