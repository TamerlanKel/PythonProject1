import inspect

class SomeClass:
    def __init__(self):
        self.attribute_1 = 10

def introspection_info(obj):
    obj_type = type(obj)
    obj_attributes = hasattr(obj, 'attribute_1')
    methods = dir(obj)
    obj_modules = getattr(obj, '__module__', '__main__')
    return {'type': obj_type,
            'attributes': obj_attributes,
            'methods': methods,
            'module': obj_modules}

number_info = introspection_info(42)
print(number_info)
