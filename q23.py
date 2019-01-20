#coding:utf-8
def check_pass(password):
    if len(password) >= 10 and not password.isalpha() and not password.isdigit() and not password.islower() and not password.isupper():
        return True
    else:
        return False

print(check_pass("dsfihdsoiHYGYU876"))