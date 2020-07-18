#!/usr/bin/env python
# coding: utf-8

# # GeoVisualization in Python
# 
# In this notbook, there is practical implimentations of how to create geographic visualizations that are useful for data science projects.

# In[1]:


import numpy as np  # useful for many scientific computing in Python
import pandas as pd # primary data structure library


# # Step 1: Generating basic maps with Folium.

# In[2]:


get_ipython().system('pip install folium')
import folium
#Folium is a powerful Python library that helps you create several types of Leaflet maps. 
#The fact that the Folium results are interactive makes this library very useful for dashboard building.


# In[3]:


# define the world map
world_map = folium.Map()

# display world map
world_map


# In[4]:


# define the world map centered around Canada with a low zoom level
world_map = folium.Map(location=[20.2, -1.4], zoom_start=4)

# display world map
world_map


# In[5]:


# define the world map in Africa
world_map = folium.Map(location=[20.2, -1.4], zoom_start=6)

# display world map
world_map


# # Step 3: Generating Stamen Toner Maps and Stamen Terrain Maps.

# Stamen Toner Maps
# 
# These are high-contrast B+W (black and white) maps. They are perfect for data mashups and exploring river meanders and coastal zones.

# In[6]:


# create a Stamen Toner map of Africa
world_map = folium.Map(location=[20.2, -1.4], zoom_start=4, tiles='Stamen Toner')

# display map
world_map


# Stamen Terrain Maps
# 
# These are maps that feature hill shading and natural vegetation colors. They showcase advanced labeling and linework generalization of dual-carriageway roads.

# In[7]:


# create a Stamen Toner map of Africa
world_map = folium.Map(location=[20.2, -1.4], zoom_start=4, tiles='Stamen Terrain')

# display map
world_map


# # Step 4: Generating Stamen Toner Maps and Stamen Terrain Maps.

# Visualizing a city on the world map

# In[8]:


# New Delhi latitude and longitude values
latitude = 28.644800
longitude = 77.216721
# create map and display it
delhi_map = folium.Map(location=[latitude, longitude], zoom_start=12)

# display the map of New Delhi
delhi_map


# # Step 5: Solving a short project using Geographical Maps.

# Maps with Markers

# In[9]:


#Let's download and import the data on police department incidents using pandas
# download the dataset and read it into pandas dataframe

df_incidents = pd.read_csv('https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DV0101EN/labs/Data_Files/Police_Department_Incidents_-_Previous_Year__2016_.csv')

print('Dataset downloaded and read into a pandas dataframe!')


# In[10]:


#Let's take a look at the first five items in our dataset.
df_incidents.head()


# In[11]:


#Let's find out how many entries there are in our dataset.
df_incidents.shape


# In[12]:


#So the dataframe consists of 150,500 crimes, which took place in the year 2016.
#In order to reduce computational cost, let's just work with the first 100 incidents in this dataset.
# get the first 100 crimes in the df_incidents dataframe
limit = 100
df_incidents = df_incidents.iloc[0:limit, :]


# In[13]:


#Let's confirm that our dataframe now consists only of 100 crimes.
df_incidents.shape


# In[14]:


#Now that we reduced the data a little bit, let's visualize where these crimes took place in the city of San Francisco.
# We will use the default style and we will initialize the zoom level to 12.
# San Francisco latitude and longitude values
latitude = 37.77
longitude = -122.42


# In[15]:


# create map and display it
sanfran_map = folium.Map(location=[latitude, longitude], zoom_start=12)

# display the map of San Francisco
sanfran_map


# In[16]:


# Now let's superimpose the locations of the crimes onto the map.
# The way to do that in Folium is to create a feature group with its own features and style
# and then add it to the sanfran_map.
# instantiate a feature group for the incidents in the dataframe
incidents = folium.map.FeatureGroup()

# loop through the 100 crimes and add each to the incidents feature group
for lat, lng, in zip(df_incidents.Y, df_incidents.X):
    incidents.add_child(
        folium.CircleMarker(
            [lat, lng],
            radius=5, # define how big you want the circle markers to be
            color='yellow',
            fill=True,
            fill_color='blue',
            fill_opacity=0.6
        )
    )

# add incidents to map
sanfran_map.add_child(incidents)


# In[17]:


# we can also add some pop-up text that would get displayed when we hover over a marker. 
# Let's make each marker display the category of the crime when hovered over.
# instantiate a feature group for the incidents in the dataframe
incidents = folium.map.FeatureGroup()

# loop through the 100 crimes and add each to the incidents feature group
for lat, lng, in zip(df_incidents.Y, df_incidents.X):
    incidents.add_child(
        folium.CircleMarker(
            [lat, lng],
            radius=5, # define how big we want the circle markers to be
            color='yellow',
            fill=True,
            fill_color='blue',
            fill_opacity=0.6
        )
    )

# add pop-up text to each marker on the map
latitudes = list(df_incidents.Y)
longitudes = list(df_incidents.X)
labels = list(df_incidents.Category)

for lat, lng, label in zip(latitudes, longitudes, labels):
    folium.Marker([lat, lng], popup=label).add_to(sanfran_map)    
    
# add incidents to map
sanfran_map.add_child(incidents)


# In[18]:


# we can remove location markers and just add the text to the circle markers themselves as follows:
# create map and display it
sanfran_map = folium.Map(location=[latitude, longitude], zoom_start=12)

# loop through the 100 crimes and add each to the map
for lat, lng, label in zip(df_incidents.Y, df_incidents.X, df_incidents.Category):
    folium.CircleMarker(
        [lat, lng],
        radius=5, # define how big we want the circle markers to be
        color='yellow',
        fill=True,
        popup=label,
        fill_color='blue',
        fill_opacity=0.6
    ).add_to(sanfran_map)

# show map

