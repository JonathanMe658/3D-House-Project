import rasterio
from rasterio.windows import Window


def slicer(geomap, coordX: float = 0.0, coordY: float = 0.0, scale_factor: float = 8.0, offset: float = 0.000006577216521967903):
    coord_offset = offset * scale_factor
    bound_x0 = coordX - coord_offset
    bound_x1 = coordX + coord_offset
    bound_y0 = coordY - coord_offset
    bound_y1 = coordY + coord_offset
    return geomap.read(1, window=rasterio.windows.from_bounds(bound_x0, bound_y0, bound_x1, bound_y1, geomap.transform))
