class Starbucks:
    def __init__(self, data):
        self.brand = data.Brand
        self.store_number = data['Store Number']
        self.ownership_type = data['Ownership Type']
        self.street_address = data['Street Address']
        self.city = data.City
        self.state_province = data['State/Province']
        self.country = data.Country
        self.postcode = data.Postcode
        self.phone_number = data['Phone Number']
        self.timezone = data.Timezone
        self.longitude = data.Longitude
        self.latitude = data.Latitude

    def __repr__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %lf, %lf" %(self.brand,
                                                                    self.store_number,
                                                                    self.ownership_type,
                                                                    self.street_address,
                                                                    self.city,
                                                                    self.state_province,
                                                                    self.country,
                                                                    self.postcode,
                                                                    self.phone_number,
                                                                    self.timezone,
                                                                    self.longitude,
                                                                    self.latitude)