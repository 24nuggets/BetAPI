import csv
from decimal import Decimal


def ConvertAmericanOddsToDecimal(americanOdds):

	americanOdds=Decimal(americanOdds)
	
	if americanOdds>0:
		result=(americanOdds/100)+1
	else:
		result=(100/abs(americanOdds))+1

	return str(result)

def WriteToCSV(line,linetype,Sportsbook1,Team1,Point1,Line1,Sportsbook2,Team2,Point2,Line2,profit):
	with open('output.csv', 'a') as file:
	    writer = csv.writer(file)
	   
	    writer.writerow([line,linetype,Sportsbook1,Team1,Point1,Line1,Sportsbook2,Team2,Point2,Line2,profit])
	    