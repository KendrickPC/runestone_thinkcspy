# 19.7.1 Storing Postal Addresses
'''
Suppose we want to write a contact management application. Among other things, the application stores names and addresses. What would be the best way to design a class that holds the information for an address? One approach would be to store the parts of the address that are consistent, such as the recipient name and the country, in instance variables, and store the rest of the address as a list of address lines:
'''


    # class Address:

    #     def __init__(self, recipient, addressLines, country):
    #         self.country = country
    #         self.recipient = recipient
    #         self.addressLines = addressLines


    # addy = Address('Ken Chang', ['650 明水路', '中山區, 台北'], 'Taiwan')
    # print(addy)


'''
This approach treats an address as a collection of unstructured bits of information. If we want to look up an address, we can search by full name or country, but if we want to find all addresses in Greenville, or all addresses in zip code 29609, we can’t do it very easily, since information such as city and zip code is mashed together in an unstructured address line along with the state abbreviation.

An approach that stores addresses as structured pieces of information might look like this:
'''


class StructuredAddress:

    def __init__(self, country, recipient, street, city, state, postalCode):
        self.country = country
        self.recipient = recipient
        self.street = street
        self.city = city
        self.state = state
        self.postalCode = postalCode


    def display(self):
        print(self.recipient)
        print(self.street)
        print(self.city + ", " + self.state + " " + self.postalCode)
        print(self.country)

addy = StructuredAddress('USA', 'Kendrick Chang', '1 Infinite Loop', 'Cupertino', 'CA', '95014')

# addy.display()


'''
Now, if we have a list of StructuredAddress objects and we want to find all of the ones that hold addresses in Greenville, we can do it much more easily:

    for addr in addrList:
        if addr.city == 'Greenville':
            addr.display()

'''



















