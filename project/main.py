import os.path
from dataio import reprojection
import coordinates
import slice as s
import re
import rasterio
import rasterio.plot as rplt
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import pandas as pd
import numpy as np
import plotly.graph_objects as go


def load_map(file):
    return rasterio.open(file)


def is_decimal(input):
    try:
        float(input)
    except ValueError:
        return False
    else:
        return True


x = input("Coordinate N/Z: ")
y = input("Coordinate E/W: ")
scale_factor = float(input("scale factor: "))

if not is_decimal(x):
    x0 = coordinates.convert_coords_to_decimal(x)
else:
    x0 = float(x)

if not is_decimal(y):
    y0 = coordinates.convert_coords_to_decimal(y)
else:
    y0 = float(y)

reprojection.reproject_map("assets/source/k01.tif")

geomap = s.slice(geomap=load_map("assets/source/k01.tif"), coordX=x0, coordY=y0, scale_factor=scale_factor)
#, index=[f"Y{i}" for i in range(geomap.shape[0])], columns=[f"X{i}" for i in range(geomap.shape[1])]
df = pd.DataFrame(data=geomap)
df.head()

# plotting


fig = plt.figure()
ax = fig.gca(projection="3d")

X = np.arange(0, df.shape[0])
Y = np.arange(0, df.shape[1])
X, Y = np.meshgrid(X, Y)
Z = df

surf = ax.plot_surface(X, Y, Z, cmap="ocean", linewidth=0, antialiased=True)
plt.show()

'''
fig = go.Figure(data=[go.Surface(z=df.values)])

fig.update_layout(title="Test", autosize=True)
fig.show()
'''

