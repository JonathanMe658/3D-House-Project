import pandas as pd
import seaborn as sns
import numpy as np
import geopandas as gpd
import rasterio
import rasterio.plot as rplt
import rasterio.coords as co
import matplotlib.pyplot as plt
from rasterio.windows import Window


fp = r"assets/output/reprojection.tif"
img = rasterio.open(fp)
coords = (51.46, 4.5)
print(img.crs)
print(img.count)
print(img.bounds.left)
print(img.shape)
# rplt.show(img, cmap="terrain")

img_band1 = img.read(1).astype("float64")
# rplt.show(img_band1, cmap="terrain")
print(img_band1[6000:6010, 7000:7001])

print(img.xy(1, 5))

dx = (img.bounds.right - img.bounds.left) / img.shape[0]
dy = (img.bounds.top - img.bounds.bottom) / img.shape[1]

x0 = int(((coords[0] - img.bounds.left) / dx) + 100)
x1 = int(((coords[0] - img.bounds.left) / dx) - 100)
y0 = int(((coords[0] - img.bounds.bottom) / dy) + 100)
y1 = int(((coords[0] - img.bounds.bottom) / dy) - 100)

print(dx)
print(dy)
print(x0)
print(x1)
print(y0)
print(y1)
write_window = Window.from_slices((5800, 6000), (10000, 10200))

with rasterio.open("assets/output/sliced.tif", "w", driver="GTiff", width=500, height=300, count=1, dtype=img_band1.dtype, crs="EPSG:4326") as dst:
    dst.write(img_band1, indexes=1, window=Window(50, 30, 250, 150))

img.close()

fp2 = r"assets/output/sliced.tif"
img2 = rasterio.open(fp2)
rplt.show(img2, cmap="terrain")