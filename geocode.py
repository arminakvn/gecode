# intall simplejson: pip install simplejson
# command line: python geocode.py -i <inpout csv> -o <output csv>
import sys, getopt
import simplejson, urllib
from read_csv_to_dict import read_csv, write_csv

def main(argv):	
	inputfile = ''
	outputfile = ''
	try:
		opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
	except getopt.GetoptError:
		print 'geocode.py -i <inputfile> -o <outputfile>'
		sys.exit(2)
	# if using an api key it should be added to the function's arguments and passed when called
	def geocodeLocations(address, **geo_args):
	    geo_args.update({
	        'address': address#, 
	        #'key' : key
	    })
	    url = GEOCODE_BASE_URL + '?' + urllib.urlencode(geo_args)
	    result = simplejson.load(urllib.urlopen(url))
	    print result['results'][0]['geometry']['location']
	    if result['status'] == 'OK':
	    	# here could be some filters that check for location type such as proximity level ...
	    	return result['results'][0]['geometry']['location']
	for opt, arg in opts:
		if opt == '-h':
			print 'geocode.py -i <inputfile> -o <outputfile>' 
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile = arg
		elif opt in ("-o", "--ofile"):
			outputfile = arg
	print 'Input file is ', inputfile
	print 'Output file is ', outputfile
	GEOCODE_BASE_URL = 'http://maps.googleapis.com/maps/api/geocode/json'
	raw_matrix = read_csv(inputfile)
	org_dist = ""
	for each_line in raw_matrix:
		# it seems that Organization could also be used, 
		# maybe concatinated with some other info, for now filter for Location
		if each_line['Tag Type'] == 'Location':
			address = each_line['Tag Value'] 
			latlng = geocodeLocations(address)
		else:
			latlng = ''
		each_line['latlng'] = str(latlng).replace('{', '').replace('}', '')
	
	write_csv(raw_matrix, outputfile)

if __name__ == '__main__':
		main(sys.argv[1:])


