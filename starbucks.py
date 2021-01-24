class Starbucks:
    def __init__(self, data):
        self.store_number = data['Store Number']
        self.teste = {self.store_number: data}
        
    def __repr__(self):
        return "%s" %(self.teste)
        # return "%s" %(self.store_number)