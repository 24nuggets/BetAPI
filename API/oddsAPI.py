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


@app.route('/api/v1/resources/nfl', methods=['GET'])
def nfl():	
	
	league='nfl'
	manager=Manager()
	masterdata=manager.dict()
	IntertopsBaseURLs='https://sports.intertops.eu/en/Bets/American-Football/NFL-Lines/1018'
	bovadaAPIUrls='https://services.bovada.lv/services/sports/event/coupon/events/A/description/football?marketFilterId=def&preMatchOnly=true&eventsLimit=50&lang=en'
	betPhoenixAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111207169812656759593_1577303361038&hid=bdb01c9f736f2e641984fcde2fce11ad&cmd=games&leagues=1&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577303361039'
	skyBookAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111206009097206260869_1577542998571&hid=e154acf7203ae1251e181abf8aca82a7&cmd=games&leagues=1&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577542998572'
	SportBetReducedURLS='https://www.sportbet.com/lines/Football/Reduced/'


	p=Process(target=intertopsBaseScraper,args=(IntertopsBaseURLs,masterdata))
	p.start()
	p1=Process(target=sportBetBaseScraper,args=(SportBetReducedURLS,masterdata))
	p1.start()
	p2=Process(target=bovadaBaseScraper,args=(bovadaAPIUrls,masterdata))
	p2.start()
	p3=Process(target=betPhoenixBaseScraper,args=(betPhoenixAPIUrls,masterdata))
	p3.start()
	p4=Process(target=skyBookBaseScraper,args=(skyBookAPIUrls,masterdata))
	p4.start()







	p.join()
	p1.join()
	p2.join()
	p3.join()
	p4.join()
	output=json.dumps(dict(masterdata))
	return output

@app.route('/api/v1/resources/nba', methods=['GET'])
def nba():
	league='nba'
	manager=Manager()
	masterdata=manager.dict()
	IntertopsBaseURLs='https://sports.intertops.eu/en/Bets/Basketball/NBA-Lines/1070'
	bovadaAPIUrls='https://services.bovada.lv/services/sports/event/coupon/events/A/description/basketball?marketFilterId=def&preMatchOnly=true&eventsLimit=50&lang=en'
	betPhoenixAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111207169812656759593_1577303361038&hid=bdb01c9f736f2e641984fcde2fce11ad&cmd=games&leagues=3&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577303361039'
	skyBookAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111206009097206260869_1577542998571&hid=e154acf7203ae1251e181abf8aca82a7&cmd=games&leagues=3&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577542998572'
	SportBetReducedURLS='https://www.sportbet.com/lines/Basketball/Reduced/'


	p=Process(target=intertopsBaseScraper,args=(IntertopsBaseURLs,masterdata))
	p.start()
	p1=Process(target=sportBetBaseScraper,args=(SportBetReducedURLS,masterdata))
	p1.start()
	p2=Process(target=bovadaBaseScraper,args=(bovadaAPIUrls,masterdata))
	p2.start()
	p3=Process(target=betPhoenixBaseScraper,args=(betPhoenixAPIUrls,masterdata))
	p3.start()
	p4=Process(target=skyBookBaseScraper,args=(skyBookAPIUrls,masterdata))
	p4.start()







	p.join()
	p1.join()
	p2.join()
	p3.join()
	p4.join()
	output=json.dumps(dict(masterdata))
	return output

@app.route('/api/v1/resources/ncaab', methods=['GET'])
def ncaab():
	league='ncaab'
	manager=Manager()
	masterdata=manager.dict()
	IntertopsBaseURLs='https://sports.intertops.eu/en/Bets/Basketball/NCAAB-Lines/1068'
	bovadaAPIUrls='https://services.bovada.lv/services/sports/event/coupon/events/A/description/basketball?marketFilterId=def&preMatchOnly=true&eventsLimit=50&lang=en'
	betPhoenixAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111207169812656759593_1577303361038&hid=bdb01c9f736f2e641984fcde2fce11ad&cmd=games&leagues=4&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577303361039'
	skyBookAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111206009097206260869_1577542998571&hid=e154acf7203ae1251e181abf8aca82a7&cmd=games&leagues=4&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577542998572'
	SportBetReducedURLS='https://www.sportbet.com/lines/Basketball/Reduced/'
	betPhoenixAPIUrls2='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111207169812656759593_1577303361038&hid=bdb01c9f736f2e641984fcde2fce11ad&cmd=games&leagues=741&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577303361039'
	skyBookAPIUrls2='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111206009097206260869_1577542998571&hid=e154acf7203ae1251e181abf8aca82a7&cmd=games&leagues=741&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577542998572'
	

	p=Process(target=intertopsBaseScraper,args=(IntertopsBaseURLs,masterdata))
	p.start()
	p1=Process(target=sportBetBaseScraper,args=(SportBetReducedURLS,masterdata))
	p1.start()
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
	p1.join()
	p2.join()
	p3.join()
	p4.join()
	p5.join()
	p6.join()
	output=json.dumps(dict(masterdata))
	return output

@app.route('/api/v1/resources/ufc', methods=['GET'])
def ufc():	
	
	league='ufc'
	manager=Manager()
	masterdata=manager.dict()
	
	bovadaAPIUrls='https://services.bovada.lv/services/sports/event/coupon/events/A/description/ufc-mma?marketFilterId=def&preMatchOnly=true&eventsLimit=50&lang=en'
	betPhoenixAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111207169812656759593_1577303361038&hid=bdb01c9f736f2e641984fcde2fce11ad&cmd=games&leagues=32&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577303361039'
	skyBookAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111206009097206260869_1577542998571&hid=e154acf7203ae1251e181abf8aca82a7&cmd=games&leagues=32&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577542998572'
	SportBetReducedURLS='https://www.sportbet.com/lines/Fighting/Reduced/'


	
	p1=Process(target=sportBetBaseScraper,args=(SportBetReducedURLS,masterdata))
	p1.start()
	p2=Process(target=bovadaBaseScraper,args=(bovadaAPIUrls,masterdata))
	p2.start()
	p3=Process(target=betPhoenixBaseScraper,args=(betPhoenixAPIUrls,masterdata))
	p3.start()
	p4=Process(target=skyBookBaseScraper,args=(skyBookAPIUrls,masterdata))
	p4.start()







	
	p1.join()
	p2.join()
	p3.join()
	p4.join()
	output=json.dumps(dict(masterdata))
	return output


@app.route('/api/v1/resources/boxing', methods=['GET'])
def boxing():	
	
	league='boxing'
	manager=Manager()
	masterdata=manager.dict()
	
	bovadaAPIUrls='https://services.bovada.lv/services/sports/event/coupon/events/A/description/boxing?marketFilterId=def&preMatchOnly=true&eventsLimit=50&lang=en'
	betPhoenixAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111207169812656759593_1577303361038&hid=bdb01c9f736f2e641984fcde2fce11ad&cmd=games&leagues=10&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577303361039'
	skyBookAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111206009097206260869_1577542998571&hid=e154acf7203ae1251e181abf8aca82a7&cmd=games&leagues=10&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577542998572'
	SportBetReducedURLS='https://www.sportbet.com/lines/Fighting/Reduced/'


	
	p1=Process(target=sportBetBaseScraper,args=(SportBetReducedURLS,masterdata))
	p1.start()
	p2=Process(target=bovadaBaseScraper,args=(bovadaAPIUrls,masterdata))
	p2.start()
	p3=Process(target=betPhoenixBaseScraper,args=(betPhoenixAPIUrls,masterdata))
	p3.start()
	p4=Process(target=skyBookBaseScraper,args=(skyBookAPIUrls,masterdata))
	p4.start()







	
	p1.join()
	p2.join()
	p3.join()
	p4.join()
	output=json.dumps(dict(masterdata))
	return output

@app.route('/api/v1/resources/nhl', methods=['GET'])
def nhl():	
	
	league='nhl'
	manager=Manager()
	masterdata=manager.dict()
	IntertopsBaseURLs='https://sports.intertops.eu/en/Bets/Ice-Hockey/NHL-Lines/1064'
	bovadaAPIUrls='https://services.bovada.lv/services/sports/event/coupon/events/A/description/hockey?marketFilterId=def&preMatchOnly=true&eventsLimit=50&lang=en'
	betPhoenixAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111207169812656759593_1577303361038&hid=bdb01c9f736f2e641984fcde2fce11ad&cmd=games&leagues=7&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577303361039'
	skyBookAPIUrls='https://api.securecashiersystem.ag/js/Lines.js?jsoncallback=jQuery111206009097206260869_1577542998571&hid=e154acf7203ae1251e181abf8aca82a7&cmd=games&leagues=7&nhlLine=A&mblLine=A&lineStyle=E&language=0&_=1577542998572'
	SportBetReducedURLS='https://www.sportbet.com/lines/Hockey/Reduced/'


	p=Process(target=intertopsBaseScraper,args=(IntertopsBaseURLs,masterdata))
	p.start()
	p1=Process(target=sportBetBaseScraper,args=(SportBetReducedURLS,masterdata))
	p1.start()
	p2=Process(target=bovadaBaseScraper,args=(bovadaAPIUrls,masterdata))
	p2.start()
	p3=Process(target=betPhoenixBaseScraper,args=(betPhoenixAPIUrls,masterdata))
	p3.start()
	p4=Process(target=skyBookBaseScraper,args=(skyBookAPIUrls,masterdata))
	p4.start()







	p.join()
	p1.join()
	p2.join()
	p3.join()
	p4.join()
	output=json.dumps(dict(masterdata))
	return output

if __name__ == '__main__':
	app.run()



