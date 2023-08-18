import pickle
import matplotlib.pyplot as plt
from Site import Site, Sighting, Animal
sites = []
with open("tst.pickle" , "rb") as f:
    sites = pickle.load(f)
#fig, ax = plt.subplots()
for i,s in enumerate(sites):
    if(len(s) > 0):
        plt.plot(i * 30, len(s), 'o', marker = s.sightings[0].marker, markersize = 30)
    print(s)
an = Animal("squirrel")

plt.show()