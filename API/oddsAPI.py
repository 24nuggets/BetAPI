import csv
from IntertopsScraper import intertopsBaseScraper
from Bovada import bovadaBaseScraper
from BetPhoenixScraper import betPhoenixBaseScraper
from multiprocessing import Process, Manager
import flask
import time
from functools import partial
from SkyBookScraper import skyBookBaseScraper
from SportBetScraper import sportBetBaseScraper
from user_agent import generate_user_agent
from requests import get
import json


app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/api/v1/resources/nfl/match/totals/american', methods=['GET'])
def nflTotalsAmerican():	
	
	league='nfl'
	manager=Manager()
	masterdata=manager.dict()
	IntertopsBaseURLs='https://sports.intertops.eu/en/Bets/American-Football/NFL-Lines/1018'
	bovadaAPIUrls='https://services.bovada.lv/services/sports/event/coupon/events/A/description/football?marketFilterId=def&preMatchOnly=true&eventsLimit=50&lang=en'
	betPhoenixAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111207169812656759593_1577303361038&hid=bdb01c9f736f2e641984fcde2fce11ad&cmd=games&leagues=1&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577303361039'
	skyBookAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111206009097206260869_1577542998571&hid=e154acf7203ae1251e181abf8aca82a7&cmd=games&leagues=1&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577542998572'
	#SportBetReducedURLS='https://www.sportbet.com/lines/Football/Reduced/'


	p=Process(target=intertopsBaseScraper,args=(IntertopsBaseURLs,masterdata))
	p.start()
	#p1=Process(target=sportBetBaseScraper,args=(SportBetReducedURLS,masterdata))
	#p1.start()
	p2=Process(target=bovadaBaseScraper,args=(bovadaAPIUrls,masterdata))
	p2.start()
	p3=Process(target=betPhoenixBaseScraper,args=(betPhoenixAPIUrls,masterdata))
	p3.start()
	p4=Process(target=skyBookBaseScraper,args=(skyBookAPIUrls,masterdata))
	p4.start()







	p.join()
	#p1.join()
	p2.join()
	p3.join()
	p4.join()
	spreadData=[]
	for key in masterdata:
		entry={}
		if len(masterdata[key])<2:
		       continue
		entry['AwayTeam']=masterdata[key][0]['AwayTeam'][2:-1].title()
		entry['HomeTeam']=masterdata[key][0]['HomeTeam'][2:-1].title()
		
		for key1 in masterdata[key]:
			if key1['LineType']=="Match":
				bookName=key1['SportsBook']
				try:
					entry[bookName+"OverPoints"]=key1['OverPoints']
					entry[bookName+"OverLine"]=key1['OverLineAmerican']
					entry[bookName+"UnderPoints"]=key1['UnderPoints']
					entry[bookName+"UnderLine"]=key1['UnderLineAmerican']
				except KeyError: pass
		spreadData.append(entry)
			
		
	output=json.dumps(spreadData)
	return output

@app.route('/api/v1/resources/nfl/match/totals/decimal', methods=['GET'])
def nflTotalsDecimal():	
	
	league='nfl'
	manager=Manager()
	masterdata=manager.dict()
	IntertopsBaseURLs='https://sports.intertops.eu/en/Bets/American-Football/NFL-Lines/1018'
	bovadaAPIUrls='https://services.bovada.lv/services/sports/event/coupon/events/A/description/football?marketFilterId=def&preMatchOnly=true&eventsLimit=50&lang=en'
	betPhoenixAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111207169812656759593_1577303361038&hid=bdb01c9f736f2e641984fcde2fce11ad&cmd=games&leagues=1&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577303361039'
	skyBookAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111206009097206260869_1577542998571&hid=e154acf7203ae1251e181abf8aca82a7&cmd=games&leagues=1&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577542998572'
	#SportBetReducedURLS='https://www.sportbet.com/lines/Football/Reduced/'


	p=Process(target=intertopsBaseScraper,args=(IntertopsBaseURLs,masterdata))
	p.start()
	#p1=Process(target=sportBetBaseScraper,args=(SportBetReducedURLS,masterdata))
	#p1.start()
	p2=Process(target=bovadaBaseScraper,args=(bovadaAPIUrls,masterdata))
	p2.start()
	p3=Process(target=betPhoenixBaseScraper,args=(betPhoenixAPIUrls,masterdata))
	p3.start()
	p4=Process(target=skyBookBaseScraper,args=(skyBookAPIUrls,masterdata))
	p4.start()







	p.join()
	#p1.join()
	p2.join()
	p3.join()
	p4.join()
	spreadData=[]
	for key in masterdata:
		entry={}
		if len(masterdata[key])<2:
		       continue
		entry['AwayTeam']=masterdata[key][0]['AwayTeam'][2:-1].title()
		entry['HomeTeam']=masterdata[key][0]['HomeTeam'][2:-1].title()
		
		for key1 in masterdata[key]:
			if key1['LineType']=="Match":
				bookName=key1['SportsBook']
				try:
					entry[bookName+"OverPoints"]=key1['OverPoints']
					entry[bookName+"OverLine"]=round(float(key1['OverLine']),2)
					entry[bookName+"UnderPoints"]=key1['UnderPoints']
					entry[bookName+"UnderLine"]=round(float(key1['UnderLine']),2)
				except KeyError:pass
		spreadData.append(entry)
			
		
	output=json.dumps(spreadData)
	return output

@app.route('/api/v1/resources/nfl/match/moneyline/decimal', methods=['GET'])
def nflMoneyLineDecimal():	
	
	league='nfl'
	manager=Manager()
	masterdata=manager.dict()
	IntertopsBaseURLs='https://sports.intertops.eu/en/Bets/American-Football/NFL-Lines/1018'
	bovadaAPIUrls='https://services.bovada.lv/services/sports/event/coupon/events/A/description/football?marketFilterId=def&preMatchOnly=true&eventsLimit=50&lang=en'
	betPhoenixAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111207169812656759593_1577303361038&hid=bdb01c9f736f2e641984fcde2fce11ad&cmd=games&leagues=1&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577303361039'
	skyBookAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111206009097206260869_1577542998571&hid=e154acf7203ae1251e181abf8aca82a7&cmd=games&leagues=1&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577542998572'
	#SportBetReducedURLS='https://www.sportbet.com/lines/Football/Reduced/'


	p=Process(target=intertopsBaseScraper,args=(IntertopsBaseURLs,masterdata))
	p.start()
	#p1=Process(target=sportBetBaseScraper,args=(SportBetReducedURLS,masterdata))
	#p1.start()
	p2=Process(target=bovadaBaseScraper,args=(bovadaAPIUrls,masterdata))
	p2.start()
	p3=Process(target=betPhoenixBaseScraper,args=(betPhoenixAPIUrls,masterdata))
	p3.start()
	p4=Process(target=skyBookBaseScraper,args=(skyBookAPIUrls,masterdata))
	p4.start()







	p.join()
	#p1.join()
	p2.join()
	p3.join()
	p4.join()
	spreadData=[]
	for key in masterdata:
		entry={}
		if len(masterdata[key])<2:
		       continue
		entry['AwayTeam']=masterdata[key][0]['AwayTeam'][2:-1].title()
		entry['HomeTeam']=masterdata[key][0]['HomeTeam'][2:-1].title()
		
		for key1 in masterdata[key]:
			if key1['LineType']=="Match":
				bookName=key1['SportsBook']
				try:
					entry[bookName+"AwayTeamMoneyLine"]=round(float(key1['AwayTeamMoneyLine']),2)

					entry[bookName+"HomeTeamMoneyLine"]=round(float(key1['HomeTeamMoneyLine']),2)
				except KeyError:pass
		spreadData.append(entry)
			
		
	output=json.dumps(spreadData)
	return output

@app.route('/api/v1/resources/nfl/match/moneyline/american', methods=['GET'])
def nflMoneyLineAmerican():	
	
	league='nfl'
	manager=Manager()
	masterdata=manager.dict()
	IntertopsBaseURLs='https://sports.intertops.eu/en/Bets/American-Football/NFL-Lines/1018'
	bovadaAPIUrls='https://services.bovada.lv/services/sports/event/coupon/events/A/description/football?marketFilterId=def&preMatchOnly=true&eventsLimit=50&lang=en'
	betPhoenixAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111207169812656759593_1577303361038&hid=bdb01c9f736f2e641984fcde2fce11ad&cmd=games&leagues=1&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577303361039'
	skyBookAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111206009097206260869_1577542998571&hid=e154acf7203ae1251e181abf8aca82a7&cmd=games&leagues=1&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577542998572'
	#SportBetReducedURLS='https://www.sportbet.com/lines/Football/Reduced/'


	p=Process(target=intertopsBaseScraper,args=(IntertopsBaseURLs,masterdata))
	p.start()
	#p1=Process(target=sportBetBaseScraper,args=(SportBetReducedURLS,masterdata))
	#p1.start()
	p2=Process(target=bovadaBaseScraper,args=(bovadaAPIUrls,masterdata))
	p2.start()
	p3=Process(target=betPhoenixBaseScraper,args=(betPhoenixAPIUrls,masterdata))
	p3.start()
	p4=Process(target=skyBookBaseScraper,args=(skyBookAPIUrls,masterdata))
	p4.start()







	p.join()
	#p1.join()
	p2.join()
	p3.join()
	p4.join()
	spreadData=[]
	for key in masterdata:
		entry={}
		if len(masterdata[key])<2:
		       continue
		entry['AwayTeam']=masterdata[key][0]['AwayTeam'][2:-1].title()
		entry['HomeTeam']=masterdata[key][0]['HomeTeam'][2:-1].title()
		
		for key1 in masterdata[key]:
			if key1['LineType']=="Match":
				bookName=key1['SportsBook']
				try:
					entry[bookName+"AwayTeamMoneyLine"]=key1['AwayTeamMoneyLineAmerican']

					entry[bookName+"HomeTeamMoneyLine"]=key1['HomeTeamMoneyLineAmerican']
				except KeyError: pass
		spreadData.append(entry)
			
		
	output=json.dumps(spreadData)
	return output

@app.route('/api/v1/resources/nfl/match/spreads/american', methods=['GET'])
def nflSpreadAmerican():	
	
	league='nfl'
	manager=Manager()
	masterdata=manager.dict()
	IntertopsBaseURLs='https://sports.intertops.eu/en/Bets/American-Football/NFL-Lines/1018'
	bovadaAPIUrls='https://services.bovada.lv/services/sports/event/coupon/events/A/description/football?marketFilterId=def&preMatchOnly=true&eventsLimit=50&lang=en'
	betPhoenixAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111207169812656759593_1577303361038&hid=bdb01c9f736f2e641984fcde2fce11ad&cmd=games&leagues=1&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577303361039'
	skyBookAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111206009097206260869_1577542998571&hid=e154acf7203ae1251e181abf8aca82a7&cmd=games&leagues=1&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577542998572'
	#SportBetReducedURLS='https://www.sportbet.com/lines/Football/Reduced/'


	p=Process(target=intertopsBaseScraper,args=(IntertopsBaseURLs,masterdata))
	p.start()
	#p1=Process(target=sportBetBaseScraper,args=(SportBetReducedURLS,masterdata))
	#p1.start()
	p2=Process(target=bovadaBaseScraper,args=(bovadaAPIUrls,masterdata))
	p2.start()
	p3=Process(target=betPhoenixBaseScraper,args=(betPhoenixAPIUrls,masterdata))
	p3.start()
	p4=Process(target=skyBookBaseScraper,args=(skyBookAPIUrls,masterdata))
	p4.start()







	p.join()
	#p1.join()
	p2.join()
	p3.join()
	p4.join()
	spreadData=[]
	for key in masterdata:
		entry={}
		if len(masterdata[key])<2:
		       continue
		entry['AwayTeam']=masterdata[key][0]['AwayTeam'][2:-1].title()
		entry['HomeTeam']=masterdata[key][0]['HomeTeam'][2:-1].title()
		
		for key1 in masterdata[key]:
			if key1['LineType']=="Match":
				bookName=key1['SportsBook']
				try:
					entry[bookName+"AwayPointSpread"]=key1['AwayTeamPointSpread']
					entry[bookName+"AwayPointLine"]=key1['AwayTeamPointLineAmerican']
					entry[bookName+"HomePointSpread"]=key1['HomeTeamPointSpread']
					entry[bookName+"HomePointLine"]=key1['HomeTeamPointLineAmerican']
				except KeyError: pass
		spreadData.append(entry)
			
		
	output=json.dumps(spreadData)
	return output
@app.route('/api/v1/resources/nfl/match/spreads/decimal', methods=['GET'])
def nflSpreadDecimal():	
	
	league='nfl'
	manager=Manager()
	masterdata=manager.dict()
	IntertopsBaseURLs='https://sports.intertops.eu/en/Bets/American-Football/NFL-Lines/1018'
	bovadaAPIUrls='https://services.bovada.lv/services/sports/event/coupon/events/A/description/football?marketFilterId=def&preMatchOnly=true&eventsLimit=50&lang=en'
	betPhoenixAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111207169812656759593_1577303361038&hid=bdb01c9f736f2e641984fcde2fce11ad&cmd=games&leagues=1&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577303361039'
	skyBookAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111206009097206260869_1577542998571&hid=e154acf7203ae1251e181abf8aca82a7&cmd=games&leagues=1&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577542998572'
	#SportBetReducedURLS='https://www.sportbet.com/lines/Football/Reduced/'


	p=Process(target=intertopsBaseScraper,args=(IntertopsBaseURLs,masterdata))
	p.start()
	#p1=Process(target=sportBetBaseScraper,args=(SportBetReducedURLS,masterdata))
	#p1.start()
	p2=Process(target=bovadaBaseScraper,args=(bovadaAPIUrls,masterdata))
	p2.start()
	p3=Process(target=betPhoenixBaseScraper,args=(betPhoenixAPIUrls,masterdata))
	p3.start()
	p4=Process(target=skyBookBaseScraper,args=(skyBookAPIUrls,masterdata))
	p4.start()







	p.join()
	#p1.join()
	p2.join()
	p3.join()
	p4.join()
	spreadData=[]
	for key in masterdata:
		entry={}
		if len(masterdata[key])<2:
		       continue
		entry['AwayTeam']=masterdata[key][0]['AwayTeam'][2:-1].title()
		entry['HomeTeam']=masterdata[key][0]['HomeTeam'][2:-1].title()
		
		for key1 in masterdata[key]:
			if key1['LineType']=="Match":
				bookName=key1['SportsBook']
				try:
					entry[bookName+"AwayPointSpread"]=key1['AwayTeamPointSpread']
					entry[bookName+"AwayPointLine"]=round(float(key1['AwayTeamPointLine']),2)
					entry[bookName+"HomePointSpread"]=key1['HomeTeamPointSpread']
					entry[bookName+"HomePointLine"]=round(float(key1['HomeTeamPointLine']),2)
				except KeyError:pass
		spreadData.append(entry)
			
		
	output=json.dumps(spreadData)
	return output

@app.route('/api/v1/resources/nba/match/spreads/american', methods=['GET'])
def nbaSpreadAmerican():
	league='nba'
	manager=Manager()
	masterdata=manager.dict()
	IntertopsBaseURLs='https://sports.intertops.eu/en/Bets/Basketball/NBA-Lines/1070'
	bovadaAPIUrls='https://services.bovada.lv/services/sports/event/coupon/events/A/description/basketball?marketFilterId=def&preMatchOnly=true&eventsLimit=50&lang=en'
	betPhoenixAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111207169812656759593_1577303361038&hid=bdb01c9f736f2e641984fcde2fce11ad&cmd=games&leagues=3&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577303361039'
	skyBookAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111206009097206260869_1577542998571&hid=e154acf7203ae1251e181abf8aca82a7&cmd=games&leagues=3&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577542998572'
	#SportBetReducedURLS='https://www.sportbet.com/lines/Basketball/Reduced/'


	p=Process(target=intertopsBaseScraper,args=(IntertopsBaseURLs,masterdata))
	p.start()
	#p1=Process(target=sportBetBaseScraper,args=(SportBetReducedURLS,masterdata))
	#p1.start()
	p2=Process(target=bovadaBaseScraper,args=(bovadaAPIUrls,masterdata))
	p2.start()
	p3=Process(target=betPhoenixBaseScraper,args=(betPhoenixAPIUrls,masterdata))
	p3.start()
	p4=Process(target=skyBookBaseScraper,args=(skyBookAPIUrls,masterdata))
	p4.start()







	p.join()
	#p1.join()
	p2.join()
	p3.join()
	p4.join()
	spreadData=[]
	for key in masterdata:
		entry={}
		if len(masterdata[key])<2:
		       continue
		entry['AwayTeam']=masterdata[key][0]['AwayTeam'][2:-1].title()
		entry['HomeTeam']=masterdata[key][0]['HomeTeam'][2:-1].title()
		
		for key1 in masterdata[key]:
			if key1['LineType']=="Match":
				bookName=key1['SportsBook']
				try:
					entry[bookName+"AwayPointSpread"]=key1['AwayTeamPointSpread']
					entry[bookName+"AwayPointLine"]=key1['AwayTeamPointLineAmerican']
					entry[bookName+"HomePointSpread"]=key1['HomeTeamPointSpread']
					entry[bookName+"HomePointLine"]=key1['HomeTeamPointLineAmerican']
				except KeyError: pass
		spreadData.append(entry)
			
		
	output=json.dumps(spreadData)
	return output



@app.route('/api/v1/resources/nba/match/moneyline/american', methods=['GET'])
def nbaMoneyLineAmerican():
	league='nba'
	manager=Manager()
	masterdata=manager.dict()
	IntertopsBaseURLs='https://sports.intertops.eu/en/Bets/Basketball/NBA-Lines/1070'
	bovadaAPIUrls='https://services.bovada.lv/services/sports/event/coupon/events/A/description/basketball?marketFilterId=def&preMatchOnly=true&eventsLimit=50&lang=en'
	betPhoenixAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111207169812656759593_1577303361038&hid=bdb01c9f736f2e641984fcde2fce11ad&cmd=games&leagues=3&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577303361039'
	skyBookAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111206009097206260869_1577542998571&hid=e154acf7203ae1251e181abf8aca82a7&cmd=games&leagues=3&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577542998572'
	#SportBetReducedURLS='https://www.sportbet.com/lines/Basketball/Reduced/'


	p=Process(target=intertopsBaseScraper,args=(IntertopsBaseURLs,masterdata))
	p.start()
	#p1=Process(target=sportBetBaseScraper,args=(SportBetReducedURLS,masterdata))
	#p1.start()
	p2=Process(target=bovadaBaseScraper,args=(bovadaAPIUrls,masterdata))
	p2.start()
	p3=Process(target=betPhoenixBaseScraper,args=(betPhoenixAPIUrls,masterdata))
	p3.start()
	p4=Process(target=skyBookBaseScraper,args=(skyBookAPIUrls,masterdata))
	p4.start()







	p.join()
	#p1.join()
	p2.join()
	p3.join()
	p4.join()
	spreadData=[]
	for key in masterdata:
		entry={}
		if len(masterdata[key])<2:
		       continue
		entry['AwayTeam']=masterdata[key][0]['AwayTeam'][2:-1].title()
		entry['HomeTeam']=masterdata[key][0]['HomeTeam'][2:-1].title()
		
		for key1 in masterdata[key]:
			if key1['LineType']=="Match":
				bookName=key1['SportsBook']
				try:
					entry[bookName+"AwayTeamMoneyLine"]=key1['AwayTeamMoneyLineAmerican']

					entry[bookName+"HomeTeamMoneyLine"]=key1['HomeTeamMoneyLineAmerican']
				except KeyError:pass
		spreadData.append(entry)
			
		
	output=json.dumps(spreadData)
	return output

@app.route('/api/v1/resources/nba/match/moneyline/decimal', methods=['GET'])
def nbaMoneyLineDecimal():
	league='nba'
	manager=Manager()
	masterdata=manager.dict()
	IntertopsBaseURLs='https://sports.intertops.eu/en/Bets/Basketball/NBA-Lines/1070'
	bovadaAPIUrls='https://services.bovada.lv/services/sports/event/coupon/events/A/description/basketball?marketFilterId=def&preMatchOnly=true&eventsLimit=50&lang=en'
	betPhoenixAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111207169812656759593_1577303361038&hid=bdb01c9f736f2e641984fcde2fce11ad&cmd=games&leagues=3&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577303361039'
	skyBookAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111206009097206260869_1577542998571&hid=e154acf7203ae1251e181abf8aca82a7&cmd=games&leagues=3&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577542998572'
	#SportBetReducedURLS='https://www.sportbet.com/lines/Basketball/Reduced/'


	p=Process(target=intertopsBaseScraper,args=(IntertopsBaseURLs,masterdata))
	p.start()
	#p1=Process(target=sportBetBaseScraper,args=(SportBetReducedURLS,masterdata))
	#p1.start()
	p2=Process(target=bovadaBaseScraper,args=(bovadaAPIUrls,masterdata))
	p2.start()
	p3=Process(target=betPhoenixBaseScraper,args=(betPhoenixAPIUrls,masterdata))
	p3.start()
	p4=Process(target=skyBookBaseScraper,args=(skyBookAPIUrls,masterdata))
	p4.start()







	p.join()
	#p1.join()
	p2.join()
	p3.join()
	p4.join()
	spreadData=[]
	for key in masterdata:
		entry={}
		if len(masterdata[key])<2:
		       continue
		entry['AwayTeam']=masterdata[key][0]['AwayTeam'][2:-1].title()
		entry['HomeTeam']=masterdata[key][0]['HomeTeam'][2:-1].title()
		
		for key1 in masterdata[key]:
			if key1['LineType']=="Match":
				bookName=key1['SportsBook']
				try:
					entry[bookName+"AwayTeamMoneyLine"]=round(float(key1['AwayTeamMoneyLine']),2)

					entry[bookName+"HomeTeamMoneyLine"]=round(float(key1['HomeTeamMoneyLine']),2)
				except KeyError:pass
		spreadData.append(entry)
			
		
	output=json.dumps(spreadData)
	return output


@app.route('/api/v1/resources/nba/match/totals/american', methods=['GET'])
def nbaTotalsAmerican():
	league='nba'
	manager=Manager()
	masterdata=manager.dict()
	IntertopsBaseURLs='https://sports.intertops.eu/en/Bets/Basketball/NBA-Lines/1070'
	bovadaAPIUrls='https://services.bovada.lv/services/sports/event/coupon/events/A/description/basketball?marketFilterId=def&preMatchOnly=true&eventsLimit=50&lang=en'
	betPhoenixAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111207169812656759593_1577303361038&hid=bdb01c9f736f2e641984fcde2fce11ad&cmd=games&leagues=3&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577303361039'
	skyBookAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111206009097206260869_1577542998571&hid=e154acf7203ae1251e181abf8aca82a7&cmd=games&leagues=3&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577542998572'
	#SportBetReducedURLS='https://www.sportbet.com/lines/Basketball/Reduced/'


	p=Process(target=intertopsBaseScraper,args=(IntertopsBaseURLs,masterdata))
	p.start()
	#p1=Process(target=sportBetBaseScraper,args=(SportBetReducedURLS,masterdata))
	#p1.start()
	p2=Process(target=bovadaBaseScraper,args=(bovadaAPIUrls,masterdata))
	p2.start()
	p3=Process(target=betPhoenixBaseScraper,args=(betPhoenixAPIUrls,masterdata))
	p3.start()
	p4=Process(target=skyBookBaseScraper,args=(skyBookAPIUrls,masterdata))
	p4.start()







	p.join()
	#p1.join()
	p2.join()
	p3.join()
	p4.join()
	spreadData=[]
	for key in masterdata:
		entry={}
		if len(masterdata[key])<2:
		       continue
		entry['AwayTeam']=masterdata[key][0]['AwayTeam'][2:-1].title()
		entry['HomeTeam']=masterdata[key][0]['HomeTeam'][2:-1].title()
		
		for key1 in masterdata[key]:
			if key1['LineType']=="Match":
				bookName=key1['SportsBook']
				try:
					entry[bookName+"OverPoints"]=key1['OverPoints']
					entry[bookName+"OverLine"]=key1['OverLineAmerican']
					entry[bookName+"UnderPoints"]=key1['UnderPoints']
					entry[bookName+"UnderLine"]=key1['UnderLineAmerican']
				except KeyError: pass
		spreadData.append(entry)
			
		
	output=json.dumps(spreadData)
	return output

@app.route('/api/v1/resources/nba/match/totals/decimal', methods=['GET'])
def nbaTotalsDecimal():
	league='nba'
	manager=Manager()
	masterdata=manager.dict()
	IntertopsBaseURLs='https://sports.intertops.eu/en/Bets/Basketball/NBA-Lines/1070'
	bovadaAPIUrls='https://services.bovada.lv/services/sports/event/coupon/events/A/description/basketball?marketFilterId=def&preMatchOnly=true&eventsLimit=50&lang=en'
	betPhoenixAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111207169812656759593_1577303361038&hid=bdb01c9f736f2e641984fcde2fce11ad&cmd=games&leagues=3&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577303361039'
	skyBookAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111206009097206260869_1577542998571&hid=e154acf7203ae1251e181abf8aca82a7&cmd=games&leagues=3&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577542998572'
	#SportBetReducedURLS='https://www.sportbet.com/lines/Basketball/Reduced/'


	p=Process(target=intertopsBaseScraper,args=(IntertopsBaseURLs,masterdata))
	p.start()
	#p1=Process(target=sportBetBaseScraper,args=(SportBetReducedURLS,masterdata))
	#p1.start()
	p2=Process(target=bovadaBaseScraper,args=(bovadaAPIUrls,masterdata))
	p2.start()
	p3=Process(target=betPhoenixBaseScraper,args=(betPhoenixAPIUrls,masterdata))
	p3.start()
	p4=Process(target=skyBookBaseScraper,args=(skyBookAPIUrls,masterdata))
	p4.start()







	p.join()
	#p1.join()
	p2.join()
	p3.join()
	p4.join()
	spreadData=[]
	for key in masterdata:
		entry={}
		if len(masterdata[key])<2:
		       continue
		entry['AwayTeam']=masterdata[key][0]['AwayTeam'][2:-1].title()
		entry['HomeTeam']=masterdata[key][0]['HomeTeam'][2:-1].title()
		
		for key1 in masterdata[key]:
			if key1['LineType']=="Match":
				bookName=key1['SportsBook']
				try:
					entry[bookName+"OverPoints"]=key1['OverPoints']
					entry[bookName+"OverLine"]=round(float(key1['OverLine']),2)
					entry[bookName+"UnderPoints"]=key1['UnderPoints']
					entry[bookName+"UnderLine"]=round(float(key1['UnderLine']),2)
				except KeyError: pass
		spreadData.append(entry)
			
		
	output=json.dumps(spreadData)
	return output

@app.route('/api/v1/resources/nba/match/spreads/decimal', methods=['GET'])
def nbaSpreadDecimal():
	league='nba'
	manager=Manager()
	masterdata=manager.dict()
	IntertopsBaseURLs='https://sports.intertops.eu/en/Bets/Basketball/NBA-Lines/1070'
	bovadaAPIUrls='https://services.bovada.lv/services/sports/event/coupon/events/A/description/basketball?marketFilterId=def&preMatchOnly=true&eventsLimit=50&lang=en'
	betPhoenixAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111207169812656759593_1577303361038&hid=bdb01c9f736f2e641984fcde2fce11ad&cmd=games&leagues=3&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577303361039'
	skyBookAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111206009097206260869_1577542998571&hid=e154acf7203ae1251e181abf8aca82a7&cmd=games&leagues=3&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577542998572'
	#SportBetReducedURLS='https://www.sportbet.com/lines/Basketball/Reduced/'


	p=Process(target=intertopsBaseScraper,args=(IntertopsBaseURLs,masterdata))
	p.start()
	#p1=Process(target=sportBetBaseScraper,args=(SportBetReducedURLS,masterdata))
	#p1.start()
	p2=Process(target=bovadaBaseScraper,args=(bovadaAPIUrls,masterdata))
	p2.start()
	p3=Process(target=betPhoenixBaseScraper,args=(betPhoenixAPIUrls,masterdata))
	p3.start()
	p4=Process(target=skyBookBaseScraper,args=(skyBookAPIUrls,masterdata))
	p4.start()







	p.join()
	#p1.join()
	p2.join()
	p3.join()
	p4.join()
	spreadData=[]
	for key in masterdata:
		entry={}
		if len(masterdata[key])<2:
		       continue
		entry['AwayTeam']=masterdata[key][0]['AwayTeam'][2:-1].title()
		entry['HomeTeam']=masterdata[key][0]['HomeTeam'][2:-1].title()
		
		for key1 in masterdata[key]:
			if key1['LineType']=="Match":
				bookName=key1['SportsBook']
				try:
					entry[bookName+"AwayPointSpread"]=key1['AwayTeamPointSpread']
					entry[bookName+"AwayPointLine"]=round(float(key1['AwayTeamPointLine']),2)
					entry[bookName+"HomePointSpread"]=key1['HomeTeamPointSpread']
					entry[bookName+"HomePointLine"]=round(float(key1['HomeTeamPointLine']),2)
				except KeyError: pass
		spreadData.append(entry)
			
		
	output=json.dumps(spreadData)
	return output

@app.route('/api/v1/resources/ncaab/match/totals/decimal', methods=['GET'])
def ncaabTotalsDecimal():
	league='ncaab'
	manager=Manager()
	masterdata=manager.dict()
	IntertopsBaseURLs='https://sports.intertops.eu/en/Bets/Basketball/NCAAB-Lines/1068'
	bovadaAPIUrls='https://services.bovada.lv/services/sports/event/coupon/events/A/description/basketball?marketFilterId=def&preMatchOnly=true&eventsLimit=50&lang=en'
	betPhoenixAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111207169812656759593_1577303361038&hid=bdb01c9f736f2e641984fcde2fce11ad&cmd=games&leagues=4&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577303361039'
	skyBookAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111206009097206260869_1577542998571&hid=e154acf7203ae1251e181abf8aca82a7&cmd=games&leagues=4&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577542998572'
	#SportBetReducedURLS='https://www.sportbet.com/lines/Basketball/Reduced/'
	betPhoenixAPIUrls2='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111207169812656759593_1577303361038&hid=bdb01c9f736f2e641984fcde2fce11ad&cmd=games&leagues=741&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577303361039'
	skyBookAPIUrls2='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111206009097206260869_1577542998571&hid=e154acf7203ae1251e181abf8aca82a7&cmd=games&leagues=741&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577542998572'
	

	p=Process(target=intertopsBaseScraper,args=(IntertopsBaseURLs,masterdata))
	p.start()
	#p1=Process(target=sportBetBaseScraper,args=(SportBetReducedURLS,masterdata))
	#p1.start()
	p2=Process(target=bovadaBaseScraper,args=(bovadaAPIUrls,masterdata))
	p2.start()
	p3=Process(target=betPhoenixBaseScraper,args=(betPhoenixAPIUrls,masterdata))
	p3.start()
	p4=Process(target=skyBookBaseScraper,args=(skyBookAPIUrls,masterdata))
	p4.start()
	p5=Process(target=betPhoenixBaseScraper,args=(betPhoenixAPIUrls2,masterdata))
	p5.start()
	p6=Process(target=skyBookBaseScraper,args=(skyBookAPIUrls2,masterdata))
	p6.start()





	p.join()
	#p1.join()
	p2.join()
	p3.join()
	p4.join()
	p5.join()
	p6.join()
	spreadData=[]
	for key in masterdata:
		entry={}
		if len(masterdata[key])<2:
		       continue
		entry['AwayTeam']=masterdata[key][0]['AwayTeam'][2:-1].title()
		entry['HomeTeam']=masterdata[key][0]['HomeTeam'][2:-1].title()
		
		for key1 in masterdata[key]:
			if key1['LineType']=="Match":
				bookName=key1['SportsBook']
				try:
					entry[bookName+"OverPoints"]=key1['OverPoints']
					entry[bookName+"OverLine"]=round(float(key1['OverLine']),2)
					entry[bookName+"UnderPoints"]=key1['UnderPoints']
					entry[bookName+"UnderLine"]=round(float(key1['UnderLine']),2)
				except KeyError: pass
		spreadData.append(entry)
	output=json.dumps(spreadData)
	return output

@app.route('/api/v1/resources/ncaab/match/moneyline/american', methods=['GET'])
def ncaabMoneyLineAmerican():
	league='ncaab'
	manager=Manager()
	masterdata=manager.dict()
	IntertopsBaseURLs='https://sports.intertops.eu/en/Bets/Basketball/NCAAB-Lines/1068'
	bovadaAPIUrls='https://services.bovada.lv/services/sports/event/coupon/events/A/description/basketball?marketFilterId=def&preMatchOnly=true&eventsLimit=50&lang=en'
	betPhoenixAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111207169812656759593_1577303361038&hid=bdb01c9f736f2e641984fcde2fce11ad&cmd=games&leagues=4&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577303361039'
	skyBookAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111206009097206260869_1577542998571&hid=e154acf7203ae1251e181abf8aca82a7&cmd=games&leagues=4&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577542998572'
	#SportBetReducedURLS='https://www.sportbet.com/lines/Basketball/Reduced/'
	betPhoenixAPIUrls2='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111207169812656759593_1577303361038&hid=bdb01c9f736f2e641984fcde2fce11ad&cmd=games&leagues=741&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577303361039'
	skyBookAPIUrls2='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111206009097206260869_1577542998571&hid=e154acf7203ae1251e181abf8aca82a7&cmd=games&leagues=741&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577542998572'
	

	p=Process(target=intertopsBaseScraper,args=(IntertopsBaseURLs,masterdata))
	p.start()
	#p1=Process(target=sportBetBaseScraper,args=(SportBetReducedURLS,masterdata))
	#p1.start()
	p2=Process(target=bovadaBaseScraper,args=(bovadaAPIUrls,masterdata))
	p2.start()
	p3=Process(target=betPhoenixBaseScraper,args=(betPhoenixAPIUrls,masterdata))
	p3.start()
	p4=Process(target=skyBookBaseScraper,args=(skyBookAPIUrls,masterdata))
	p4.start()
	p5=Process(target=betPhoenixBaseScraper,args=(betPhoenixAPIUrls2,masterdata))
	p5.start()
	p6=Process(target=skyBookBaseScraper,args=(skyBookAPIUrls2,masterdata))
	p6.start()





	p.join()
	#p1.join()
	p2.join()
	p3.join()
	p4.join()
	p5.join()
	p6.join()
	spreadData=[]
	for key in masterdata:
		entry={}
		if len(masterdata[key])<2:
		       continue
		entry['AwayTeam']=masterdata[key][0]['AwayTeam'][2:-1].title()
		entry['HomeTeam']=masterdata[key][0]['HomeTeam'][2:-1].title()
		
		for key1 in masterdata[key]:
			if key1['LineType']=="Match":
				bookName=key1['SportsBook']
				try:
					entry[bookName+"AwayTeamMoneyLine"]=key1['AwayTeamMoneyLineAmerican']

					entry[bookName+"HomeTeamMoneyLine"]=key1['HomeTeamMoneyLineAmerican']
				except KeyError:pass
		spreadData.append(entry)
	output=json.dumps(spreadData)
	return output

@app.route('/api/v1/resources/ncaab/match/moneyline/decimal', methods=['GET'])
def ncaabMoneyLineDecimal():
	league='ncaab'
	manager=Manager()
	masterdata=manager.dict()
	IntertopsBaseURLs='https://sports.intertops.eu/en/Bets/Basketball/NCAAB-Lines/1068'
	bovadaAPIUrls='https://services.bovada.lv/services/sports/event/coupon/events/A/description/basketball?marketFilterId=def&preMatchOnly=true&eventsLimit=50&lang=en'
	betPhoenixAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111207169812656759593_1577303361038&hid=bdb01c9f736f2e641984fcde2fce11ad&cmd=games&leagues=4&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577303361039'
	skyBookAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111206009097206260869_1577542998571&hid=e154acf7203ae1251e181abf8aca82a7&cmd=games&leagues=4&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577542998572'
	#SportBetReducedURLS='https://www.sportbet.com/lines/Basketball/Reduced/'
	betPhoenixAPIUrls2='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111207169812656759593_1577303361038&hid=bdb01c9f736f2e641984fcde2fce11ad&cmd=games&leagues=741&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577303361039'
	skyBookAPIUrls2='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111206009097206260869_1577542998571&hid=e154acf7203ae1251e181abf8aca82a7&cmd=games&leagues=741&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577542998572'
	

	p=Process(target=intertopsBaseScraper,args=(IntertopsBaseURLs,masterdata))
	p.start()
	#p1=Process(target=sportBetBaseScraper,args=(SportBetReducedURLS,masterdata))
	#p1.start()
	p2=Process(target=bovadaBaseScraper,args=(bovadaAPIUrls,masterdata))
	p2.start()
	p3=Process(target=betPhoenixBaseScraper,args=(betPhoenixAPIUrls,masterdata))
	p3.start()
	p4=Process(target=skyBookBaseScraper,args=(skyBookAPIUrls,masterdata))
	p4.start()
	p5=Process(target=betPhoenixBaseScraper,args=(betPhoenixAPIUrls2,masterdata))
	p5.start()
	p6=Process(target=skyBookBaseScraper,args=(skyBookAPIUrls2,masterdata))
	p6.start()





	p.join()
	#p1.join()
	p2.join()
	p3.join()
	p4.join()
	p5.join()
	p6.join()
	spreadData=[]
	for key in masterdata:
		entry={}
		if len(masterdata[key])<2:
		       continue
		entry['AwayTeam']=masterdata[key][0]['AwayTeam'][2:-1].title()
		entry['HomeTeam']=masterdata[key][0]['HomeTeam'][2:-1].title()
		
		for key1 in masterdata[key]:
			if key1['LineType']=="Match":
				bookName=key1['SportsBook']
				try:
					entry[bookName+"AwayTeamMoneyLine"]=round(float(key1['AwayTeamMoneyLine']),2)

					entry[bookName+"HomeTeamMoneyLine"]=round(float(key1['HomeTeamMoneyLine']),2)
				except KeyError: pass
		spreadData.append(entry)
	output=json.dumps(spreadData)
	return output

@app.route('/api/v1/resources/ncaab/match/totals/american', methods=['GET'])
def ncaabTotalsAmerican():
	league='ncaab'
	manager=Manager()
	masterdata=manager.dict()
	IntertopsBaseURLs='https://sports.intertops.eu/en/Bets/Basketball/NCAAB-Lines/1068'
	bovadaAPIUrls='https://services.bovada.lv/services/sports/event/coupon/events/A/description/basketball?marketFilterId=def&preMatchOnly=true&eventsLimit=50&lang=en'
	betPhoenixAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111207169812656759593_1577303361038&hid=bdb01c9f736f2e641984fcde2fce11ad&cmd=games&leagues=4&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577303361039'
	skyBookAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111206009097206260869_1577542998571&hid=e154acf7203ae1251e181abf8aca82a7&cmd=games&leagues=4&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577542998572'
	#SportBetReducedURLS='https://www.sportbet.com/lines/Basketball/Reduced/'
	betPhoenixAPIUrls2='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111207169812656759593_1577303361038&hid=bdb01c9f736f2e641984fcde2fce11ad&cmd=games&leagues=741&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577303361039'
	skyBookAPIUrls2='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111206009097206260869_1577542998571&hid=e154acf7203ae1251e181abf8aca82a7&cmd=games&leagues=741&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577542998572'
	

	p=Process(target=intertopsBaseScraper,args=(IntertopsBaseURLs,masterdata))
	p.start()
	#p1=Process(target=sportBetBaseScraper,args=(SportBetReducedURLS,masterdata))
	#p1.start()
	p2=Process(target=bovadaBaseScraper,args=(bovadaAPIUrls,masterdata))
	p2.start()
	p3=Process(target=betPhoenixBaseScraper,args=(betPhoenixAPIUrls,masterdata))
	p3.start()
	p4=Process(target=skyBookBaseScraper,args=(skyBookAPIUrls,masterdata))
	p4.start()
	p5=Process(target=betPhoenixBaseScraper,args=(betPhoenixAPIUrls2,masterdata))
	p5.start()
	p6=Process(target=skyBookBaseScraper,args=(skyBookAPIUrls2,masterdata))
	p6.start()





	p.join()
	#p1.join()
	p2.join()
	p3.join()
	p4.join()
	p5.join()
	p6.join()
	spreadData=[]
	for key in masterdata:
		entry={}
		if len(masterdata[key])<2:
		       continue
		entry['AwayTeam']=masterdata[key][0]['AwayTeam'][2:-1].title()
		entry['HomeTeam']=masterdata[key][0]['HomeTeam'][2:-1].title()
		
		for key1 in masterdata[key]:
			if key1['LineType']=="Match":
				bookName=key1['SportsBook']
				try:
					entry[bookName+"OverPoints"]=key1['OverPoints']
					entry[bookName+"OverLine"]=key1['OverLineAmerican']
					entry[bookName+"UnderPoints"]=key1['UnderPoints']
					entry[bookName+"UnderLine"]=key1['UnderLineAmerican']
				except KeyError: pass
		spreadData.append(entry)
		
	output=json.dumps(spreadData)
	return output


@app.route('/api/v1/resources/ncaab/match/spreads/american', methods=['GET'])
def ncaabSpreadAmerican():
	league='ncaab'
	manager=Manager()
	masterdata=manager.dict()
	IntertopsBaseURLs='https://sports.intertops.eu/en/Bets/Basketball/NCAAB-Lines/1068'
	bovadaAPIUrls='https://services.bovada.lv/services/sports/event/coupon/events/A/description/basketball?marketFilterId=def&preMatchOnly=true&eventsLimit=50&lang=en'
	betPhoenixAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111207169812656759593_1577303361038&hid=bdb01c9f736f2e641984fcde2fce11ad&cmd=games&leagues=4&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577303361039'
	skyBookAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111206009097206260869_1577542998571&hid=e154acf7203ae1251e181abf8aca82a7&cmd=games&leagues=4&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577542998572'
	#SportBetReducedURLS='https://www.sportbet.com/lines/Basketball/Reduced/'
	betPhoenixAPIUrls2='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111207169812656759593_1577303361038&hid=bdb01c9f736f2e641984fcde2fce11ad&cmd=games&leagues=741&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577303361039'
	skyBookAPIUrls2='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111206009097206260869_1577542998571&hid=e154acf7203ae1251e181abf8aca82a7&cmd=games&leagues=741&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577542998572'
	

	p=Process(target=intertopsBaseScraper,args=(IntertopsBaseURLs,masterdata))
	p.start()
	#p1=Process(target=sportBetBaseScraper,args=(SportBetReducedURLS,masterdata))
	#p1.start()
	p2=Process(target=bovadaBaseScraper,args=(bovadaAPIUrls,masterdata))
	p2.start()
	p3=Process(target=betPhoenixBaseScraper,args=(betPhoenixAPIUrls,masterdata))
	p3.start()
	p4=Process(target=skyBookBaseScraper,args=(skyBookAPIUrls,masterdata))
	p4.start()
	p5=Process(target=betPhoenixBaseScraper,args=(betPhoenixAPIUrls2,masterdata))
	p5.start()
	p6=Process(target=skyBookBaseScraper,args=(skyBookAPIUrls2,masterdata))
	p6.start()





	p.join()
	#p1.join()
	p2.join()
	p3.join()
	p4.join()
	p5.join()
	p6.join()
	spreadData=[]
	for key in masterdata:
		entry={}
		if len(masterdata[key])<2:
		       continue
		entry['AwayTeam']=masterdata[key][0]['AwayTeam'][2:-1].title()
		entry['HomeTeam']=masterdata[key][0]['HomeTeam'][2:-1].title()
		
		for key1 in masterdata[key]:
			if key1['LineType']=="Match":
				bookName=key1['SportsBook']
				try:
					entry[bookName+"AwayPointSpread"]=key1['AwayTeamPointSpread']
					entry[bookName+"AwayPointLine"]=key1['AwayTeamPointLineAmerican']
					entry[bookName+"HomePointSpread"]=key1['HomeTeamPointSpread']
					entry[bookName+"HomePointLine"]=key1['HomeTeamPointLineAmerican']
				except KeyError: pass
		spreadData.append(entry)
	output=json.dumps(spreadData)
	return output

@app.route('/api/v1/resources/ncaab/match/spreads/decimal', methods=['GET'])
def ncaabSpreadDecimal():
	league='ncaab'
	manager=Manager()
	masterdata=manager.dict()
	IntertopsBaseURLs='https://sports.intertops.eu/en/Bets/Basketball/NCAAB-Lines/1068'
	bovadaAPIUrls='https://services.bovada.lv/services/sports/event/coupon/events/A/description/basketball?marketFilterId=def&preMatchOnly=true&eventsLimit=50&lang=en'
	betPhoenixAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111207169812656759593_1577303361038&hid=bdb01c9f736f2e641984fcde2fce11ad&cmd=games&leagues=4&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577303361039'
	skyBookAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111206009097206260869_1577542998571&hid=e154acf7203ae1251e181abf8aca82a7&cmd=games&leagues=4&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577542998572'
	#SportBetReducedURLS='https://www.sportbet.com/lines/Basketball/Reduced/'
	betPhoenixAPIUrls2='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111207169812656759593_1577303361038&hid=bdb01c9f736f2e641984fcde2fce11ad&cmd=games&leagues=741&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577303361039'
	skyBookAPIUrls2='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111206009097206260869_1577542998571&hid=e154acf7203ae1251e181abf8aca82a7&cmd=games&leagues=741&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577542998572'
	

	p=Process(target=intertopsBaseScraper,args=(IntertopsBaseURLs,masterdata))
	p.start()
	#p1=Process(target=sportBetBaseScraper,args=(SportBetReducedURLS,masterdata))
	#p1.start()
	p2=Process(target=bovadaBaseScraper,args=(bovadaAPIUrls,masterdata))
	p2.start()
	p3=Process(target=betPhoenixBaseScraper,args=(betPhoenixAPIUrls,masterdata))
	p3.start()
	p4=Process(target=skyBookBaseScraper,args=(skyBookAPIUrls,masterdata))
	p4.start()
	p5=Process(target=betPhoenixBaseScraper,args=(betPhoenixAPIUrls2,masterdata))
	p5.start()
	p6=Process(target=skyBookBaseScraper,args=(skyBookAPIUrls2,masterdata))
	p6.start()





	p.join()
	#p1.join()
	p2.join()
	p3.join()
	p4.join()
	p5.join()
	p6.join()
	spreadData=[]
	for key in masterdata:
		entry={}
		if len(masterdata[key])<2:
		       continue
		entry['AwayTeam']=masterdata[key][0]['AwayTeam'][2:-1].title()
		entry['HomeTeam']=masterdata[key][0]['HomeTeam'][2:-1].title()
		
		for key1 in masterdata[key]:
			if key1['LineType']=="Match":
				bookName=key1['SportsBook']
				try:
					entry[bookName+"AwayPointSpread"]=key1['AwayTeamPointSpread']
					entry[bookName+"AwayPointLine"]=round(float(key1['AwayTeamPointLine']),2)
					entry[bookName+"HomePointSpread"]=key1['HomeTeamPointSpread']
					entry[bookName+"HomePointLine"]=round(float(key1['HomeTeamPointLine']),2)
				except KeyError: pass
		spreadData.append(entry)
		
	output=json.dumps(spreadData)
	return output

@app.route('/api/v1/resources/ufc/match/moneyline/american', methods=['GET'])
def ufcMoneyLineAmerican():	
	
	league='ufc'
	manager=Manager()
	masterdata=manager.dict()
	
	bovadaAPIUrls='https://services.bovada.lv/services/sports/event/coupon/events/A/description/ufc-mma?marketFilterId=def&preMatchOnly=true&eventsLimit=50&lang=en'
	betPhoenixAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111207169812656759593_1577303361038&hid=bdb01c9f736f2e641984fcde2fce11ad&cmd=games&leagues=32&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577303361039'
	skyBookAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111206009097206260869_1577542998571&hid=e154acf7203ae1251e181abf8aca82a7&cmd=games&leagues=32&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577542998572'
	#SportBetReducedURLS='https://www.sportbet.com/lines/Fighting/Reduced/'


	
	#p1=Process(target=sportBetBaseScraper,args=(SportBetReducedURLS,masterdata))
	#p1.start()
	p2=Process(target=bovadaBaseScraper,args=(bovadaAPIUrls,masterdata))
	p2.start()
	p3=Process(target=betPhoenixBaseScraper,args=(betPhoenixAPIUrls,masterdata))
	p3.start()
	p4=Process(target=skyBookBaseScraper,args=(skyBookAPIUrls,masterdata))
	p4.start()







	
	#p1.join()
	p2.join()
	p3.join()
	p4.join()
	spreadData=[]
	for key in masterdata:
		entry={}
		if len(masterdata[key])<2:
		       continue
		entry['AwayTeam']=masterdata[key][0]['AwayTeam'][2:-1].title()
		entry['HomeTeam']=masterdata[key][0]['HomeTeam'][2:-1].title()
		
		for key1 in masterdata[key]:
			if key1['LineType']=="Match":
				bookName=key1['SportsBook']
				try:
					entry[bookName+"AwayTeamMoneyLine"]=key1['AwayTeamMoneyLineAmerican']

					entry[bookName+"HomeTeamMoneyLine"]=key1['HomeTeamMoneyLineAmerican']
				except KeyError:pass
		spreadData.append(entry)
	output=json.dumps(spreadData)
	return output

@app.route('/api/v1/resources/ufc/match/moneyline/decimal', methods=['GET'])
def ufcMoneyLineDecimal():	
	
	league='ufc'
	manager=Manager()
	masterdata=manager.dict()
	
	bovadaAPIUrls='https://services.bovada.lv/services/sports/event/coupon/events/A/description/ufc-mma?marketFilterId=def&preMatchOnly=true&eventsLimit=50&lang=en'
	betPhoenixAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111207169812656759593_1577303361038&hid=bdb01c9f736f2e641984fcde2fce11ad&cmd=games&leagues=32&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577303361039'
	skyBookAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111206009097206260869_1577542998571&hid=e154acf7203ae1251e181abf8aca82a7&cmd=games&leagues=32&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577542998572'
	#SportBetReducedURLS='https://www.sportbet.com/lines/Fighting/Reduced/'


	
	#p1=Process(target=sportBetBaseScraper,args=(SportBetReducedURLS,masterdata))
	#p1.start()
	p2=Process(target=bovadaBaseScraper,args=(bovadaAPIUrls,masterdata))
	p2.start()
	p3=Process(target=betPhoenixBaseScraper,args=(betPhoenixAPIUrls,masterdata))
	p3.start()
	p4=Process(target=skyBookBaseScraper,args=(skyBookAPIUrls,masterdata))
	p4.start()







	
	#p1.join()
	p2.join()
	p3.join()
	p4.join()
	spreadData=[]
	for key in masterdata:
		entry={}
		if len(masterdata[key])<2:
		       continue
		entry['AwayTeam']=masterdata[key][0]['AwayTeam'][2:-1].title()
		entry['HomeTeam']=masterdata[key][0]['HomeTeam'][2:-1].title()
		
		for key1 in masterdata[key]:
			if key1['LineType']=="Match":
				bookName=key1['SportsBook']
				try:
					entry[bookName+"AwayTeamMoneyLine"]=round(float(key1['AwayTeamMoneyLine']),2)

					entry[bookName+"HomeTeamMoneyLine"]=round(float(key1['HomeTeamMoneyLine']),2)
				except KeyError:pass
		spreadData.append(entry)
	output=json.dumps(spreadData)
	return output

@app.route('/api/v1/resources/boxing/match/moneyline/american', methods=['GET'])
def boxingMoneyLineAmerican():	
	
	league='boxing'
	manager=Manager()
	masterdata=manager.dict()
	
	bovadaAPIUrls='https://services.bovada.lv/services/sports/event/coupon/events/A/description/boxing?marketFilterId=def&preMatchOnly=true&eventsLimit=50&lang=en'
	betPhoenixAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111207169812656759593_1577303361038&hid=bdb01c9f736f2e641984fcde2fce11ad&cmd=games&leagues=10&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577303361039'
	skyBookAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111206009097206260869_1577542998571&hid=e154acf7203ae1251e181abf8aca82a7&cmd=games&leagues=10&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577542998572'
	#SportBetReducedURLS='https://www.sportbet.com/lines/Fighting/Reduced/'


	
	#p1=Process(target=sportBetBaseScraper,args=(SportBetReducedURLS,masterdata))
	#p1.start()
	p2=Process(target=bovadaBaseScraper,args=(bovadaAPIUrls,masterdata))
	p2.start()
	p3=Process(target=betPhoenixBaseScraper,args=(betPhoenixAPIUrls,masterdata))
	p3.start()
	p4=Process(target=skyBookBaseScraper,args=(skyBookAPIUrls,masterdata))
	p4.start()







	
	#p1.join()
	p2.join()
	p3.join()
	p4.join()
	return masterdata
	spreadData=[]
	for key in masterdata:
		entry={}
		#if len(masterdata[key])<2:
		#       continue
		entry['AwayTeam']=masterdata[key][0]['AwayTeam'][2:-1].title()
		entry['HomeTeam']=masterdata[key][0]['HomeTeam'][2:-1].title()
		
		for key1 in masterdata[key]:
			if key1['LineType']=="Match":
				bookName=key1['SportsBook']
				try:
					entry[bookName+"AwayTeamMoneyLine"]=key1['AwayTeamMoneyLineAmerican']

					entry[bookName+"HomeTeamMoneyLine"]=key1['HomeTeamMoneyLineAmerican']
				except KeyError: pass
		spreadData.append(entry)
	output=json.dumps(spreadData)
	return output

@app.route('/api/v1/resources/boxing/match/moneyline/decimal', methods=['GET'])
def boxingMoneyLineDecimal():	
	
	league='boxing'
	manager=Manager()
	masterdata=manager.dict()
	
	bovadaAPIUrls='https://services.bovada.lv/services/sports/event/coupon/events/A/description/boxing?marketFilterId=def&preMatchOnly=true&eventsLimit=50&lang=en'
	betPhoenixAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111207169812656759593_1577303361038&hid=bdb01c9f736f2e641984fcde2fce11ad&cmd=games&leagues=10&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577303361039'
	skyBookAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111206009097206260869_1577542998571&hid=e154acf7203ae1251e181abf8aca82a7&cmd=games&leagues=10&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577542998572'
	#SportBetReducedURLS='https://www.sportbet.com/lines/Fighting/Reduced/'


	
	#p1=Process(target=sportBetBaseScraper,args=(SportBetReducedURLS,masterdata))
	#p1.start()
	p2=Process(target=bovadaBaseScraper,args=(bovadaAPIUrls,masterdata))
	p2.start()
	p3=Process(target=betPhoenixBaseScraper,args=(betPhoenixAPIUrls,masterdata))
	p3.start()
	p4=Process(target=skyBookBaseScraper,args=(skyBookAPIUrls,masterdata))
	p4.start()







	
	#p1.join()
	p2.join()
	p3.join()
	p4.join()
	spreadData=[]
	for key in masterdata:
		entry={}
		if len(masterdata[key])<2:
		       continue
		entry['AwayTeam']=masterdata[key][0]['AwayTeam'][2:-1].title()
		entry['HomeTeam']=masterdata[key][0]['HomeTeam'][2:-1].title()
		
		for key1 in masterdata[key]:
			if key1['LineType']=="Match":
				bookName=key1['SportsBook']
				try:
					entry[bookName+"AwayTeamMoneyLine"]=round(float(key1['AwayTeamMoneyLine']),2)

					entry[bookName+"HomeTeamMoneyLine"]=round(float(key1['HomeTeamMoneyLine']),2)
				except KeyError:pass
		spreadData.append(entry)
	output=json.dumps(spreadData)
	return output

@app.route('/api/v1/resources/nhl/match/spreads/decimal', methods=['GET'])
def nhlSpreadDecimal():	
	
	league='nhl'
	manager=Manager()
	masterdata=manager.dict()
	IntertopsBaseURLs='https://sports.intertops.eu/en/Bets/Ice-Hockey/NHL-Lines/1064'
	bovadaAPIUrls='https://services.bovada.lv/services/sports/event/coupon/events/A/description/hockey?marketFilterId=def&preMatchOnly=true&eventsLimit=50&lang=en'
	betPhoenixAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111207169812656759593_1577303361038&hid=bdb01c9f736f2e641984fcde2fce11ad&cmd=games&leagues=7&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577303361039'
	skyBookAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111206009097206260869_1577542998571&hid=e154acf7203ae1251e181abf8aca82a7&cmd=games&leagues=7&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577542998572'
	#SportBetReducedURLS='https://www.sportbet.com/lines/Hockey/Reduced/'


	p=Process(target=intertopsBaseScraper,args=(IntertopsBaseURLs,masterdata))
	p.start()
	#p1=Process(target=sportBetBaseScraper,args=(SportBetReducedURLS,masterdata))
	#p1.start()
	p2=Process(target=bovadaBaseScraper,args=(bovadaAPIUrls,masterdata))
	p2.start()
	p3=Process(target=betPhoenixBaseScraper,args=(betPhoenixAPIUrls,masterdata))
	p3.start()
	p4=Process(target=skyBookBaseScraper,args=(skyBookAPIUrls,masterdata))
	p4.start()







	p.join()
	#p1.join()
	p2.join()
	p3.join()
	p4.join()
	spreadData=[]
	for key in masterdata:
		entry={}
		if len(masterdata[key])<2:
		       continue
		entry['AwayTeam']=masterdata[key][0]['AwayTeam'][2:-1].title()
		entry['HomeTeam']=masterdata[key][0]['HomeTeam'][2:-1].title()
		
		for key1 in masterdata[key]:
			if key1['LineType']=="Match":
				bookName=key1['SportsBook']
				try:
					entry[bookName+"AwayPointSpread"]=key1['AwayTeamPointSpread']
					entry[bookName+"AwayPointLine"]=round(float(key1['AwayTeamPointLine']),2)
					entry[bookName+"HomePointSpread"]=key1['HomeTeamPointSpread']
					entry[bookName+"HomePointLine"]=round(float(key1['HomeTeamPointLine']),2)
				except KeyError: pass
		spreadData.append(entry)
	
	output=json.dumps(spreadData)
	return output

@app.route('/api/v1/resources/nhl/match/spreads/american', methods=['GET'])
def nhlSpreadAmerican():	
	
	league='nhl'
	manager=Manager()
	masterdata=manager.dict()
	IntertopsBaseURLs='https://sports.intertops.eu/en/Bets/Ice-Hockey/NHL-Lines/1064'
	bovadaAPIUrls='https://services.bovada.lv/services/sports/event/coupon/events/A/description/hockey?marketFilterId=def&preMatchOnly=true&eventsLimit=50&lang=en'
	betPhoenixAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111207169812656759593_1577303361038&hid=bdb01c9f736f2e641984fcde2fce11ad&cmd=games&leagues=7&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577303361039'
	skyBookAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111206009097206260869_1577542998571&hid=e154acf7203ae1251e181abf8aca82a7&cmd=games&leagues=7&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577542998572'
	#SportBetReducedURLS='https://www.sportbet.com/lines/Hockey/Reduced/'


	p=Process(target=intertopsBaseScraper,args=(IntertopsBaseURLs,masterdata))
	p.start()
	#p1=Process(target=sportBetBaseScraper,args=(SportBetReducedURLS,masterdata))
	#p1.start()
	p2=Process(target=bovadaBaseScraper,args=(bovadaAPIUrls,masterdata))
	p2.start()
	p3=Process(target=betPhoenixBaseScraper,args=(betPhoenixAPIUrls,masterdata))
	p3.start()
	p4=Process(target=skyBookBaseScraper,args=(skyBookAPIUrls,masterdata))
	p4.start()







	p.join()
	#p1.join()
	p2.join()
	p3.join()
	p4.join()
	spreadData=[]
	for key in masterdata:
		entry={}
		if len(masterdata[key])<2:
		       continue
		entry['AwayTeam']=masterdata[key][0]['AwayTeam'][2:-1].title()
		entry['HomeTeam']=masterdata[key][0]['HomeTeam'][2:-1].title()
		
		for key1 in masterdata[key]:
			if key1['LineType']=="Match":
				bookName=key1['SportsBook']
				try:
					entry[bookName+"AwayPointSpread"]=key1['AwayTeamPointSpread']
					entry[bookName+"AwayPointLine"]=key1['AwayTeamPointLineAmerican']
					entry[bookName+"HomePointSpread"]=key1['HomeTeamPointSpread']
					entry[bookName+"HomePointLine"]=key1['HomeTeamPointLineAmerican']
				except KeyError: pass
		spreadData.append(entry)
	output=json.dumps(spreadData)
	return output

@app.route('/api/v1/resources/nhl/match/moneyline/decimal', methods=['GET'])
def nhlMoneyLineDecimal():	
	
	league='nhl'
	manager=Manager()
	masterdata=manager.dict()
	IntertopsBaseURLs='https://sports.intertops.eu/en/Bets/Ice-Hockey/NHL-Lines/1064'
	bovadaAPIUrls='https://services.bovada.lv/services/sports/event/coupon/events/A/description/hockey?marketFilterId=def&preMatchOnly=true&eventsLimit=50&lang=en'
	betPhoenixAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111207169812656759593_1577303361038&hid=bdb01c9f736f2e641984fcde2fce11ad&cmd=games&leagues=7&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577303361039'
	skyBookAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111206009097206260869_1577542998571&hid=e154acf7203ae1251e181abf8aca82a7&cmd=games&leagues=7&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577542998572'
	#SportBetReducedURLS='https://www.sportbet.com/lines/Hockey/Reduced/'


	p=Process(target=intertopsBaseScraper,args=(IntertopsBaseURLs,masterdata))
	p.start()
	#p1=Process(target=sportBetBaseScraper,args=(SportBetReducedURLS,masterdata))
	#p1.start()
	p2=Process(target=bovadaBaseScraper,args=(bovadaAPIUrls,masterdata))
	p2.start()
	p3=Process(target=betPhoenixBaseScraper,args=(betPhoenixAPIUrls,masterdata))
	p3.start()
	p4=Process(target=skyBookBaseScraper,args=(skyBookAPIUrls,masterdata))
	p4.start()







	p.join()
	#p1.join()
	p2.join()
	p3.join()
	p4.join()
	spreadData=[]
	for key in masterdata:
		entry={}
		if len(masterdata[key])<2:
		       continue
		entry['AwayTeam']=masterdata[key][0]['AwayTeam'][2:-1].title()
		entry['HomeTeam']=masterdata[key][0]['HomeTeam'][2:-1].title()
		
		for key1 in masterdata[key]:
			if key1['LineType']=="Match":
				bookName=key1['SportsBook']
				try:
					entry[bookName+"AwayTeamMoneyLine"]=round(float(key1['AwayTeamMoneyLine']),2)

					entry[bookName+"HomeTeamMoneyLine"]=round(float(key1['HomeTeamMoneyLine']),2)
				except KeyError: pass
		spreadData.append(entry)
	output=json.dumps(spreadData)
	return output

@app.route('/api/v1/resources/nhl/match/moneyline/american', methods=['GET'])
def nhlMoneyLineAmerican():	
	
	league='nhl'
	manager=Manager()
	masterdata=manager.dict()
	IntertopsBaseURLs='https://sports.intertops.eu/en/Bets/Ice-Hockey/NHL-Lines/1064'
	bovadaAPIUrls='https://services.bovada.lv/services/sports/event/coupon/events/A/description/hockey?marketFilterId=def&preMatchOnly=true&eventsLimit=50&lang=en'
	betPhoenixAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111207169812656759593_1577303361038&hid=bdb01c9f736f2e641984fcde2fce11ad&cmd=games&leagues=7&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577303361039'
	skyBookAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111206009097206260869_1577542998571&hid=e154acf7203ae1251e181abf8aca82a7&cmd=games&leagues=7&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577542998572'
	#SportBetReducedURLS='https://www.sportbet.com/lines/Hockey/Reduced/'


	p=Process(target=intertopsBaseScraper,args=(IntertopsBaseURLs,masterdata))
	p.start()
	#p1=Process(target=sportBetBaseScraper,args=(SportBetReducedURLS,masterdata))
	#p1.start()
	p2=Process(target=bovadaBaseScraper,args=(bovadaAPIUrls,masterdata))
	p2.start()
	p3=Process(target=betPhoenixBaseScraper,args=(betPhoenixAPIUrls,masterdata))
	p3.start()
	p4=Process(target=skyBookBaseScraper,args=(skyBookAPIUrls,masterdata))
	p4.start()







	p.join()
	#p1.join()
	p2.join()
	p3.join()
	p4.join()
	spreadData=[]
	for key in masterdata:
		entry={}
		if len(masterdata[key])<2:
		       continue
		entry['AwayTeam']=masterdata[key][0]['AwayTeam'][2:-1].title()
		entry['HomeTeam']=masterdata[key][0]['HomeTeam'][2:-1].title()
		
		for key1 in masterdata[key]:
			if key1['LineType']=="Match":
				bookName=key1['SportsBook']
				try:
					entry[bookName+"AwayTeamMoneyLine"]=key1['AwayTeamMoneyLineAmerican']

					entry[bookName+"HomeTeamMoneyLine"]=key1['HomeTeamMoneyLineAmerican']
				except KeyError: pass
		spreadData.append(entry)
	output=json.dumps(spreadData)
	return output

@app.route('/api/v1/resources/nhl/match/totals/american', methods=['GET'])
def nhlTotalsAmerican():	
	
	league='nhl'
	manager=Manager()
	masterdata=manager.dict()
	IntertopsBaseURLs='https://sports.intertops.eu/en/Bets/Ice-Hockey/NHL-Lines/1064'
	bovadaAPIUrls='https://services.bovada.lv/services/sports/event/coupon/events/A/description/hockey?marketFilterId=def&preMatchOnly=true&eventsLimit=50&lang=en'
	betPhoenixAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111207169812656759593_1577303361038&hid=bdb01c9f736f2e641984fcde2fce11ad&cmd=games&leagues=7&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577303361039'
	skyBookAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111206009097206260869_1577542998571&hid=e154acf7203ae1251e181abf8aca82a7&cmd=games&leagues=7&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577542998572'
	#SportBetReducedURLS='https://www.sportbet.com/lines/Hockey/Reduced/'


	p=Process(target=intertopsBaseScraper,args=(IntertopsBaseURLs,masterdata))
	p.start()
	#p1=Process(target=sportBetBaseScraper,args=(SportBetReducedURLS,masterdata))
	#p1.start()
	p2=Process(target=bovadaBaseScraper,args=(bovadaAPIUrls,masterdata))
	p2.start()
	p3=Process(target=betPhoenixBaseScraper,args=(betPhoenixAPIUrls,masterdata))
	p3.start()
	p4=Process(target=skyBookBaseScraper,args=(skyBookAPIUrls,masterdata))
	p4.start()







	p.join()
	#p1.join()
	p2.join()
	p3.join()
	p4.join()
	spreadData=[]
	for key in masterdata:
		entry={}
		if len(masterdata[key])<2:
		       continue
		entry['AwayTeam']=masterdata[key][0]['AwayTeam'][2:-1].title()
		entry['HomeTeam']=masterdata[key][0]['HomeTeam'][2:-1].title()
		
		for key1 in masterdata[key]:
			if key1['LineType']=="Match":
				bookName=key1['SportsBook']
				try:
					entry[bookName+"OverPoints"]=key1['OverPoints']
					entry[bookName+"OverLine"]=key1['OverLineAmerican']
					entry[bookName+"UnderPoints"]=key1['UnderPoints']
					entry[bookName+"UnderLine"]=key1['UnderLineAmerican']
				except KeyError: pass
		spreadData.append(entry)
	output=json.dumps(spreadData)
	return output

@app.route('/api/v1/resources/nhl/match/totals/decimal', methods=['GET'])
def nhlTotalsDecimal():	
	
	league='nhl'
	manager=Manager()
	masterdata=manager.dict()
	IntertopsBaseURLs='https://sports.intertops.eu/en/Bets/Ice-Hockey/NHL-Lines/1064'
	bovadaAPIUrls='https://services.bovada.lv/services/sports/event/coupon/events/A/description/hockey?marketFilterId=def&preMatchOnly=true&eventsLimit=50&lang=en'
	betPhoenixAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111207169812656759593_1577303361038&hid=bdb01c9f736f2e641984fcde2fce11ad&cmd=games&leagues=7&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577303361039'
	skyBookAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111206009097206260869_1577542998571&hid=e154acf7203ae1251e181abf8aca82a7&cmd=games&leagues=7&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577542998572'
	#SportBetReducedURLS='https://www.sportbet.com/lines/Hockey/Reduced/'


	p=Process(target=intertopsBaseScraper,args=(IntertopsBaseURLs,masterdata))
	p.start()
	#p1=Process(target=sportBetBaseScraper,args=(SportBetReducedURLS,masterdata))
	#p1.start()
	p2=Process(target=bovadaBaseScraper,args=(bovadaAPIUrls,masterdata))
	p2.start()
	p3=Process(target=betPhoenixBaseScraper,args=(betPhoenixAPIUrls,masterdata))
	p3.start()
	p4=Process(target=skyBookBaseScraper,args=(skyBookAPIUrls,masterdata))
	p4.start()







	p.join()
	#p1.join()
	p2.join()
	p3.join()
	p4.join()
	spreadData=[]
	for key in masterdata:
		entry={}
		if len(masterdata[key])<2:
		       continue
		entry['AwayTeam']=masterdata[key][0]['AwayTeam'][2:-1].title()
		entry['HomeTeam']=masterdata[key][0]['HomeTeam'][2:-1].title()
		
		for key1 in masterdata[key]:
			if key1['LineType']=="Match":
				bookName=key1['SportsBook']
				try:
					entry[bookName+"OverPoints"]=key1['OverPoints']
					entry[bookName+"OverLine"]=round(float(key1['OverLine']),2)
					entry[bookName+"UnderPoints"]=key1['UnderPoints']
					entry[bookName+"UnderLine"]=round(float(key1['UnderLine']),2)
				except KeyError: pass
		spreadData.append(entry)
	output=json.dumps(spreadData)
	return output

if __name__ == '__main__':
	app.run()



