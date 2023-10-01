from Site import Site, Sighting, SiteList
import numpy as np 
import pandas as pd
import pickle
import random
import time 
def create_sites_from_csv(filename, start_time = "1/1/2022"):
    df = pd.read_csv(filename)
    sites = []
    site_names =df["Site"].unique()
    site_indices = df.groupby('Site').apply(lambda group: group.index.tolist())
    for i, site in enumerate(site_indices):
        utm_north_value = df.loc[site[0], 'Latitude']
        utm_east_value = df.loc[site[0], 'Longitude']
        #print( site_names[i], site[0], utm_north_value, utm_east_value)
        newsite = Site(site_names[i], lat = utm_north_value, long = utm_east_value)
        sites.append(newsite)
    #site_indices = site_indices[0:1]
    start_time = time.strptime(start_time, "%m/%d/%Y")
    for counter, list_of_rows in enumerate(site_indices):
        for row in list_of_rows:
            animal = df.loc[row, 'Species']
            #the number of coulmns - 5 is the number of days
            #  
            days = len(df.columns) - 5
            for x in range(1,days):
                was_seen = df.loc[row, f'Day_{x}']

                #if was_seen != "NA" or was_seen != "0":
                if was_seen != 0.0 and not pd.isna(df.loc[row, f'Day_{x}']):
                    our_site = sites[counter]
                    sight_date = time.mktime(start_time) + (x * 86400)
                    sight_date = time.localtime(sight_date)
                    new_sighting = Sighting(animal= animal, date= sight_date, site= our_site )
                    our_site.add_sighting(new_sighting)
        #utm_east_value = df.loc[site[0], 'UTMEast']
        #print( site_names[i], site[0], utm_north_value, utm_east_value)
        #newsite = Site(site_names[i], utm_north_value, utm_east_value)
        #sites.append(newsite)
    return sites
sites = create_sites_from_csv("PB3_spsu.csv")
sites = SiteList(sites)
with open("tst.pickle" , "wb") as f:
    pickle.dump(sites, f )
#print(animal)