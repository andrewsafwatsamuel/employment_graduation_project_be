def parametrized_query(index):
    return "'{" + str(index) + "}'"


def create_insert_query(table_name, params):
    params_string = ""
    parameterized_indexes = ""
    for param in params:
        params_string += f"{param} , "
    for index in range(len(params)):
        parameterized_indexes += "%s , "
    query = f""" INSERT INTO {table_name} ( {params_string.removesuffix(", ")} ) VALUES ( {parameterized_indexes.removesuffix(", ")} );"""
    return query


def create_insert_multi_values_query(table_name, params, values_count):
    params_string = ""
    parameterized_indexes = ""
    for param in params:
        params_string += f"{param} , "
    for i in range(values_count):
        place_holders = ""
        for index in range(len(params)):
            place_holders += "%s , "
        parameterized_indexes += f"\n ({place_holders.removesuffix(', ')}), "
    query = f""" INSERT INTO {table_name} ( {params_string.removesuffix(", ")} ) VALUES {parameterized_indexes.removesuffix(", ")};"""
    return query


def create_retrieve_query(table_name, columns=None, where_clause=None):
    where = ""
    if where_clause is not None and len(where_clause) > 0:
        where = f"WHERE {where_clause}"

    if columns is None or len(where_clause) == 0:
        selection = "*"
    else:
        selection = str(columns).replace("[", "").replace("]", "")
    query = f""" SELECT {selection} FROM {table_name} {where}"""
    return query


def create_delete_query(table_name, where_clause=None):
    where = ""
    if where_clause is not None and len(where_clause) > 0:
        where = f"WHERE {where_clause}"
    query = f""" DELETE FROM {table_name} {where}"""
    return query
