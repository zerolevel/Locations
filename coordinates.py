class Coordinates:
    def __init__(self, name=None, given_query=None, lat=None, lng=None, state=None, district=None, sub_district=None,
                 level=None, quality="No_Information_Provided"):
        self.lat = lat
        self.lng = lng
        self.given_query = given_query
        self.state = state
        self.district = district
        self.sub_district = sub_district
        self.level = level
        self.name = name
        self.quality = quality

    def __eq__(self, other):
        return abs(float(self.lat) - float(other.lat)) < 0.00001 and \
            abs(float(self.lng) - float(other.lng)) < 0.00001 and \
            self.state == other.state and \
            self.district == other.district and \
            self.sub_district == other.sub_district and \
            self.level == other.level and \
            self.name == other.name

    def __repr__(self):
        return str(self.lat) + " " + str(self.lng) + " " + str(self.state) + " " +\
               str(self.district) + " " + str(self.sub_district) + " " + str(self.level) + " " + str(self.name)