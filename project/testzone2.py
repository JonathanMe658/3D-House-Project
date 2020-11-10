import fiona
import rasterio
import rasterio.mask
import matplotlib.pyplot as plt

# with fiona.open("assets/DSM/DSM_k01.shp", "r") as shapefile:
#    shapes = [feature["geometry"] for feature in shapefile]


with rasterio.open("assets/DSM/DSM_k01.tif") as src:
    out_image, out_transform = rasterio.mask.mask(src, shapes, crop=True)
    out_meta = src.meta

plt.imshow(out_image)
plt.show()