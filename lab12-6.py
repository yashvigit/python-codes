class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __eq__(self, other):
        if isinstance(other, Date):
            return (self.day == other.day and
                    self.month == other.month and
                    self.year == other.year)
        return False

date1 = Date(10, 10, 2023)
date2 = Date(10, 10, 2023)
date3 = Date(11, 10, 2023)

print(date1 == date2)  
print(date1 == date3) 