from typing import Any

# Metaclass
class Singleton(type):
    
    instance = None

    def __call__(self, *args, **kwargs):
        print(self, *args, **kwargs)
        if self.instance is None:
            self.instance = super().__call__(*args, **kwargs)
        
        return self.instance
