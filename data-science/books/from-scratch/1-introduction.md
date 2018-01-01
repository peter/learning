# 1. Introduction (Data Science from Scratch)

DataSciencester is a social network for data scientists.

## Key Connectors (Most Popular)

Your first job is to find "key connectors" amount data scientists
(those who are central to the network).

```python
users = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" },
    { "id": 2, "name": "Sue" },
    { "id": 3, "name": "Chi" },
    { "id": 4, "name": "Thor" },
    { "id": 5, "name": "Clive" },
    { "id": 6, "name": "Hicks" },
    { "id": 7, "name": "Devin" },
    { "id": 8, "name": "Kate" },
    { "id": 9, "name": "Klein" },
    { "id": 10, "name": "Jen" }
]

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

for user in users:
  user["friends"] = []

for i, j in friendships:
  users[i]["friends"].append(users[j])
  users[j]["friends"].append(users[i])

def number_of_friends(user):
  """Number of friends of a given user"""
  return len(user["friends"])

# Double check the friends arrays:
for user in users:
  print("user %s has %s friends: %s" % (user["id"],
                                        number_of_friends(user),
                                        map(lambda f: f["id"], user["friends"])))

total_connections = sum(number_of_friends(user) for user in users)

from __future__ import division

avg_connections = total_connections / len(users)

num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]
sorted(num_friends_by_id, key=lambda (user_id, num_friends): num_friends, reverse=True)
```

## Data Scientists You May Know

```python
def friends_of_friends_ids_bad(user):
  return [foaf["id"]
          for friend in user["friends"]
          for foaf in friend["friends"]]

print([friend["id"] for friend in users[0]["friends"]]) # => [1, 2]
print([friend["id"] for friend in users[1]["friends"]]) # => [0, 2, 3]
print([friend["id"] for friend in users[2]["friends"]]) # => [0, 1, 3]
```

```python
from collections import Counter

def users_eq(user1, user2):
  return user1["id"] == user2["id"]

def friends(user1, user2):
  return any(users_eq(friend, user2) for friend in user1["friends"])

def friends_of_friends_ids(user):
  return Counter(foaf["id"]
                 for friend in user["friends"]
                 for foaf in friend["friends"]
                 if not(users_eq(user, foaf))
                 and not(friends(user, foaf)))
```


```python
interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

from collections import defaultdict

interests_by_user = defaultdict(list)
for id, interest in interests:
  interests_by_user[id].append(interest)

users_by_interest = defaultdict(list)
for id, interest in interests:
  users_by_interest[interest].append(id)

import json
def pretty_json(obj):
  print json.dumps(obj, indent=4)

pretty_json(interests_by_user)
pretty_json(users_by_interest)

def most_common_interests_with(user):
  return Counter(interested_user_id
                 for interest in interests_by_user[user["id"]]
                 for interested_user_id in users_by_interest[interest]
                 if interested_user_id != user["id"])
```

## Salaries and Experience

```python
from __future__ import division

salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                        (48000, 0.7), (76000, 6),
                        (69000, 6.5), (76000, 7.5),
                        (60000, 2.5), (83000, 10),
                        (48000, 1.9), (63000, 4.2)]

def tenure_bucket(tenure):
  if tenure < 2:
    return "less than two"
  elif tenure < 5:
    return "between two and five"
  else:
    return "more than five"

salary_by_tenure_bucket = defaultdict(list)
for salary, tenure in salaries_and_tenures:
  salary_by_tenure_bucket[tenure_bucket(tenure)].append(salary)

average_salary_by_bucket = {
  tenure_bucket : sum(salaries) / len(salaries)
  for tenure_bucket, salaries in salary_by_tenure_bucket.iteritems()
}
```

## Topics of Interest

```python
from collections import Counter

word_counts = Counter(word
                      for user, interest in interests
                      for word in interest.lower().split())

for word, count in word_counts.most_common():
  if count > 1:
    print word, count
```

```python
```

```python
```

```python
```
