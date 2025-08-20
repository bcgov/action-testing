
import os

import arcgis
from arcgis.gis import GIS
import geopandas as gpd


username = os.getenv('AGO_USERNAME')
password = os.getenv('AGO_PASSWORD')
portal = os.getenv('AGO_PORTAL')

gis = GIS(url=portal, username=username, password=password)

print("Logged in as: " + username)

search_results = gis.content.search(query="type:Feature Layer", max_items=10)

for item in search_results:
    print(f"Title: {item.title}, Type: {item.type}, ID: {item.id}") 
