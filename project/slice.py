import rasterio
import rasterio.plot as rplt
from rasterio.windows import Window

offset = 0.0001

def slice(geomap=None, coordX=0.0, coordY=0.0, scale_factor=5.0):
    coord_offset = offset * scale_factor
    bound_x0 = coordX - coord_offset
    bound_x1 = coordX + coord_offset
    bound_y0 = coordY - coord_offset
    bound_y1 = coordY + coord_offset
    return geomap.read(1, window=rasterio.windows.from_bounds(bound_y0, bound_x0, bound_y1, bound_x1, geomap.transform))