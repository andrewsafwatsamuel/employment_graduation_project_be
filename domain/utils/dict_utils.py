
def get_or_none(immutable_multi_dict, key):
    return immutable_multi_dict[key] if immutable_multi_dict.__contains__(key) else None
