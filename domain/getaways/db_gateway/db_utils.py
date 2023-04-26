def paremetrized_query(index):
    return "'{" + str(index) + "}'"


def create_insert_query(table_name, params):
    params_string = ""
    parameterized_indexes = ""
    for param in params:
        params_string += f"{param} , "
    for index in range(len(params)):
        parameterized_indexes += "%s , "
    query = f""" INSERT INTO {table_name} ( {params_string.removesuffix(", ")} ) VALUES ( {parameterized_indexes.removesuffix(", ")} )"""
    return query
