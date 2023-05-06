# takes the dict and the key that is supposed to be inside the dict
# returns the value of that key or None incase the key is not inside the dict
def get_or_none(dictionary, key):
    return dictionary[key] if dictionary.__contains__(key) else None
