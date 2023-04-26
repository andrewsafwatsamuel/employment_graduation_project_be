import re


def is_valid_string_input(input, pattern=None):
    return (input is not None) \
        and (len(input.strip()) > 0) \
        and (re.match(pattern if pattern is not None else ".*", input))
