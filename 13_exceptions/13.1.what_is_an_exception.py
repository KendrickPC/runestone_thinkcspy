# 13.1 What is an exception?
'''
An exception is a signal that a condition has occurred that can’t be easily
handled using the normal flow-of-control of a Python program. Exceptions are
often defined as being “errors” but this is not always the case. All errors
in Python are dealt with using exceptions, but not all exceptions are errors.
'''

# 13.2. Exception Handling Flow-of-control
'''
In Python, your create an exception message using the raise command. The
simplest format for a raise command is the keyword raise followed by the
name of an exception. For example:

        def main()
          A()

        def A():
          B()

        def B():
          C()

        def C():
          D()

        def D()
          # processing


    raise ExceptionName


    def main()
      A()

    def A():
      B()

    def B():
      C()

    def C():
      D()

    def D()
      try:
        # processing code
        if something_special_happened:
          raise MyException
      except MyException:
        # execute if the MyException message happened

But perhaps function C is better able to handle the issue, so you could put
the try: except: block in function C:

    def main()
      A()

    def A():
      B()

    def B():
      C()

    def C():
      try:
        D()
      except MyException:
        # execute if the MyException message happened

    def D()
      # processing code
      if something_special_happened:
        raise MyException

But perhaps the main function is better able to handle the issue, so you could
put the try: except: block in the main function:


    def main()
      try:
        A()
      except MyException:
        # execute if the MyException message happened

    def A():
      B()

    def B():
      C()

    def C():
      D()

    def D()
      # processing code
      if something_special_happened:
        raise MyException


'''










