# 13.3 Principles for Using Exceptions
'''
There are many bad examples of exception use on the Internet. The purpose
of an exception is to modify the flow-of-control, not to catch simple errors.
If your try: except: block is in the same function that raises the exception,
you are probably mis-using exceptions.

    Principle 1:
    If a condition can be handled using the normal flow-of-control,
    don’t use an exception!

    Principle 2:
    If you call a function that potentially raises exceptions, and you can do
    something appropriate to deal with the exception, then surround the code
    that contains the function call with a try: except: block.

    Principle 3:
    If you call a function that potentially raises exceptions, and you can’t do
    anything meaningful about the conditions that are raised, then don’t catch
    the exception message(s).

'''