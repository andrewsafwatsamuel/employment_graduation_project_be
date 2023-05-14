from domain.getaways.db_gateway.operations.employee_db_operation import retrieve_employee_with_experiences


def get_employee_profile_use_case(emp_id, operation=retrieve_employee_with_experiences):
    if emp_id is None:
        raise Exception("Something went wrong")
    return operation(emp_id)
