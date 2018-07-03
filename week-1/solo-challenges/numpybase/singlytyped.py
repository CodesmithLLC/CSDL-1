from functools import reduce

class SinglyTyped(list):
    def __init__(self, lst, *args, **kwargs):
        lst_type = SinglyTyped.get_type(lst)
        assert lst_type, "list is not singly-typed"
        self.dtype = lst_type[1]
        super().__init__(lst, *args, **kwargs)

    @staticmethod
    def get_type(val):
        if not isinstance(val, list):
            return (0, type(val))

        types = [SinglyTyped.get_type(x) for x in val]
        first = types[0]
        if not first: return False
        return (
            (first[0] + 1, first[1]) if
            reduce(lambda acc, tup: acc and tup == first, types,True) else
            False
        )
