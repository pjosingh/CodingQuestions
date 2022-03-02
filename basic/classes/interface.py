class Location(object):

    def __init__(self, type):
        self.type = ""

    def get_location(self):
        pass


class InternetLocation(Location):

    def __init__(self):
        self.type = "Internet"

    def get_location(self):
        print("type: "+self.type)

class LocalLocation(Location):

    def __init__(self):
        self.type = "Local"
    def get_location(self):
        print("type: "+self.type)


location = LocalLocation()
location.get_location()


location = InternetLocation()
location.get_location()
