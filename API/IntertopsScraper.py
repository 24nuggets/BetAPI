
import requests
from requests import get
import time
from bs4 import BeautifulSoup, SoupStrainer

from user_agent import generate_user_agent
import numpy as np





  
  

  


      


def IntertopsQuartersHalfsGames(table, linetype, masterdata,sport):
	
	entries=[]
	data=[]

	entries= table.findAll('div', {'class':'trw'})
		
	for entry in entries:
		matchup={}
		team1=entry.find('div', {'class':'ustop'})
		team2=entry.find('div', {'class':'usbot'})
		if team1 != None:
			#Teams.append(team1.text.strip())
			#Opponents.append(team2.text.strip())
			matchup["LineType"]=linetype
			matchup["SportsBook"]="Intertops"
			team2=team2.text.strip()
			team1=team1.text.strip()
			team2=team2.replace('-',' ')
			team1=team1.replace('-',' ')
			team1=team1.lower()
			team2=team2.lower()
			team1=str(team1.encode('utf-8'))
			team2=str(team2.encode('utf-8'))
			matchup["HomeTeam"]=team2
			matchup["AwayTeam"]=team1
			matchup["Sport"]=sport

			key=sport+" "+team1+" vs "+team2
			
		else:
			continue
		data=entry.findAll('a',{'class','bs o us-o active'})
		i=0
		
				
				
		for point in data:

			if i<4:
				x=point.get('data-o-pts')
				y=point.get('data-o-inv')
				
				if i==0:
					if x !=None:
						#SpreadTeam.append('')
						point2=point.find('span',{'class','fright odds'})
						z=point2['data-o-cnt']
						matchup["AwayTeamPointSpread"]=x
						matchup["AwayTeamPointLine"]=y
						matchup["AwayTeamPointLineAmerican"]=z
				elif i==1:
					if x !=None:
						point2=point.find('span',{'class','fright odds'})
						z=point2['data-o-cnt']
						matchup["HomeTeamPointSpread"]= x
						matchup["HomeTeamPointLine"]=y
						matchup["HomeTeamPointLineAmerican"]=z
				elif i==2:
					if x !=None:
						point2=point.find('span',{'class','fright odds'})
						z=point2['data-o-cnt']
						matchup["OverPoints"]=x
						matchup["OverLine"]=y
						matchup["OverLineAmerican"]=z
				elif i==3:
					if x !=None:
						point2=point.find('span',{'class','fright odds'})
						z=point2['data-o-cnt']
						matchup["UnderPoints"]=x
						matchup["UnderLine"]=y
						matchup["UnderLineAmerican"]=z
			else:
				x=point.get('data-o-inv')
				point2=point.find('span',{'class','fright odds'})
				z=point2.get('data-o-cnt')
				if i==4:
					if x !=None:
						point2=point.find('span',{'class','odds'})
						z=point2['data-o-cnt']
						matchup["AwayTeamMoneyLineAmerican"]=z
						matchup["AwayTeamMoneyLine"]=x
				elif i==5:
					if x !=None:
						point2=point.find('span',{'class','odds'})
						z=point2['data-o-cnt']
						matchup["HomeTeamMoneyLineAmerican"]=z
						matchup["HomeTeamMoneyLine"]=x
			
			i=i+1
		
		if (key in masterdata.keys()):
			l=masterdata[key]
			l.append(matchup)
			masterdata[key]=l

		else:
			l=[]
			l.append(matchup)
			masterdata[key]=l	
		
	


def intertopsBaseScraper(myurl, masterdata):
	# generate a user agent
	
	referer='https://www.google.com/'
	h = {'User-Agent': generate_user_agent(device_type="desktop", os=('mac', 'linux')),
		'referer': referer}
	# pause for delay second to not do too many requests to server
	delays = [.5, .33, 3, 2, 1, 1.5]
	delay = np.random.choice(delays)
	#time.sleep(delay)
	

	try:	
		
		r = get(myurl,timeout=5, headers=h)
	except Exception as e:
		print(str(e))
		
		print('Intertops connnetion error')
		return
	if r.status_code==200:
		
		c = r.text
		
		
		#elapsed_time=time.time()
		
		soup=BeautifulSoup(c, 'lxml')
		
		#elapsed_time = time.time()-elapsed_time
		#print(elapsed_time)
		tables=[]
		
		j=0
		names=[]
		
		tables=soup.findAll('fieldset')
		Panels=soup.findAll('div',{'class':'panel-heading subpanel-heading'})
		code= myurl[-4:]
		if code=='1018':
			sport='football'
		elif code=='1016':
			sport='football'
		elif code=='3295':
			sport='basketball'
		elif code=='/739':
			sport='basketball'
		elif code=='/736':
			sport='basketball'
		elif code=='3297':
			sport='basketball'
		elif code=='1070':
			sport='basketball'
		elif code=='1068':
			sport='basketball'
		elif code=='1064':
			sport='hockey'
		sport=(str(sport.encode("utf-8")))
		for panel in Panels:
			name=panel.find('span',{'class':'title-string'})
			names.append(name.text.strip())
		
		for table in tables:
			
			if (names[j]=='Team Total'):
				continue
			else:
				linetype=names[j]
				if names[j]=='Game Lines':
					linetype="Match"
				df=IntertopsQuartersHalfsGames(table, linetype, masterdata,sport)
			j=j+1
		
			#df.index.name=(names[j])
	else:
		print("Intertops request error: " + str(r.status_code))


		
     
	


	

	









