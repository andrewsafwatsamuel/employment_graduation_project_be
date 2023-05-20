from domain.getaways.db_gateway.operations.employee_db_operation import remove_experience


def remove_experience_use_case(employee_id, experience_id, operation=remove_experience):
    if employee_id is None or experience_id is None:
        raise Exception("Invalid data")
    return operation(experience_id, experience_id) > 0
