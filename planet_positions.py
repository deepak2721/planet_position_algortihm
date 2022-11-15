from re import M
import this
from time import sleep
from tkinter.tix import tixCommand
from astropy.coordinates import SkyCoord
from sunpy.coordinates import get_body_heliographic_stonyhurst
from astropy.time import Time
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
from datetime import date
from datetime import timedelta, datetime
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import sys


lat = []
long = []
rad = []


def abs_date_time():

    date_time = datetime.today().strftime('%Y-%m-%dT%H:%M:%S') 
    tomorrow = datetime.today() + timedelta(days=i)
    date_time_converted = tomorrow.strftime('%Y-%m-%dT%H:%M:%S') 
    return(date_time_converted)


# def animate(longitude,radius,latitude):
#     fig = plt.figure()
#     ax = Axes3D(fig)
#     plot_geeks = ax.scatter(longitude, radius, color='green')
#     plt.rcParams["figure.figsize"] = (8, 6)
#     plt.xticks([0.1, 0.2, 0.3, 0.4, 0.5])
#     plt.yticks([0.1, 0.2, 0.3, 0.4, 0.5])
#     # plt.zticks([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])

#     ax.set_title("3D plot")
#     ax.set_xlabel('x-axis')
#     ax.set_ylabel('y-axis')
#     ax.set_zlabel('z-axis')
#     plt.show()
#     plt.pause(0.01)
#     # displaying the plot
#     plt.close()


    # plt.plot(longitude,radius,'o') 
    # plt.show()
    # plt.pause(0.1)
  
def animate(longitude,radius, latitude):
   
    plt.xlabel("X-axis")
    plt.ylabel("Y-plot")
    plt.title("Simple bar plot")
    plt.bar(longitude, radius, color = "green")
    plt.pause(0.01)
    
    plt.show()
   

    


def solar_coordinates(abs_date_time):

    obstime = Time(abs_date_time)
    print(abs_date_time)
    # planet_list = ['earth', 'venus', 'mars', 'mercury', 'jupiter', 'neptune', 'uranus']
    # planet_coord = [get_body_heliographic_stonyhurst(this_planet, time=obstime) for this_planet in planet_list]

    planet_list = ['uranus']
    planet_coord = [get_body_heliographic_stonyhurst(this_planet, time=obstime) for this_planet in planet_list]
    # print(planet_coord)


    for this_planet, this_coord in zip(planet_list, planet_coord):
        # coordinates = (np.deg2rad(this_coord.lon),np.deg2rad(this_coord.lon), this_coord.radius) 
        # print(coordinates)
        latitude = np.deg2rad(this_coord.lon)
        lat.append(latitude)

        longitude = np.deg2rad(this_coord.lon)
        long.append(longitude)

        radius =  this_coord.radius
        rad.append(radius)

        # plt.plot(np.deg2rad(this_coord.lon), this_coord.radius, 'o', label=this_planet) 
        # plt.plot(longitude, radius,'o')
        print('LONGITUDE', longitude)
        print('LATITUDE', latitude)
        print('RADIUS', radius)

        animate(longitude,radius, latitude)
        

    # plt.legend(loc='lower left')
    # plt.show()
    # plt.pause(0.3)
    # plt.clf()
    all_coordinates = [longitude, radius, latitude]
    return all_coordinates




for i in range (10):
    # print(abs_date_time()
    a = solar_coordinates(abs_date_time())
    print(a)
    
    
    # animate()
    # animate( solar_coordinates)
