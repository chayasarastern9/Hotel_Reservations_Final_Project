class Guest:

    def __init__(self, data_row):
        """
        constructore for he guest class
        parameters:
        self(Guest)
        data_row(data row): row of data
        variables:
        self.data_row(data row): the dat row passed in 
        self.adults_int(int): number of adults in that row
        self.children_int(int): number of children in that row
        self.babies_int(int): number of babies in that row 
        self.country_int(str): country of that row
        """
        self.data_row = data_row
        self.adults_int= data_row["adults"]
        self.children_int= data_row["children"]
        self.babies_int=data_row["babies"]
        self.country_str=data_row["country"]

    def __str__(self):
        """
        return:
        a string of the guest information 
        """
        return f"Number of adults={self.adults_int}, Number of children={self.children_int}, Number of babies={self.babies_int}, Country={self.country_str}"
    
 
   
   

