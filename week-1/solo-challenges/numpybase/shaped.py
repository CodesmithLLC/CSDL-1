from functools import reduce

class Shaped(list):
    def __init__(self, lst, *args, **kwargs):
        lst_shape = Shaped.get_shape(lst)
        assert lst_shape, "list does not have well-defined shape"
        self.shape = lst_shape
        super().__init__(lst, *args, **kwargs)

    @staticmethod
    def get_shape(val):
        if not isinstance(val, list):
            return ()
        shapes = [Shaped.get_shape(x) for x in val]
        first = shapes[0]
        return (
            (len(val),) + first if
            reduce(lambda acc, shape: acc and shape == first, shapes, True) else
            False
        )
