from Site import Site, Sighting, SiteList
import argparse
import numpy as np 
import pandas as pd
import pickle
import random
import time 
def create_sites_from_csv(filename, start_time = "1/1/2022"):
    df = pd.read_csv(filename, skiprows=3)
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
        
    return sites


def main():
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description="Parse a file name and an optional start date")

    # Add argument for the file name
    parser.add_argument("file_name", help="Name of the file to be processed")

    # Add an optional argument for the start date
    parser.add_argument("-d", "--start_date", help="Optional start date in mm/dd/yy format")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Access the file name and start date
    file_name = args.file_name
    start_date = args.start_date

    return file_name,start_date


if __name__ == "__main__":
    fname, startdate = main()
    if(startdate != None):
        sites = create_sites_from_csv(fname, startdate)
    else:
        sites = create_sites_from_csv(fname)

    sites = SiteList(sites)
    with open("tst.pickle" , "wb") as f:
        pickle.dump(sites, f )
    