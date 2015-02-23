from scalpyr import Scalpyr
import requests
import json
import pprint
from datetime import datetime as dt
import csv
seatgeek = Scalpyr()

#list of nba ids that are formatted to be called by Scalpry.get_events()

nba_slugs = ['boston-celtics', 'brooklyn-nets', 'new-york-knicks', 'philadelphia-76ers', 'toronto-raptors',
	'dallas-mavericks', 'houston-rockets', 'memphis-grizzlies', 'new-orleans-pelicans', 'san-antonio-spurs',
	'chicago-bulls', 'cleveland-cavaliers', 'detroit-pistons', 'indiana-pacers', 'milwaukee-bucks', 'denver-nuggets',
	'minnesota-timberwolves', 'oklahoma-city-thunder', 'portland-trail-blazers', 'utah-jazz',
	'atlanta-hawks', 'charlotte-hornets', 'miami-heat', 'orlando-magic','washington-wizards',
	'golden-state-warriors', 'los-angeles-clippers', 'los-angeles-lakers', 'phoenix-suns', 'sacromento-kings']

venue_ids = ['1544', '7546', '93', '3148','91','117', '129','1243', '184','185','136','120','137','121','207',
			 '187','135','208','256','188','127','112','183','2652','181', '132','134','130']

def slug_iter():
	"""Executes code and puts it in a csv file"""
	for team in nba_slugs:
		h = get_event_stat(team)
		csv_ticket_stat(h)

def get_event_stat(team_id):
	"Make api call with scalpyr.get_events"

	request_args = {'per_page' : 25}
	slug_arg = 'performers[home_team].slug'
	request_args[slug_arg] = team_id
	return seatgeek.get_events(request_args)

def create_csv():
	csvFile = open('nbatickets.csv', 'a')
	csvWriter = csv.writer(csvFile)

def csv_ticket_stat(response):
	"""Takes response from the api call and sets stats, to be written to a csv file"""
	#setting the json dictionary variables to make code easier to follow (and easier to type)
	stats = 'stats'
	lc = 'listing_count'
	ap = 'average_price'
	lp = 'lowest_price'
	hp = 'highest_price'
	event_id = 'id'
	st = 'short_title'
	v = 'venue'

	#name the response
	event_response = response['events']
	
	#call csvwriter
	csvFile = open('nbatickets.csv', 'a')
	csvWriter = csv.writer(csvFile)

	for event in event_response:
		print [event[event_id], event[v][event_id], event[st].replace(' at ','_'), event[stats][lc], event[stats][ap], event[stats][lp], event[stats][hp],
			   (dt.now())]
		csvWriter.writerow([event[event_id], event[v][event_id], event[st].replace(' at ','_'), event[stats][lc], event[stats][ap], event[stats][lp], event[stats][hp],
			     (dt.now())])
	csvFile.close()

slug_iter()







