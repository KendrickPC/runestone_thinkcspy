# 19.7.4. A List of Addresses
'''
Normally, if a program iterates over a list that contains different types of objects, it has to be careful about making assumptions about the methods and operations that it can invoke on the different objects in the list, since an attempt to invoke a method or apply an operator to an object that does not support the method or operator will result in a runtime error. In this case, we know that all of the objects in the list inherit from BasePostalAddress. It is safe to invoke any methods defined in BasePostalAddress, since all children of BasePostalAddress are guaranteed to contain those methods. Programs that use inheritance often contain loops like this.

Notice something else. As the loop iterates over the list, each time the display() method is invoked, the computer will execute the one that is defined for the specific object referenced by addr. The first time through the loop, addr references an IrishPostalAddress, so the display() method for Irish addresses is invoked. The second time through the loop, the display() method in USPostalAddress is invoked. This behavior—where the computer always executes the method that is defined for the object being referenced—is called polymorphism. Python exhibits this behavior whether or not the objects in question utilize inheritance, but languages like Java and C++, polymorphism is available only through inheritance.

'''

class IrishPostalAddress(BasePostalAddress):

    def __init__(self, recipient, postalCode):
        super().__init__("IRELAND", recipient)
        self.postalCode = postalCode

    def display(self):
        print(self.recipient)
        print(self.postalCode)
        print(self.country)

    def validate(self):
        return super().validate() and len(self.postalCode) == 7


class USPostalAddress(BasePostalAddress):

    def __init__(self, recipient, street, city, state, zipcode):
        super().__init__("USA", recipient)
        self.street = street
        self.city = city
        self.state = state
        self.zip = zipcode

    def display(self):
        print(self.recipient)
        print(self.street)
        print(self.city + ", " + self.state + " " + self.zip)
        print(self.country)

    def validate(self):
        return (super().validate() and self.city != '' and len(self.state) == 2 and (len(self.postalCode) == 5 or len(self.postalCode) == 9))



addrList = [IrishPostalAddress("Alf Jones", "A26F4G9"),
            USPostalAddress("Abe Jones", "103 Anywhere Ln",
                "Greenville", "SC", "29609"),
            IrishPostalAddress("Gabe Jones", "A65F4E2")]

for addr in addrList:
    addr.display()

