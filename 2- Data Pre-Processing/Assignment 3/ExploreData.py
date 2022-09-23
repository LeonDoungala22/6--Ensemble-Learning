#Count null values
def count_na_rows():
    print(Data.isnull().sum())
    print("\nData shape:",Data.shape)
    
