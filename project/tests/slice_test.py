import rasterio
import rasterio.plot as rplt
from rasterio.windows import Window


# , "w", driver="GTiff", width=500, height=300, count=1, dtype=img_band1.dtype, crs="EPSG:4326"

with rasterio.open("../assets/output/reprojection.tif", crs="EPSG:4326") as src:
    width = src.shape[1]
    height = src.shape[0]
    print(width / 2)
    print(height / 2)
    print(src.shape)
    w = src.read(1, window=rasterio.windows.from_bounds(4.45, 51.48, 4.451, 51.481, src.transform))

print(w.shape)
rasterio.plot.show(w, cmap="terrain")