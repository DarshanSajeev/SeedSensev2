#@Tireni Oluwabunmi(TireniO)

#Turn 2dlist matrix into a string
def WriteToDb(ListMatrix):
    """
    Functionality:
        Seprates rows via "+" character and values on rows
        via "," char

    Returns:
        2dlist of strings
    """

    for i in range(len(ListMatrix)):
        for value in ListMatrix[i]:
            ToWrite += str(value) + ","
        ToWrite += "+"

    return ToWrite


#Turn stringfied matrix intto a 2dlist
def ReadFromDb(str StrMatrix):
    """
    Functionality:
        Seprate values within 1d lists via "," char and once
        end of row is reached adds + to string

    Returns:
        2dlist of strings
    """
    TwoDList = []

    SplitString = StrMatrix.split("+")

    for row in range(len(SplitString)):
        CurrentRow = row.split(",")
        TwoDList.append(CurrentRow)

    return TwoDList

    

    
            
    

