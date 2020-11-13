import rasterio
import rasterio.warp as warp
import os

def update_bounding_boxes():
    bounding_boxes = {}
    with open("assets/boundingboxes.txt", "r") as bounds:
        lines = bounds.readlines()
        for n in lines:
            x = n.split()
            # k-file: (left, right, top, bottom)
            bounding_boxes[x[0]] = (x[1], x[2], x[3], x[4])
    return bounding_boxes

def reproject_map(file):
    if not os.path.isfile(file):
        reproject("assets/tif/DSM_k01.tif", file)
        filename = os.path.basename(file)
        filename = os.path.splitext(filename)[0]
        src = rasterio.open(file)
        boundaries = src.bounds
        with open("assets/boundingboxes.txt", "r+") as bounds:
            lines = bounds.readlines()
            for n in lines:
                x = n.split()
                if x[0] == filename:
                    return
            lines.append(f"{filename} {boundaries.left} {boundaries.right} {boundaries.top} {boundaries.bottom}\n")
            bounds.writelines(lines)


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

