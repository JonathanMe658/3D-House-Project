import rasterio
import rasterio.warp as warp
import coordinates
import os
from exceptions import LocationException

extensions = ".tiff"


def update_bounding_boxes():
    bounding_boxes = {}
    with open("assets/boundingboxes.txt", "r") as bounds:
        lines = bounds.readlines()
        if len(lines) == 0:
            return
        for n in lines:
            x = n.split()
            # k-file: (left, right, top, bottom)
            bounding_boxes[x[0]] = (float(x[1]), float(x[2]), float(x[3]), float(x[4].replace("\n", "")))
    return bounding_boxes


def reproject_map(srcpath, destpath):
    reproject(srcpath, destpath)
    filename = os.path.basename(srcpath)
    dst = rasterio.open(destpath)
    boundaries = dst.bounds
    with open("assets/boundingboxes.txt", "r+") as bounds:
        lines = bounds.readlines()
        for n in lines:
            x = n.split()
            if x[0] == filename:
                return
        lines.append(f"{filename} {boundaries.left} {boundaries.right} {boundaries.top} {boundaries.bottom}\n")
        bounds.seek(0, 0)
        bounds.writelines(lines)
    dst.close()
    return boundaries


def reproject(srcpath, dstpath):
    with rasterio.open(srcpath, "r") as src:
        dst_crs = "EPSG:4326"
        transform, width, height = warp.calculate_default_transform(src.crs, dst_crs, src.width, src.height, *src.bounds)
        kwargs = src.meta.copy()
        kwargs.update({
            "crs": dst_crs,
            "transform": transform,
            "width": width,
            "height": height
        })

        with rasterio.open(dstpath, "w", **kwargs) as dst:
            for i in range(1, src.count + 1):
                warp.reproject(
                    source=rasterio.band(src, i),
                    destination=rasterio.band(dst, i),
                    src_transform=src.transform,
                    src_crs=src.crs,
                    dst_transform=transform,
                    dst_crs=dst_crs,
                    resampling=warp.Resampling.nearest)


def load_map(coordX, coordY, scale=5.0, sourcepath="assets/source/", tifpath="assets/tif/"):
    bounds = update_bounding_boxes()
    if bounds == None:
        bounds = {}
    filename = ""
    check_directory = True
    for n in bounds.keys():
        if coordinates.is_in_boundaries(bounds[n], coordX, coordY, scale):
            check_directory = False
            filename = n
    if check_directory:
        if not os.path.exists(sourcepath) and not os.path.exists(tifpath):
            return None
        for file in os.listdir(tifpath):
            if not file.endswith(".tif"):
                continue
            if file not in bounds.keys():
                boundaries = reproject_map(f"{tifpath}{file}", f"{sourcepath}{file}")
                if coordinates.is_in_boundaries((boundaries.left, boundaries.right, boundaries.top, boundaries.bottom), coordX, coordY, scale):
                    filename = file
                    break
    if not filename:
        raise LocationException(f"Cannot find location! Coordinates {coordX}, {coordY} are missing from the available data.")
    return rasterio.open(f"{sourcepath}{filename}")

