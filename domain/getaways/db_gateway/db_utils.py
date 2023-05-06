# takes list of dictionaries
# returns values of all dictionaries as list
def flatten_dict_array_values(foreign_key, dict_array):
    result = []
    for dictionary in dict_array:
        result.append(foreign_key)
        result.extend(dictionary.values())
    return result
