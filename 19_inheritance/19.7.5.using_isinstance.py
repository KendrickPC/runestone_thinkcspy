'''
Let’s try something else with our list of addresses. Suppose we wanted to display all addresses with a given city. We might write some code like this:

    for addr in addrList:
        if addr.city == 'Greenville':
            addr.display()

However, we would get into trouble on the first iteration of the loop. The first address is an Irish address, which does not have a city attribute. Python would raise an error. We want to perform this test only for US addresses.

In this case, since all addresses have a country attribute, we could write the loop this way:

    for addr in addrList:
        if addr.country == 'USA' and addr.city == 'Greenville':
            addr.display()

Another way to test the address is to find out if the object belongs to a specific class. Python provides the isinstance() function for this purpose. isinstance() is designed for situations where you want to access a field or invoke a method on an object, but you want to do so only if the object provides the needed functionality. Given an object obj and a class cls, isinstance(obj, cls) returns True if obj is an instance of cls (or a subclass of cls), and False if it is not. Here is how we might use it in our loop:

    for addr in addrList:
        if isinstance(addr, USPostalAddress) and addr.city == 'Greenville':
            addr.display()

In this version of the code, the city attribute will be tested only if addr references an instance of USPostalAddress, or a child of USPostalAddress (which would also have a city attribute).

Now that you’ve learned about isinstance(), you should know that, like inheritance itself, isinstance() should be used sparingly. Code that invokes isinstance() is often performing work on an object that the object should be designed to do itself, and is not utilizing inheritance and polymorphism to its full potential.

To make this loop better utilize inheritance and polymorphism, we need a way to test each address to see if it is in a given city. Let’s add a method to BasePostalAddress for this purpose. It will return a boolean indicating whether the address is in a certain city.

    class BasePostalAddress:

        ...

        def isInCity(self, city):
            return False


BasePostalAddresses do not have a city attribute, so they just return False. USPostalAddresses do have a city, so we’ll override this method for that class:

    class USPostalAddress:

        ...

        def isInCity(self, city):
            return self.city == city


Now, we rewrite our loop to use isInCity() to perform the test:

    for addr in addrList:
        if addr.isInCity('Greenville'):
            addr.display()

Notice how we’ve eliminated the isinstance() test. Also, notice how this test works for IrishPostalAddress objects, even though we didn’t define isInCity() for IrishPostalAddress, since IrishPostalAddress inherits its version from BasePostalAddress.

'''

