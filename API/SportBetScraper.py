# -*- coding: utf-8 -*-

import requests
from requests import get
import time
from bs4 import BeautifulSoup, SoupStrainer
from Utilities import ConvertAmericanOddsToDecimal
from user_agent import generate_user_agent
import numpy as np




def sportBetBaseScraper(myurl, masterdata):
	# generate a user agent
	
	referer='https://www.google.com/'
	h = {'User-Agent': generate_user_agent(device_type="desktop", os=('mac', 'linux')),
		'referer': referer}
	# pause for delay second to not do too many requests to server
	delays = [.5, .33, 3, 2, 1, 1.5]
	delay = np.random.choice(delays)
	#time.sleep(delay)
	

	try:	
		
		r = get(myurl, timeout=5, headers=h, verify=False)
	except Exception as e:
		print(str(e))
		
		print('Sportsbet connnetion error')
		return
	if r.status_code==200:
		
		c = r.text
		
		
		#elapsed_time=time.time()
		strainer=SoupStrainer('div',attrs={'id':'thecontent'})
		soup=BeautifulSoup(c, 'lxml',parse_only=strainer)
		
		#elapsed_time = time.time()-elapsed_time
		#print(elapsed_time)
		entries=[]
		
		
		
		entries=soup.findAll('div',{'class':'card'})
		
		code= myurl[-16:]
		if code=='ketball/Reduced/':
			sport='basketball'
			linetype='Match'
		elif code=='ootball/Reduced/':
			sport='football'
			linetype='Match'
		elif code=='/Hockey/Reduced/':
			sport='hockey'
			linetype='Match'
		elif code=='ighting/Reduced/':
			sport='fighting'
			linetype='Match'
		
		sport=(str(sport.encode("utf-8")))
		j=0
		
		for entry in entries:
			
			if j==0:
				j=j+1
				continue
			
			j=j+1
			matchup={}
			
			title=entry.find('p',{'class':'linetitle'})
			title=title.text.strip()
			if title=="1st Half" or title=="2nd Half" or title=="1st Quarter" or title=="2nd Quarter" or title=="3rd Quarter" or title=="4th Quarter":
				linetype=title
			else:
				linetype="Match"
			line1=entry.find('div',{'class':'line1'})
			line2=entry.find('div',{'class':'line2'})
			
			teamline1=line1.find('div',{'class':'game'})
			teamline2=line2.find('div',{'class':'game'})
			
			team1=teamline1.find('p')
			team2=teamline2.find('p')
			
			team1=team1.text.strip()
			team2=team2.text.strip()
			if team1.endswith(' U') :
				team1=team1[:-2]
			
			if team2.endswith(' U'):
				team2=team2[:-2]
			team1=team1.lower()
			team2=team2.lower()
			team1=str(team1.encode('utf-8'))
			team2=str(team2.encode('utf-8'))
			lines1=line1.findAll('p',{'class':'betting-line'})
			lines2=line2.findAll('p',{'class':'betting-line'})
			

			
			
			
			
			try:
				spread1Info=lines1[0].text.strip()
				spread2Info=lines2[0].text.strip()
				if spread2Info!=' ':
					try:
						index1=spread1Info.index('-',1)
					except:index1=spread1Info.index('+',1)
					try:
						index2=spread2Info.index('-',1)
					except:index2=spread2Info.index('+',1)
					
					awayTeamPointSpread=spread1Info[:index1]
					awayTeamPointLine=spread1Info[index1:]
					homeTeamPointSpread=spread2Info[:index2]
					homeTeamPointLine=spread2Info[index2:]
					awayTeamPointSpread=str(awayTeamPointSpread.encode('utf-8'))
					homeTeamPointSpread=str(homeTeamPointSpread.encode('utf-8'))
					awayTeamPointSpread=awayTeamPointSpread.replace(u"½",u".5")
					homeTeamPointSpread=homeTeamPointSpread.replace(u"½",u".5")
					
					awayTeamPointLine=ConvertAmericanOddsToDecimal(awayTeamPointLine)
					homeTeamPointLine=ConvertAmericanOddsToDecimal(homeTeamPointLine)
					matchup["AwayTeamPointSpread"]=awayTeamPointSpread
					matchup["HomeTeamPointSpread"]=homeTeamPointSpread
					matchup["AwayTeamPointLine"]=awayTeamPointLine
					matchup["HomeTeamPointLine"]=homeTeamPointLine

			except:pass
			
			try:
				moneyline1Info=lines1[1].text.strip()
				moneyline2Info=lines2[1].text.strip()
				if moneyline1Info!=' ':
					awayTeamMoneyLine=ConvertAmericanOddsToDecimal(moneyline1Info)
					homeTeamMoneyLine=ConvertAmericanOddsToDecimal(moneyline2Info)
					matchup["AwayTeamMoneyLine"]=awayTeamMoneyLine
					matchup["HomeTeamMoneyLine"]=homeTeamMoneyLine
				
			except:pass
			
			try:
				overInfo=lines1[2].text.strip()
				underInfo=lines2[2].text.strip()
				if overInfo!=' ':
					totalOverList=overInfo.split(' ')
					over=totalOverList[1]
					over=str(over.encode('utf-8'))
					over=over.replace(u"½",u".5")
					overLine=totalOverList[2]
					
					totalUnderList=underInfo.split(' ')
					under=totalUnderList[1]
					under=str(under.encode('utf-8'))
					under=under.replace(u"½",u".5")
					underLine=totalUnderList[2]
					
					overLine=ConvertAmericanOddsToDecimal(overLine)
					underLine=ConvertAmericanOddsToDecimal(underLine)
					matchup["OverPoints"]=over
					matchup["UnderPoints"]=under
					matchup["OverLine"]=overLine
					matchup["UnderLine"]=underLine
				
			except: pass

			matchup["LineType"]=linetype
			matchup["SportsBook"]="SportBet"
			matchup["HomeTeam"]=team2
			matchup["AwayTeam"]=team1
			matchup["Sport"]=sport
			key=sport+" "+team1+" vs "+team2
			
			if (key in masterdata.keys()):
				l=masterdata[key]
				l.append(matchup)
				masterdata[key]=l

			else:
				l=[]
				l.append(matchup)
				masterdata[key]=l


			
			

		
	else:
		print("SportBet request error: " + str(r.status_code))

