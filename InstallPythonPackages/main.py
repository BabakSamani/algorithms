#!/usr/local/bin python2

import os

if __name__ == '__main__':

    packages = ['attrs', 'beautifulsoup4', 'certifi', 'characteristic', 'chardet', 'Click', 'bs4', 'service-identity',
                'click-plugins', 'cligj', 'DateTime', 'decorator', 'defer', 'duplicity', 'ecdsa', 'pygobject',
                'enum34', 'Fiona', 'Flask', 'Flask-Caching', 'GDAL', 'geojson', 'html5lib', 'httplib2', 'idna',
                'ipython', 'itsdangerous', 'Jinja2', 'lockfile', 'lxml', 'MarkupSafe', 'matplotlib', 'mock', 'munch',
                'ndg-httpsclient', 'nose', 'numpy', 'oauthlib', 'PAM', 'paramiko', 'pexpect', 'Pillow', 'pymongo',
                'piston-mini-client', 'psycopg2', 'pyasn1', 'pyasn1-modules', 'pycrypto', 'pycups', 'Pygments',
                'PyOpenGL', 'pyOpenSSL', 'pyparsing', 'pypi-install', 'pyproj', 'pyserial', 'pyspatialite',
                'python-dateutil', 'python-dotenv', 'pytz', 'pyxdg', 'requests', 'schedule', 'selenium', 'setuptools',
                'Shapely', 'simplegeneric', 'six', 'urllib3', 'Werkzeug', 'wxPython', 'zope.interface' ]

    for p in packages:
        os.system('pip install ' + p)

