from flask_apps import app
from flask import render_template
import requests
from requests.auth import HTTPBasicAuth
import datetime


def getPlaceID(city):
    req = requests.get("https://api.sncf.com/v1/coverage/sncf/places?q="+ city, auth=HTTPBasicAuth(app.config['SNCFAPIKEY'], ''))
    ret = []
    ret.append(req.status_code)
    ret.append(req.json())
    return ret


def getJourneys(srcStation, dstStation, departureDateTime):
    print "getJourneys"
    req = requests.get("https://api.sncf.com/v1/coverage/sncf/journeys?from="+ srcStation + "&to=" + dstStation + "&datetime=" + departureDateTime + "&datetime_represents=departure&min_nb_journeys=4"\
    , auth=HTTPBasicAuth(app.config['SNCFAPIKEY'], ''))
    ret = []
    ret.append(req.status_code)
    ret.append(req.json())
    return ret


@app.route("/route/<string:from_place>/<string:to_place>")
def routes(from_place, to_place):
    places = []

    # Get places IDs
    fromPlaceIdResult = getPlaceID(from_place)
    fromPlaceID = fromPlaceIdResult[1]['places'][1]['id']

    toPlaceIdResult = getPlaceID(to_place)
    toPlaceID = toPlaceIdResult[1]['places'][1]['id']

    places.append({'from_place': from_place, 'to_place': to_place,\
                    'from_place_id': fromPlaceID, 'to_place_id': toPlaceID,\
    })

    #Ymd\TH:i
    date = datetime.datetime.today().strftime('%Y%m%d %R:%M')
    print date
    journeysResult = getJourneys(fromPlaceID, toPlaceID, date)
    print journeysResult
    
    return render_template("welcome.html", places=places, journeysResult=journeysResult)
