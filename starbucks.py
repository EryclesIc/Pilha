class Starbucks(object):
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
        self.longitude = str(data.Longitude)
        self.latitude = str(data.Latitude)
    
    def __str__(self):
        return ('Brand: '+ self.brand + '\n'
        'Store Number'+ self.store_number + '\n'
        'Ownership Type'+ self.ownership_type + '\n'
        'Street Address'+ self.street_address + '\n'
        'City'+ self.city + '\n'
        'State Province'+ self.state_province + '\n'
        'Country'+ self.country + '\n'
        'Postcode'+ self.postcode + '\n'
        'Phone Number'+ self.phone_number + '\n'
        'Timezone'+ self.timezone + '\n'
        'Longitude'+ self.longitude + '\n'
        'Latitude'+ self.latitude + '\n')