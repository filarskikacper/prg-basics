def f(password):
    if len(password) < 6:
        return False
    else:
        if(len(set(password)) != len(password)):
            return False
    return True
