class _const:
    class constError(TypeError):
        pass

    def __setattr__(self, name, value):
        if self.__dict__.has_key(name):
            raise self.constError, "exists key"
        self.__dict__[name] = value


import sys
sys.modules[__name__] = _const()
