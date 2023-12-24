class Guest:

    def __init__(self, data_row):
        """
        constructore for he guest class
        parameters:
        self(Guest)
        data_row(data row): row of data
        variables:
        self.data_row(data row): the dat row passed in 
        self.adults(int): number of adults in that row
        self.children(int): number of children in that row
        self.babies(int): number of babies in that row 
        self.country(str): country of that row
        """
        self.data_row = data_row
        self.adults= data_row["adults"]
        self.children= data_row["children"]
        self.babies=data_row["babies"]
        self.country=data_row["country"]

    def __str__(self):
        """
        return:
        a string of the guest information 
        """
        return f"Number of adults={self.adults}, Number of children={self.children}, Number of babies={self.babies}, Country={self.country}"
    
 
   
   

