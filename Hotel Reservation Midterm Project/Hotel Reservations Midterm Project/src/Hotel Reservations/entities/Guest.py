class Guest:
    def __init__(self, data_row):
        self.data_row = data_row
        self.adults= data_row["adults"]
        self.children= data_row["children"]
        self.babies=data_row["babies"]
        self.country=data_row["country"]

    def __str__(self):
        return f"Number of adults={self.adults}, Number of children={self.children}, Number of babies={self.babies}, Country={self.country}"
    
 
   
   

