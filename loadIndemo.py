import pickle
import matplotlib.pyplot as plt
from Site import Site, Sighting, Animal
sites = []
with open("tst.pickle" , "rb") as f:
    sites = pickle.load(f)
fig, ax = plt.subplots()
for i,s in enumerate(sites):
    if(len(s) > 0):
        anim_sightings = s.get_sightings_by_animal()
        for an in anim_sightings:
            print(s, anim_sightings[an])
            ax.plot(i * 30, len(anim_sightings[an]), 'o', marker = anim_sightings[an][0].marker, markersize = 15)
           
an = Animal("squirrel")
ax.set_xticks([i * 30 for i,s in enumerate(sites)])
ax.set_xticklabels([s.name for s in sites], rotation='vertical')
plt.show()