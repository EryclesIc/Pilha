class Cord19:
    def __init__(self, index_key, line):
        self.line = line
        if index_key == 0:
            self.key = self.line.Brand
        elif index_key == 1:
            self.key = self.line.'Store Number'
        elif index_key == 2:
            self.key = self.line.'Ownership Type'
        elif index_key == 3:
            self.key = self.line.'Street Address'
        elif index_key == 4:
            self.key = self.line.City
        elif index_key == 5:
            self.key = self.line.'State/Province'
        elif index_key == 6:
            self.key = self.line.Country
        elif index_key == 7:
            self.key = self.line.Postcode
        elif index_key == 8:
            self.key = self.line.'Phone Number'
        elif index_key == 9:
            self.key = self.line.Timezone
        elif index_key == 10:
            self.key = self.line.Longitude
        elif index_key == 11:
            self.key = self.line.Latitude
        self.left = None
        self.right = None

    def __str__(self):
        return "Brand: {0}\nStore Number: {1}\nStore Name: {2}\nOwnership Type: {3}\nStreet Address: {4}\nCity: {5}\nState/Province: {6}\nCountry: {7}\nPostcode: {8}\nPhone Number: {9}\nTimezone: {10}\nLongitude: {11}\nLatitude:".format(self.line.Brand,
                                                                                                                                                                                                                                             self.line.'Store Number',
                                                                                                                                                                                                                                             self.line.'Store Name',
                                                                                                                                                                                                                                             self.line.'Ownership Type',
                                                                                                                                                                                                                                             self.line.'Street Address',
                                                                                                                                                                                                                                             self.line.City,
                                                                                                                                                                                                                                             self.line.'State/Province',
                                                                                                                                                                                                                                             self.line.Country,
                                                                                                                                                                                                                                             self.line.Postcode,
                                                                                                                                                                                                                                             self.line.'Phone Number',
                                                                                                                                                                                                                                             self.line.Timezone,
                                                                                                                                                                                                                                             self.line.Longitude,
                                                                                                                                                                                                                                             self.line.Latitude)