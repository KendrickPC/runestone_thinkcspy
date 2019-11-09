# 19.7.0 Case Study
'''
Postal addresses are interesting things. Every country has its own format for postal addresses, and sometimes one country can have multiple address formats.

Postal addresses generally consist of a few standard elements: the recipient name; street address; city or locality; state or province; and a postal code. However, other elements are often included, such as neighborhood, district, post office identifier, and so on. For example, the following is

Mr. Abe Jones
Acme Corporation
123 Somewhere Ln
Greenville, SC 29609
USA
This same address would be written as follows for delivery to the Netherlands (in the example, the street, city, and state are unchanged, even though they do not exist in the Netherlands):

Acme Corporation
Mr. Abe Jones
Somewhere Ln 123
29609 SC Greenville
NETHERLANDS
Addresses in Ireland are complex, having up to 12 parts (such as building name and number, primary and secondary thoroughfare, primary and secondary locality, town, county, …) plus an Eircode, a unique identifier assigned to each of the ~2 million addresses in Ireland. For example, Abe might live at the following address (English translation is given in parentheses, and would be omitted):

Abe Jones
Cnoc na Sceiche (The Hill of the Thorn)
Leac an Anfa (The Flagstone of the Storm)
Cathair na Mart (The City of the Beeves)
Co. Mhaigh Eo (The County of the Plain of the Yews)
A65 F4E2
IRELAND
(One would think that since each address has its own unique Eircode, it ought to be possible to address mail to Abe Jones, A65 F4E2, IRELAND. On second thought, perhaps that is not such a great idea. Can you imagine the practical concerns with such a scheme?)

'''