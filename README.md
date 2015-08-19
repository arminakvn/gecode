### how to use python to programmatically geocode addresses from a .csv file using Google Maps Geocoding API
See [Google Geocoding API](https://developers.google.com/maps/documentation/geocoding/intro).

Setup the [Google APIs Client Library for Python](https://developers.google.com/api-client-library/python/start/get_started) and activate a proper api-key
This code requires the  `simplejson`   library which can be installed with [pip](https://pypi.python.org/pypi/pip):

```
pip install simplejson


```   

Run it with:  

```
python geocode -i <input.csv> -o <output.csv>

```
__For example  __
in command line:

```
python geocode.py -i OutputKarimAãnouz.csv -o OutputKarimAãnouzGeo.csv

```