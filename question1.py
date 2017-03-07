# Retrieve the weather station data from the url below and print the total
# precipitation in February 2007 as reported by the data.
# https://www.wunderground.com/history/airport/KNUQ/2007/1/1/CustomHistory.html?dayend=31&monthend=12&yearend=2007&req_city=NA&req_state=NA&req_statename=NA&format=1
# Implement the solution entirely in python

import urllib2

def main():

	# scrapes given webpage and sets weather_data equal to the source code
        weather_data = urllib2.urlopen("https://www.wunderground.com/history/airport/KNUQ/2007/1/1/CustomHistory.html?dayend=31&monthend=12&year\end=2007&req_city=NA&req_state=NA&req_statename=NA&format=1")

	# In each line of source code looks for February, 2007 and then find the precipitation by day and adds them together
	dates = "2007-2"
	curr_precip = []
	for line in weather_data:
		if dates in line:
			curr_precip = line.split(",")	
			print curr_precip[20]


if __name__ == "__main__":
	main()


                                                                                            
