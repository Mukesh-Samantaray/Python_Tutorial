"""
Overview of Dictionaries in Python

A dictionary is an unordered, mutable collection of key-value pairs.
Each key must be unique and immutable (like int, str, tuple), while values can be of any type.

Creation:
- Using curly braces:        d = {"a": 1, "b": 2}
- Using dict constructor:    d = dict(a=1, b=2)

Key Operations:
- Access:           d["a"] or d.get("a")
- Add/Update:       d["c"] = 3
- Delete:           del d["b"] or d.pop("b")
- Check key:        "a" in d
- Length:           len(d)
- Iteration:
    for k in d: print(k, d[k])        # keys and values
    for k, v in d.items(): print(k,v) # unpacking key-value

Useful Methods:
- keys(), values(), items()
- update():         d.update({"x": 10})
- clear():          d.clear()
- copy():           new_d = d.copy()
- popitem():        Removes last inserted pair (LIFO)

Conversions:
- dict to list of keys:      list(d)
- dict to list of tuples:    list(d.items())
- list of tuples to dict:    dict([("a", 1), ("b", 2)])

Nested Dictionary:
- d = {"person": {"name": "Alice", "age": 25}}

Interview Tips:
- Dictionaries are hash maps (hash table implementation).
- Keys must be immutable (int, str, tuple), values can be anything.
- Lookup is O(1) average time.
"""

# Example
d = {"name": "Mukesh", "age": 25, "city": "Bhubaneswar"}

# Access
print(d["name"])
print(d.get("email", "Not found"))

# Update
d["age"] = 26
d["email"] = "mukesh@example.com"

# Delete
del d["city"]
popped = d.pop("email")

# Iteration
for k, v in d.items():
    print(f"{k}: {v}")

# Conversion
keys_list = list(d.keys())
values_list = list(d.values())
items_list = list(d.items())
new_dict = dict([("x", 1), ("y", 2)])

# Nested example
person = {
    "name": "Mukesh",
    "contact": {
        "email": "mukesh@gmail.com",
        "phone": "1234567890"
    }
}
print(person["contact"]["email"])

# Interview Question Practice
# 1. What is the difference between dict.get("key") and dict["key"]?
# 2. Can a list be a dictionary key? Why not?
# 3. What happens when you try to access a key that doesn’t exist?
# 4. How do you merge two dictionaries in Python 3.9+?
# 5. How is dictionary lookup so fast?

