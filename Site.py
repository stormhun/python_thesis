class Site:
    def __init__(self, name, lat, long):
        self.name = name
        self.lat = lat
        self.long = long
        self.sightings = []

    def add_sighting(self, sighting):
        self.sightings.append(sighting)

    def get_sightings(self):
        return self.sightings

    def get_name(self):
        return self.name

    def get_latitude(self):
        return self.lat

    def get_longitude(self):
        return self.long

    def __str__(self):
        return f"Site: {self.name}, Latitude: {self.lat}, Longitude: {self.long}, Sightings: {len(self.sightings)}"
class Sighting:
    def __init__(self, date, animal, site):
        self.date = date
        self.animal = animal
        self.site = site

    def get_date(self):
        return self.date

    def get_animal(self):
        return self.animal

    def get_site(self):
        return self.site

    def __str__(self):
        return f"Date: {self.date}, Animal: {self.animal}, Location: {self.site.name}"

