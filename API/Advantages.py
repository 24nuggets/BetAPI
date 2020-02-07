from decimal import Decimal
from Utilities import WriteToCSV


def CheckForArbritage(sportsbook1,sportsbook2, linetype, team1, line1,team2, line2):
	
	line1=Decimal(line1)
	line2=Decimal(line2)
	result=((1/line1)*100)+((1/line2)*100)
	
	#print(linetype+" "+sportsbook1+" "+team1+" "+str(line1)+" "+sportsbook2+" "+team2+" "+str(line2))
	if (result<100):
		profitpercent=((1/(result/100))-1)*100
		if profitpercent>0:
			WriteToCSV("Arb",linetype,sportsbook1,team1,"N/A",line1,sportsbook2,team2,"N/A",line2,profitpercent)
			print(linetype+" "+sportsbook1+" "+team1+" "+str(line1)+" "+sportsbook2+" "+team2+" "+str(line2))
			print("Profit Percentage: "+str(profitpercent))
			
	

def CheckForMiddlesSpread(sport,sportsbook1,sportsbook2, linetype, team1, point1, line1,team2, point2, line2):
	line1=Decimal(line1)
	line2=Decimal(line2)
	point1=Decimal(point1)
	point2=Decimal(point2)

	dif=point1+point2
	result=((1/line1)*100)+((1/line2)*100)
	profitpercent=((1/(result/100))-1)*100
	dif2=result-100

	#print("Spread "+linetype+" "+sportsbook1+" "+team1+" "+str(point1)+" "+str(line1)+" "+sportsbook2+" "+team2+" "+str(point2)+" "+str(line2))
	# if dif2<=0 and dif>=0:
	# 	print("Polish Middle Spread "+linetype+" "+sportsbook1+" "+team1+" "+str(point1)+" "+str(line1)+" "+sportsbook2+" "+team2+" "+str(point2)+" "+str(line2))
	# 	print("Profit Percentage: "+str(profitpercent))
	# 	WriteToCSV("Spread Middle",linetype,sportsbook1,team1,point1,line1,sportsbook2,team2,point2,line2)
	# elif profitpercent>=3:
	# 	print("Middle Spread "+linetype+" "+sportsbook1+" "+team1+" "+str(point1)+" "+str(line1)+" "+sportsbook2+" "+team2+" "+str(point2)+" "+str(line2))
	# 	print("Profit Percentage: "+str(profitpercent))
	# 	WriteToCSV("Spread Middle",linetype,sportsbook1,team1,point1,line1,sportsbook2,team2,point2,line2)
	if dif>=.5:
		if sport=="football" or sport=="basketball":
			if profitpercent>-.5:
				print("Spread "+linetype+" "+sportsbook1+" "+team1+" "+str(point1)+" "+str(line1)+" "+sportsbook2+" "+team2+" "+str(point2)+" "+str(line2))
				print("Profit Percentage: "+str(profitpercent))
				WriteToCSV("Spread Middle",linetype,sportsbook1,team1,point1,line1,sportsbook2,team2,point2,line2,profitpercent)
		elif profitpercent>-5:
			print("Spread "+linetype+" "+sportsbook1+" "+team1+" "+str(point1)+" "+str(line1)+" "+sportsbook2+" "+team2+" "+str(point2)+" "+str(line2))
			print("Profit Percentage: "+str(profitpercent))
			WriteToCSV("Spread Middle",linetype,sportsbook1,team1,point1,line1,sportsbook2,team2,point2,line2,profitpercent)
	elif dif>=1:
		if dif2<=6:
			print("Spread "+linetype+" "+sportsbook1+" "+team1+" "+str(point1)+" "+str(line1)+" "+sportsbook2+" "+team2+" "+str(point2)+" "+str(line2))
			print("Profit Percentage: "+str(profitpercent))
			WriteToCSV("Spread Middle",linetype,sportsbook1,team1,point1,line1,sportsbook2,team2,point2,line2,profitpercent)
	elif dif>=1.5:
		if dif2<=9:
			print("Spread "+linetype+" "+sportsbook1+" "+team1+" "+str(point1)+" "+str(line1)+" "+sportsbook2+" "+team2+" "+str(point2)+" "+str(line2))
			print("Profit Percentage: "+str(profitpercent))
			WriteToCSV("Spread Middle",linetype,sportsbook1,team1,point1,line1,sportsbook2,team2,point2,line2,profitpercent)
	elif dif>=2:
		if dif2<=12:
			print("Spread "+linetype+" "+sportsbook1+" "+team1+" "+str(point1)+" "+str(line1)+" "+sportsbook2+" "+team2+" "+str(point2)+" "+str(line2))
			print("Profit Percentage: "+str(profitpercent))
			WriteToCSV("Spread Middle",linetype,sportsbook1,team1,point1,line1,sportsbook2,team2,point2,line2,profitpercent)
	elif dif>=2.5:
		print("Spread "+linetype+" "+sportsbook1+" "+team1+" "+str(point1)+" "+str(line1)+" "+sportsbook2+" "+team2+" "+str(point2)+" "+str(line2))
		print("Profit Percentage: "+str(profitpercent))
		WriteToCSV("Spread Middle",linetype,sportsbook1,team1,point1,line1,sportsbook2,team2,point2,line2,profitpercent)

def CheckForMiddlesTotals(sport,sportsbook1,sportsbook2, linetype, team1, OverPoints, OverLine,team2, UnderPoints, UnderLine):
	OverLine=Decimal(OverLine)
	OverPoints=Decimal(OverPoints)
	UnderLine=Decimal(UnderLine)
	UnderPoints=Decimal(UnderPoints)

	dif=UnderPoints-OverPoints
	result=((1/OverLine)*100)+((1/UnderLine)*100)
	profitpercent=((1/(result/100))-1)*100
	dif2=result-100
	#print("Totals "+linetype+" "+sportsbook1+" "+team1+" "+str(OverPoints)+" "+str(OverLine)+" "+sportsbook2+" "+team2+" "+str(UnderPoints)+" "+str(UnderLine))
	# if dif2<=0 and dif>=0:
	# 	print("Polish Middle Totals "+linetype+" "+sportsbook1+" "+team1+" "+str(OverPoints)+" "+str(OverLine)+" "+sportsbook2+" "+team2+" "+str(UnderPoints)+" "+str(UnderLine))
	# 	print("Profit Percentage: "+str(profitpercent))
	# elif profitpercent>=3:
	# 	print("Polish Middle Totals "+linetype+" "+sportsbook1+" "+team1+" "+str(OverPoints)+" "+str(OverLine)+" "+sportsbook2+" "+team2+" "+str(UnderPoints)+" "+str(UnderLine))
	# 	print("Profit Percentage: "+str(profitpercent))
	if dif>=.5:
		if sport=="football" or sport=="basketball":
			if profitpercent>-.3:
				print("Totals "+linetype+" "+sportsbook1+" "+team1+" "+str(OverPoints)+" "+str(OverLine)+" "+sportsbook2+" "+team2+" "+str(UnderPoints)+" "+str(UnderLine))
				print("Profit Percentage: "+str(profitpercent))
				WriteToCSV("Totals Middle",linetype,sportsbook1,team1,OverPoints,OverLine,sportsbook2,team2,UnderPoints,UnderLine,profitpercent)
		elif profitpercent>-5:
			print("Totals "+linetype+" "+sportsbook1+" "+team1+" "+str(OverPoints)+" "+str(OverLine)+" "+sportsbook2+" "+team2+" "+str(UnderPoints)+" "+str(UnderLine))
			print("Profit Percentage: "+str(profitpercent))
			WriteToCSV("Totals Middle",linetype,sportsbook1,team1,OverPoints,OverLine,sportsbook2,team2,UnderPoints,UnderLine,profitpercent)
	elif dif>=1:
		if dif2<=6:
			print("Totals "+linetype+" "+sportsbook1+" "+team1+" "+str(OverPoints)+" "+str(OverLine)+" "+sportsbook2+" "+team2+" "+str(UnderPoints)+" "+str(UnderLine))
			print("Profit Percentage: "+str(profitpercent))
			WriteToCSV("Totals Middle",linetype,sportsbook1,team1,OverPoints,OverLine,sportsbook2,team2,UnderPoints,UnderLine,profitpercent)
	elif dif>=1.5:
		if dif2<=9:
			print("Totals "+linetype+" "+sportsbook1+" "+team1+" "+str(OverPoints)+" "+str(OverLine)+" "+sportsbook2+" "+team2+" "+str(UnderPoints)+" "+str(UnderLine))
			print("Profit Percentage: "+str(profitpercent))
			WriteToCSV("Totals Middle",linetype,sportsbook1,team1,OverPoints,OverLine,sportsbook2,team2,UnderPoints,UnderLine,profitpercent)
	elif dif>=2:
		if dif2<=12:
			print("Totals "+linetype+" "+sportsbook1+" "+team1+" "+str(OverPoints)+" "+str(OverLine)+" "+sportsbook2+" "+team2+" "+str(UnderPoints)+" "+str(UnderLine))
			print("Profit Percentage: "+str(profitpercent))
			WriteToCSV("Totals Middle",linetype,sportsbook1,team1,OverPoints,OverLine,sportsbook2,team2,UnderPoints,UnderLine,profitpercent)
	elif dif>=2.5:
		print("Totals "+linetype+" "+sportsbook1+" "+team1+" "+str(OverPoints)+" "+str(OverLine)+" "+sportsbook2+" "+team2+" "+str(UnderPoints)+" "+str(UnderLine))
		print("Profit Percentage: "+str(profitpercent))
		WriteToCSV("Totals Middle",linetype,sportsbook1,team1,OverPoints,OverLine,sportsbook2,team2,UnderPoints,UnderLine,profitpercent)


def CheckforAdvantages(masterdata):
	profit=0
	try:
		for matchup in masterdata.keys():
			
			sportbooks=masterdata[matchup]

			if len(sportbooks)<2:
				continue
			else:
				for sportsbook1 in sportbooks:
					for sportsbook2 in sportbooks:
						if sportsbook1["SportsBook"]==sportsbook2["SportsBook"]:
							continue
						else:
							if sportsbook1["LineType"]==sportsbook2["LineType"]:
								sportsbookOne=sportsbook1["SportsBook"]
								sportsbookTwo=sportsbook2["SportsBook"]
								LineType=sportsbook1["LineType"]
								AwayTeam=sportsbook1["AwayTeam"]
								HomeTeam=sportsbook2["HomeTeam"]

								try:
									AwayTeamMoneyLine=sportsbook1["AwayTeamMoneyLine"]
								
									HomeTeamMoneyLine=sportsbook2["HomeTeamMoneyLine"]
									CheckForArbritage(sportsbookOne,sportsbookTwo, LineType, AwayTeam, AwayTeamMoneyLine, HomeTeam, HomeTeamMoneyLine)

								except KeyError:pass

								try:
									AwayTeamPointSpread=sportsbook1["AwayTeamPointSpread"]
								
									HomeTeamPointSpread=sportsbook2["HomeTeamPointSpread"]
								
									AwayTeamPointLine=sportsbook1["AwayTeamPointLine"]
									sport=sportsbook1["Sport"]
									HomeTeamPointLine=sportsbook2["HomeTeamPointLine"]
									if (Decimal(AwayTeamPointSpread)<0 and Decimal(HomeTeamPointSpread)<0) or (Decimal(AwayTeamPointSpread)>0 and Decimal(HomeTeamPointSpread)>0):
										HomeTeamPointSpread=sportsbook2["AwayTeamPointSpread"]
										HomeTeamPointLine=sportsbook2["AwayTeamPointLine"]
										HomeTeam=sportsbook2["AwayTeam"]

									CheckForMiddlesSpread(sport,sportsbookOne,sportsbookTwo, LineType,AwayTeam,AwayTeamPointSpread,AwayTeamPointLine,HomeTeam,HomeTeamPointSpread,HomeTeamPointLine)

								except KeyError:pass

								try:
									OverPoints=sportsbook1["OverPoints"]
									OverLine=sportsbook1["OverLine"]
									UnderPoints=sportsbook2["UnderPoints"]
									UnderLine=sportsbook2["UnderLine"]
									sport=sportsbook1["Sport"]
									CheckForMiddlesTotals(sport,sportsbookOne,sportsbookTwo, LineType,AwayTeam,OverPoints,OverLine,HomeTeam,UnderPoints,UnderLine)
								except KeyError: pass
	except:
		time.sleep(60)
		return
							
							

