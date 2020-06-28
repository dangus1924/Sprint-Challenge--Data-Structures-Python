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

    def contains(self, target):
        if target == self.value:
            return True
        elif target > self.value:
            if self.right != None:
                return self.right.contains(target)
            else:
                return False

        elif target < self.value:
            if self.left != None:
                return self.left.contains(target)
            else:
                return False

    def get_max(self):
        if self.right != None:
            return self.right.get_max()
        else:
            return self.value


    def for_each(self, fn):
        fn(self.value)
        if self.right:
            self.right.for_each(fn)
        if self.left:
            self.left.for_each(fn)