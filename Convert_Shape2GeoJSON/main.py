#!usr/local/bin

from pyproj import Proj, transform
import shapefile
import fiona
import shapely
import geojson


def main():
    # esri102686 = Proj(
    #     "+proj=lcc +lat_1=41.71666666666667 +lat_2=42.68333333333333 +lat_0=41 +lon_0=-71.5 +x_0=200000 +y_0=750000.0000000001 +datum=NAD83 +units=us-ft+no_defs",
    #     preserve_units=True)
    geoJSON = {'type': "FeatureCollection", 'features': []}
    features = []

    input_shape_file = './Input_data/adams_tvc/adams_tvc.shp'
    shape_file = fiona.open(input_shape_file)
    inProj = Proj(shape_file.crs)
    outProj = Proj("+init=EPSG:4326", preserve_units=True)

    shp = shapefile.Reader(input_shape_file)
    fields = shp.fields[1:]
    field_names = [field[0] for field in fields]

    for sr in shp.shapeRecords():
        props = dict(zip(field_names, sr.record))
        geom = sr.shape.__geo_interface__
        feature = {'type': "Feature", 'properties': props}
        if geom['type'] == 'LineString':
            l_str = []
            for coords in geom['coordinates']:
                x = coords[0]
                y = coords[1]
                lat_lng = transform(inProj, outProj, x, y)
                l_str.append([lat_lng[0], lat_lng[1]])
            feature['geometry'] = {'type': geom['type'], 'coordinates': l_str}
        if geom['type'] == 'MultiLineString':
            ml_str = []
            for lineCoords in geom['coordinates']:
                l_str = []
                for coords in lineCoords:
                    x = coords[0]
                    y = coords[1]
                    lat_lng = transform(inProj, outProj, x, y)
                    l_str.append([lat_lng[0], lat_lng[1]])
                ml_str.append(l_str)
            feature['geometry'] = {'type': geom['type'], 'coordinates': ml_str}

        features.append(feature)
    geoJSON['features'] = features

    # Write the results into a GeoJSON file
    output_file = "./Output_data/adams_tvc.geojson"
    with open(output_file, 'w') as out_file:
        geojson.dump(geoJSON, out_file)


if __name__ == "__main__":
    main()
