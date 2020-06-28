class Bst:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None 

    def __repr__(self):
        return (f"Value: {self.value}, Left: {self.left}, Right: {self.right}")

    def insert(self, value):
        if self.value > value:
            if self.laeft == None:
                self.left = Bst(value)
            else: 
                self.left.isert(value)

        if self.value <= value:
            if self.right == None:
                self.right.Bst(value)
            else:
                self.right.insert(value)