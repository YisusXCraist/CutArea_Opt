# Description: This script is the main script of the project
# Import the necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Polygon



#Define the area of a Floor Plan
verx = [0, 0, 10, 10]
very = [0, 10, 10, 0]
#Define coordenades of the points, vertices of the polygon
#Define the area of a polygon based on the coordinates
poly = Polygon(zip(verx,very))
