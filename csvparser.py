from Site import Site, Sighting
import numpy as np 
import pandas as pd
df = pd.read_csv("squirel.csv")
sites = []
site_names =df["Site"].unique()
site_indices = df.groupby('Site').apply(lambda group: group.index.tolist())
for i, site in enumerate(site_indices):
    utm_north_value = df.loc[site[0], 'UTMNorth']
    utm_east_value = df.loc[site[0], 'UTMEast']
    #print( site_names[i], site[0], utm_north_value, utm_east_value)
    newsite = Site(site_names[i], utm_north_value, utm_east_value)
    sites.append(newsite)
#site_indices = site_indices[0:1]
for counter, list_of_rows in enumerate(site_indices):
    for row in list_of_rows:
        animal = df.loc[row, 'Species']
        for x in range(1,874):
            was_seen = df.loc[row, f'Day_{x}']
            
            #if was_seen != "NA" or was_seen != "0":
            if was_seen != 0.0 and not pd.isna(df.loc[row, f'Day_{x}']):
                print(was_seen)
                our_site = sites[counter]
                new_sighting = Sighting(animal, f'Day_{x}', our_site )
                our_site.add_sighting(new_sighting)
for s in sites:
    print(s)
    for si in s.sightings:
        print(si)
    #utm_east_value = df.loc[site[0], 'UTMEast']
    #print( site_names[i], site[0], utm_north_value, utm_east_value)
    #newsite = Site(site_names[i], utm_north_value, utm_east_value)
    #sites.append(newsite)
#print(animal)