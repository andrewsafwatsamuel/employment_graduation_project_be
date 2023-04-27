def parametrized_query(index):
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


def create_retrieve_query(table_name, columns=None, where_clause=None):
    where = ""
    selection = ""
    if where_clause is not None and len(where_clause) > 0:
        where += "WHERE "
        for index in range(len(where_clause)):
            item = where_clause[index]
            if item.upper().strip() in ("AND", "OR"):
                where += f"{item.upper().strip()} "
            else:
                where += f"{item} {parametrized_query(index)} "
    if columns is None or len(where_clause) == 0:
        selection = "*"
    else:
        selection = str(columns).replace("[", "").replace("]", "")
    return f""" SELECT {selection} FROM {table_name} {where}"""
