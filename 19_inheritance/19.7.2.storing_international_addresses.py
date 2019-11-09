# 19.7.2 Storing International Addresses
'''
But now we have another problem. Our StructuredAddress works fine for U.S. addresses, but not for those of other countries. Suppose we want to handle Irish and Italian addresses. We might enhance the display() method to handle these with appropriate logic:

'''


def display(self):
    print(self.recipient)

    if self.country == 'USA':
        print(self.street)
        print(self.city + ", " + self.state + " " + self.postalCode)
    elif self.country == 'IRELAND':
        print(self.postalCode)
    elif self.country == 'ITALY':
        print(self.street)
        print(self.postalCode + ' ' + self.city + ' ' + self.state)
    else:
        pass

    print(self.country)



'''
This example works for Italian addresses because they conveniently have the same elements as U.S. addresses (just displayed in a slightly different order). For Irish addresses, we ignore the complicated address format and assume that the Irish post office will get mail to the recipient because of Ireland’s unique Eircode scheme. But what if we wanted to include the additional elements of Irish addresses? We might create additional instance variables for those elements in our StructuredAddress class. However, you can probably see that approach will quickly become unwieldy.
'''