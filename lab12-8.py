class String:
    def __init__(self, s=""):
        self.str = s

    def __iadd__(self, other):
        if isinstance(other, String):
            self.str += other.str
        elif isinstance(other, str):
            self.str += other
        else:
            raise TypeError("Operand must be a String or str")
        return self

    def toLower(self):
        self.str = self.str.lower()

    def toUpper(self):
        self.str = self.str.upper()

    def __str__(self):
        return self.str
