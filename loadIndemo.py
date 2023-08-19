import pickle
import matplotlib.pyplot as plt
from Site import Site, Sighting, Animal
sites = []
with open("tst.pickle" , "rb") as f:
    siteL = pickle.load(f)
sites = siteL.sites
#siteL.plot_animal("Squirrel" , True )
#print(siteL.get_all_animals())
siteL.plot_all_sites()
"""
for i,s in enumerate(sites):
    if(len(s) > 0):
        fig, ax = plt.subplots()
        s.plot_site(ax) 
        plt.show()
        for x in s.sightings:
            print(x)
"""