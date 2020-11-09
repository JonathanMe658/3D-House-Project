import geopandas as gpd
import matplotlib.pyplot as plt
import rasterio
import rasterio.plot as rplt

# import and plotting DSM geoTIFF file

fp = r"assets/DSM/DSM_k02.tif"
img = rasterio.open(fp)
rplt.show(img, cmap="terrain")

# import and plotting DTM geoTIFF file

fp2 = r"assets/DTM/DTM_k01.tif"
img2 = rasterio.open(fp2)
rplt.show(img2)

# import and plotting terrain shape file

hmap = gpd.read_file("assets/DTM/DTM_k01.shp")
hmap.plot()
plt.show()

# import and plotting surface shape file
bmap = gpd.read_file("assets/DSM/DSM_k01.shp")
print(bmap.head(5))
bmap2 = gpd.read_file("assets/DSM/DSM_k02.shp")
bmap3 = gpd.read_file("assets/DSM/DSM_k03.shp")
bmap4 = gpd.read_file("assets/DSM/DSM_k04.shp")

fig, ax= plt.subplots(1)
bmap.plot(ax=ax)
bmap2.plot(ax=ax)
bmap3.plot(ax=ax)
bmap4.plot(ax=ax)
plt.show()