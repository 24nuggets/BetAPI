import requests
from requests import get
import time
import pandas as pd
from bs4 import BeautifulSoup, SoupStrainer
from multiprocessing import Pool
from user_agent import generate_user_agent
import numpy as np


def bovadaBaseScraper(myurl, masterdata):
	# generate a user agent
	
	referer='https://www.google.com/'
	h = {'User-Agent': generate_user_agent(device_type="desktop", os=('mac', 'linux')),
		'referer': referer}
	# pause for delay second to not do too many requests to server
	delays = [.5, .33, 3, 2, 1, 1.5]
	delay = np.random.choice(delays)
	#time.sleep(delay)
	

	
	try:
		source = get(myurl, timeout=5, headers=h).json()
	except Exception,e:
		print(str(e))
		print('Bovada connnetion error')
		return
	
	
		
		

	
	for data in source:
		
		sport=data['path'][1]['description']
		sport=sport.lower()
		sport=(unicode(sport).encode("utf-8"))
		for team in data['events']:
			matchup={}
			try:
				team_1 = team['competitors'][0]['name']
				team_2 = team['competitors'][1]['name']
				team_1=team_1.split('(')[0]
				
				team_2=team_2.split('(')[0]
				team_1=team_1.strip()
				team_2=team_2.strip()
				
				team_1=team_1.replace('. ',' ')
				team_2=team_2.replace('. ',' ')
				if team_1.endswith(' U') :
					team_1=team_1[:-1]
				
				if team_2.endswith(' U'):
					team_2=team_2[:-1]
				team_1=team_1.strip()
				team_2=team_2.strip()
				team_1=team_1.lower()
				team_2=team_2.lower()
				team_1=unicode(team_1).encode("utf-8")
				team_2=unicode(team_2).encode("utf-8")
				
				linetype=team['displayGroups'][0]['markets'][0]['period']['description']
				try: 
					odd_1_1 = team['displayGroups'][0]['markets'][0]['outcomes'][0]['price']['handicap'] 
					matchup["AwayTeamPointSpread"]=odd_1_1
				except KeyError: pass
				try: 
					odd_1_2 = team['displayGroups'][0]['markets'][0]['outcomes'][0]['price']['decimal'] 
					matchup["AwayTeamPointLine"]=odd_1_2
				except KeyError: pass
				try: 
					moneyline1=team['displayGroups'][0]['markets'][1]['outcomes'][0]['price']['decimal']
					matchup["AwayTeamMoneyLine"]=moneyline1
				except KeyError: pass
				try: 
					over=team['displayGroups'][0]['markets'][2]['outcomes'][0]['price']['handicap'] 
					matchup["OverPoints"]=over
				except KeyError: pass
				try: 
					overline=team['displayGroups'][0]['markets'][2]['outcomes'][0]['price']['decimal'] 
					matchup["OverLine"]=overline
				except KeyError: pass
				try:
					odd_2_1 = team['displayGroups'][0]['markets'][0]['outcomes'][1]['price']['handicap'] 
					matchup["HomeTeamPointSpread"]= odd_2_1
				except KeyError: pass
				try: 
					odd_2_2 = team['displayGroups'][0]['markets'][0]['outcomes'][1]['price']['decimal'] 
					matchup["HomeTeamPointLine"]=odd_2_2
				except KeyError: pass
				try: 
					moneyline2=team['displayGroups'][0]['markets'][1]['outcomes'][1]['price']['decimal']
					matchup["HomeTeamMoneyLine"]=moneyline2
				except KeyError: pass
				try: 
					under=team['displayGroups'][0]['markets'][2]['outcomes'][1]['price']['handicap'] 
					matchup["UnderPoints"]=under
				except KeyError: pass
				try:
					underline=team['displayGroups'][0]['markets'][2]['outcomes'][1]['price']['decimal'] 
					matchup["UnderLine"]=underline
				except KeyError: pass
				if linetype=="Second Half":
					linetype="2nd Half"
				matchup["LineType"]=linetype
				matchup["SportsBook"]="Bovada"
				matchup["HomeTeam"]=team_1
				matchup["AwayTeam"]=team_2
				matchup["Sport"]=sport
				
				
				
				
				
				
				
				
				

				key=sport+" "+team_2+" vs "+team_1
				
				if (key in masterdata.keys()):
					l=masterdata[key]
					l.append(matchup)
					masterdata[key]=l

				else:
					l=[]
					l.append(matchup)
					masterdata[key]=l

				
				
			except IndexError:
				continue
	return

			
			
			


	










