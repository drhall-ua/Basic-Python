# Method for converting 2 lists into a dictionary

def to_dict(keys, values):
    return dict(zip(keys, values))

key = ["a", "b", "c"]
val = [1, 2, 3]
print(to_dict(key, val))

