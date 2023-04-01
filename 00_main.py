# Description: This script is the main script of the project
# Import the necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Polygon
import random
import ifcopenshell


def generate_random_room(x_offset=0, y_offset=0):
    width = random.uniform(3, 10)
    height = random.uniform(3, 10)
    coords = [
        (x_offset, y_offset),
        (x_offset, y_offset + height),
        (x_offset + width, y_offset + height),
        (x_offset + width, y_offset),
    ]
    return Polygon(coords)

def plot_floor_plan(rooms, ax):
    for i, room in enumerate(rooms):
        x, y = room.exterior.xy
        ax.plot(x, y)

        area = room.area
        centroid_x, centroid_y = room.centroid.x, room.centroid.y
        ax.text(centroid_x, centroid_y, f"Area {i+1}: {area:.2f} m²", ha='center', fontsize=9, bbox=dict(facecolor='white', alpha=0.5))

    ax.set_aspect('equal', adjustable='box')

fig, axes = plt.subplots(3, figsize=(8, 24))

for i in range(3):
    # Generate random room layouts
    room1 = generate_random_room()
    room2 = generate_random_room(x_offset=room1.bounds[2] + random.uniform(0, 2))
    room3 = generate_random_room(y_offset=room1.bounds[3] + random.uniform(0, 2))

    # Plot the floor plan
    plot_floor_plan([room1, room2, room3], axes[i])


# Load an IFC file
ifc_file = ifcopenshell.open('Duplex_A_20110907.ifc')

# Extract spaces (rooms) from the IFC file
spaces = ifc_file.by_type('IfcSpace')

for space in spaces:
    # Get the global ID, name, and description of the space
    global_id = space.GlobalId
    name = space.Name
    description = space.Description

    print(f"Space: {name}")
    print(f"Description: {description}")

    # Get the properties of the space
    for relDefinesByProperties in space.IsDefinedBy:
        property_set = relDefinesByProperties.RelatingPropertyDefinition
        if property_set.is_a('IfcPropertySet'):
            print(f"Property set: {property_set.Name}")
            for prop in property_set.HasProperties:
                property_name = prop.Name
                property_value = prop.NominalValue.wrappedValue if hasattr(prop.NominalValue, 'wrappedValue') else prop.NominalValue
                print(f"  {property_name}: {property_value}")
        elif property_set.is_a('IfcElementQuantity'):
            # Handle IfcElementQuantity if needed
            pass

    print("\n")


#plt.show()

'''
#Define coordenades of the points, vertices of the polygon
#Define the area of a polygon based on the coordinates
poly = Polygon(zip(verx,very))
#Define the area of the polygon
area = poly.area
#Define the perimeter of the polygon
perimeter = poly.length
#Define the centroid of the polygon
centroid = poly.centroid
#Define the coordinates of the centroid
centroidx = centroid.x
centroidy = centroid.y

'''

#print("The area of the floor plan is: ", area)
#print("The perimeter of the floor plan is: ", perimeter)
