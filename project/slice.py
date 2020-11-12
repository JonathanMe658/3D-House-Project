import rasterio
import rasterio.plot as rplt
from rasterio.windows import Window

coord_offset = 0.0005

def slice(geomap=None, coordX=0.0, coordY=0.0):
    bound_x0 = coordX - coord_offset
    bound_x1 = coordX - coord_offset
    bound_y0 = coordY - coord_offset
    bound_y1 = coordY - coord_offset
    return geomap.read(1, window=rasterio.windows.from_bounds(bound_y0, bound_x0, bound_y1, bound_x1, geomap.transform))