class Node:

    def __init__(self, name, weight, children):
        self.name = name
        self.weight = weight
        self.children = children
        self.total = 0

    def __str__(self):

        string = "Name: {} Weight: {} Children: [".format(self.name, self.weight)
        for child in self.children:
            string+= str(child)
            if len(self.children) > 1 and child != self.children[-1]:
                string+=", "
        string += "]"
        
        return string