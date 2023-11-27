class Program:

    def __init__(self, name, connections=None, used=False):
        self.name = name
        self.connections = connections
        self.used = used

    def __str__(self):

        string = "Name: {} Connections: ".format(self.name)
        for connection in self.connections:
            string += connection.name + " "
        
        return string