# Олег Молчанов уроки Пайтон


def measure_time(function):
    from datetime import datetime
    def wrapper():
        start = datetime.now()
        res = function()
        print(datetime.now() - start)
        return res
    return wrapper()