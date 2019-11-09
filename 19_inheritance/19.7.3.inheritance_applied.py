# 19.7.3 Inheritance Applied
'''
Let’s apply inheritance to the problem of managing structured postal addresses. We will define a base class that contains the attributes in common to all postal addresses: recipient and country.

'''


class BasePostalAddress:
    
    def __init__(self, country, recipient):
        self.country = country
        self.recipient = recipient

    def display(self):
        print(self.recipient)
        print(self.country)

    def validate(self):
        return self.recipient != '' and self.country != ''


'''
This class isn’t very useful by itself; relatively few people in the world could receive mail addressed to them using only their name and country. But it does establish two methods to perform functionality we want all addresses to perform: display themselves, and check whether the required information is present and of an appropriate length.

Next, we build on BasePostalAddress by creating a separate class for each country that inherits from it:
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













