class Starbucks:
    def __init__(self, data):
        self.data = data
        self.store_number = data['Store Number'].replace("-","")
        self.starbucks_data = {self.store_number: self.data}
        
    def __repr__(self):
        return "%s" %(self.starbucks_data)