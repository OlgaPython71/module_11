import inspect
from pprint import pprint


def introspection_info(obj):
    type_obj = type(obj)
    attr_obj = dir(obj)
    module_obj = inspect.getmodule(introspection_info)
    return type_obj, attr_obj, module_obj


number_info = introspection_info(42)
pprint(number_info)
