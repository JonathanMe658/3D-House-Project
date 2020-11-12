import rasterio
import rasterio.plot as rplt
from rasterio.windows import Window
from rasterio.warp import calculate_default_transform, reproject, Resampling
import numpy as np

# , "w", driver="GTiff", width=500, height=300, count=1, dtype=img_band1.dtype, crs="EPSG:4326"


dst_crs = "EPSG:4326"# {"init": "EPSG:4326"}
with rasterio.open("assets/tif/DSM_k01.tif") as src:

    transform, width, height = calculate_default_transform(src.crs, dst_crs, src.width, src.height, *src.bounds)
    kwargs = src.meta.copy()
    kwargs.update({
        "crs": dst_crs,
        "transform": transform,
        "width": width,
        "height": height
    })

    dst = np.zeros(src.read().shape, src.read().dtype)

    for i in range(1, src.count + 1):
        reproject(
            source=rasterio.band(src, i),
            destination=rasterio.band(dst, i),
            src_transform=src.transform,
            src_crs=src.crs,
            dst_transform=transform,
            dst_crs=dst_crs,
            resampling=Resampling.nearest)


    print(src.shape)
    w = src.read(1, window=rasterio.windows.from_bounds(4.45, 51.48, 4.451, 51.481, src.transform))

print(w.shape)
rasterio.plot.show(w, cmap="terrain")

