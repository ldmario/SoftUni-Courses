class Calculator:

    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        res = args[0]
        for n in args[1:]:
            res *= n
        return res

    @staticmethod
    def divide(*args):
        res = args[0]
        for n in args[1:]:
            res /= n
        return res

    @staticmethod
    def subtract(*args):
        res = args[0]
        for n in args[1:]:
            res -= n
        return res
