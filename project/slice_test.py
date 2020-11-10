import numpy as np
import rasterio
from rasterio.windows import Window

with rasterio.open("assets/output/reprojection.tif", "r") as src:
    b, g, r = (src.read(k) for k in (1, 2, 3))

write_window = Window.from_slices((30, 269), (50, 313))

with rasterio.open("assets/output/sliced.tif", "w", driver="GTiff") as dst:
    for k, arr in [(1, b), (2, g), (3, r)]:
        dst.write(arr, indexes=k, window=write_window)


