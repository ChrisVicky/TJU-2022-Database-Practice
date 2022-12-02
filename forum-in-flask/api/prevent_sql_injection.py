import re

def sql_injection_check(input_str: str) -> (bool, str):
    """
    Check if the input string contains SQL injection.
    :param input_str: input string
    :return: (True, replaced string) if SQL injection is detected, otherwise (False, '')
    """
    sql_injection_pattern = re.compile(r"('|;|--|/\*|\*/|xp_cmdshell|exec|execute|insert|select|delete|update|count|)")
    if sql_injection_pattern.search(input_str):
        return True, sql_injection_pattern.sub('', input_str)
    else:
        return False, input_str


if __name__ == '__main__':
    # Test
    test_str = "'select * from users where username = \"admin\" and password"
    print(sql_injection_check(test_str))
