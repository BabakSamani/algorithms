import json
from pyproj import Proj, transform
import shapefile
import fiona
import shapely
import geojson


def main():
    # esri102686 = Proj(
    #     "+proj=lcc +lat_1=41.71666666666667 +lat_2=42.68333333333333 +lat_0=41 +lon_0=-71.5 +x_0=200000 +y_0=750000.0000000001 +datum=NAD83 +units=us-ft+no_defs",
    #     preserve_units=True)
    buffer = []
    input_shape_file = './Input_data/adams_tvc/adams_tvc.shp'
    shape_file = fiona.open(input_shape_file)
    inProj = Proj(shape_file.crs)
    outProj = Proj("+init=EPSG:4326", preserve_units=True)

    shp = shapefile.Reader(input_shape_file)
    fields = shp.fields[1:]
    field_names = [field[0] for field in fields]

    for sr in shp.shapeRecords():
        attr = dict(zip(field_names, sr.record))
        geom = sr.shape.__geo_interface__

        print geom['coordinates']


if __name__ == "__main__":
    main()
