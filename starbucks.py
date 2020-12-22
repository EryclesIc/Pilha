class Starbucks:
    def __init__(self, data, n):
        self.brand = data.Brand[n]
        self.store_number = data['Store Number'][n]
        self.ownership_type = data['Ownership Type'][n]
        self.street_address = data['Street Address'][n]
        self.city = data.City[n]
        self.state_province = data['State/Province'][n]
        self.country = data.Country[n]
        self.postcode = data.Postcode[n]
        self.phone_number = data['Phone Number'][n]
        self.timezone = data.Timezone[n]
        self.longitude = data.Longitude[n]
        self.latitude = data.Latitude[n]