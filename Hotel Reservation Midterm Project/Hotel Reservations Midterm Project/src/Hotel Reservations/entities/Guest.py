class Guest:
    def __init__(self, data_row):
        self.data_row = data_row
        self.adults= data_row["adults"]
        self.children= data_row["children"]
        self.babies=data_row["babies"]
        self.country=data_row["country"]
   
   

