"""
Obtained from
http://stackoverflow.com/questions/16746546/determine-whether-a-python-function-is-already-implemented-in-c-extension/16752719#16752719

Answered by Bakuriu (http://stackoverflow.com/users/510937/bakuriu)
This function can determine whether a function "obj" is implemented in C extension or not. 

If a function "cf" is in C extension,

>>is_implemented_in_c(cf)
True

However, this is not perfect. If a function "cf" in C extension is wrapped by a Python function "pf"

>>is_implemented_in_c(pf)
False

So even if all the computation done by "pf" is indeed done by "cf" in C, this will tell you "pf" is not implemented in C.
This is the best we can get - We can't determine this recursively due to Rice's theorem (http://en.wikipedia.org/wiki/Rice%27s_theorem).

"""
import types
def is_implemented_in_c(obj):
    if isinstance(obj, (types.FunctionType, types.LambdaType)):
        return False
    elif isinstance(obj, type):
        if '__dict__' in dir(obj): return False
        return not hasattr(obj, '__slots__')
    # We accept also instances of classes.
    # Return True for instances of C classes, False for python classes.
    return not isinstance(obj, types.InstanceType)

