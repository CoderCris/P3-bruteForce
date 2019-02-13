class Server:

    def __init__(self):

        self.server = {}

    def add(self, name, password):
        self.server[name] = password
