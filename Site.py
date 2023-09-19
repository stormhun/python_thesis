import matplotlib.transforms as transforms
from svgpath2mpl import parse_path
from svgpathtools import svg2paths
import time
import matplotlib.pyplot as plt
import distinctipy
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
    def __len__(self):
        return len(self.sightings)
    def get_name(self):
        return self.name

    def get_latitude(self):
        return self.lat

    def get_longitude(self):
        return self.long
    def get_sightings_by_animal(self):
        animal_dict = {}
        for a in self.sightings:
            if(a.name not in animal_dict.keys()):
                animal_dict[a.name] = []
            animal_dict[a.name].append(a)
        return animal_dict
    def __str__(self):
        return f"Site: {self.name}, Latitude: {self.lat}, Longitude: {self.long}, Sightings: {len(self.sightings)}"
    def plot_site(self, ax):
        anim_sightings = self.get_sightings_by_animal()
        #colors =  plt.cm.Set3.colors 
        colors = distinctipy.get_colors(len(anim_sightings))
        for i, an in enumerate(anim_sightings):
            #bar graph
            for x in range(1,len(anim_sightings[an]) + 1):
                ax.plot(i , x, 'o', marker = anim_sightings[an][0].marker, markersize = 15, color = colors[i])
        ax.set_xticks([i - 0.1 for i,s in enumerate(anim_sightings)], [s for s in anim_sightings] , rotation=80)
        ax.set_ylabel("Number of Sightings")
        ax.set_xlabel("Animal")
        ax.set_title(f"Sightings at {self.name}")
    def plot_animal(self, ax, animal, x_index = 0, color = 'blue', fuzz = False):
        anim_sightings = self.get_sightings_by_animal()
        if(fuzz):
            actual_keys = list(anim_sightings.keys())
            #find all keys that have the animal string in them (case insensitive)
            keys = [x for x in actual_keys if animal.lower() in x.lower()]
            #plot all the keys
            count = 0
            for i, k in enumerate(keys):
                for x in range(1,len(anim_sightings[k]) + 1):
                    count += 1
                    ax.plot(x_index, count , 'o', marker = anim_sightings[k][0].marker, markersize = 15, color = color)
        else:

            if animal in anim_sightings.keys():
                for i ,a in enumerate(anim_sightings[animal]):
                    ax.plot(x_index, i, 'o', marker = a.marker, markersize = 15, color = color)
class Animal:
    def __init__(self, name):
        self.name = name
        if("squirrel" in name.lower() or "chipmunk" in name.lower()):
            tmp_path, attributes = svg2paths('svgs/squirrel-cute.svg')
        elif("coyote" in name.lower()):
            tmp_path, attributes = svg2paths('svgs/coyote-cute.svg')
        elif("raccoon" in name.lower()):
            tmp_path, attributes = svg2paths('svgs/nutria-cute.svg')

        elif("bird" in name.lower() or "thrush" in name.lower() or "jay" in name.lower() or "robin" in name.lower() or "flicker" in name.lower()):
            tmp_path, attributes = svg2paths('svgs/bird-cute.svg')
        elif("otter" in name.lower()):
            tmp_path , attributes = svg2paths('svgs/otter-cute.svg')
        elif("deer" in name.lower()):
            tmp_path , attributes = svg2paths('svgs/deer-cute.svg')
        elif("rat" in name.lower() or "rodent" in name.lower() or "mouse" in name.lower()):
            tmp_path , attributes = svg2paths('svgs/rat-cute.svg')
        elif("cat" in name.lower()):
            tmp_path , attributes = svg2paths('svgs/cat-cute.svg')
        elif("dog" in name.lower()):
            tmp_path , attributes = svg2paths('svgs/dog-cute.svg')
        else:
            tmp_path , attributes = svg2paths('svgs/nutria-cute.svg')

        
        tmp_marker = parse_path(attributes[0]['d'])

        # Apply transformations
        tmp_marker.vertices -= tmp_marker.vertices.mean(axis=0)
        tmp_marker = tmp_marker.transformed(transforms.Affine2D().rotate_deg(180))
        tmp_marker = tmp_marker.transformed(transforms.Affine2D().scale(-1, 1))
        self.marker =  tmp_marker
    def get_animal(self):
        return self.animal
    def get_animal(self):
        return self.name
    def __hash__(self) -> int:
        return hash(self.name)
    def __eq__(self, other) -> bool:
        if(self.name == other.name):
            return True
        return False
class Sighting(Animal):
    def __init__(self, date, animal, site):
        super().__init__(animal)
        self.date = date
        self.site = site

    def get_date(self):
        return self.date


    def get_site(self):
        return self.site
    def get_time_str(self):
        return time.strftime("%d/%m/%Y", self.date)
    def __str__(self):
        return f"Date: {self.get_time_str()}, Animal: {self.name}, Location: {self.site.name}"
    def __eq__(self, other) -> bool:
        return super().__eq__(other)
class SiteList:
    def __init__(self, sites = []):
        self.sites = sites
        self.colors = distinctipy.get_colors(len(sites))
    def add_site(self, site):
        self.sites.append(site)
    def plot_animal(self, animal, fuzz = False):
        fig, ax = plt.subplots()
        
        for i, s in enumerate(self.sites):
            s.plot_animal(ax, animal, i, self.colors[i], fuzz)
        ax.set_xticks([i for i,s in enumerate(self.sites)], [s.name for s in self.sites] , rotation='vertical')
        ax.set_ylabel("Number of Sightings")
        ax.set_xlabel("Site")
        ax.set_title(f"Sightings of {animal}")
        plt.show() 
    def plot_site(self, site):
        fig, ax = plt.subplots()
        site = [s for s in self.sites if s.name == site][0]
        site.plot_site(ax)
        plt.subplots_adjust(bottom=0.35)
        plt.show()
    def get_all_animals(self):
        animals = set()
        for s in self.sites:
            for a in s.sightings:
                animals.add(a.name)
        #remove duplicates
        animals = list(animals)
        return animals
    def plot_all_sites(self):
        for s in self.sites:
            self.plot_site(s.name)