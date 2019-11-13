""" 
Bite 123. Find the user with most friends
"""
from collections import defaultdict

names = 'bob julian tim martin rod sara joyce nick beverly kevin'.split()
ids = range(len(names))
users = dict(zip(ids, names))  # 0: bob, 1: julian, etc

# user ID's
f1 = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7),
      (5, 9), (6, 8), (7, 8), (8, 9)]

f2 = [(0, 1), (0, 2), (1, 2), (1, 6), (2, 3), (3, 4), (4, 6), (5, 6), (5, 7),
      (5, 9), (6, 7), (6, 8), (6, 9)]

names2 = 'bob bob tim tim julian julian'.split()
ids2 = range(len(names2))
users2 = dict(zip(ids2, names2))
f3 = [(0, 1), (0, 2), (0, 4), (0, 5), (1, 3), (2, 4), (4, 5)]


def get_friend_with_most_friends(friendships, users):
    """Receives the friendships list of user ID pairs,
       parse it to see who has most friends, return a tuple
       of (name_friend_with_most_friends, his_or_her_friends)
    """
    friends = defaultdict(list)
    for u, f in friendships:
        friend = users[f]
        user = users[u]

        friends[u].append(friend)
        friends[f].append(user)

    result = sorted([(users[n], sorted(u)) for n, u in friends.items()],
                    key=lambda x: len(x[1]))[-1]
    return result


if __name__ == "__main__":
    print("-" * 45)
    print(get_friend_with_most_friends(f1, users))
    print("-" * 45)
    print(get_friend_with_most_friends(f2, users))
    print("-" * 45)
    print(get_friend_with_most_friends(f3, users2))
