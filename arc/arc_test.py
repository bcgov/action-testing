
import os

import arcgis
from arcgis.gis import GIS
import geopandas as gpd


username = os.getenv('AGO_USERNAME')
password = os.getenv('AGO_PASSWORD')
portal = os.getenv('AGO_PORTAL')

gis = GIS(url=portal, username=username, password=password)

print(username)
print(f"logged in as {gis.properties.user.username} to {gis.properties.name} at {gis.properties.url}")
print("Successfully imported arcgis and geopandas")