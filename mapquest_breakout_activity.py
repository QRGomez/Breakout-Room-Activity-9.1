from crypt import methods
import urllib.parse
import requests
from flask import Flask
from flask import request
from flask import render_template





main_api="https://www.mapquestapi.com/directions/v2/route?"
key= "b78UB9skq4FPRrU8tUQgbosdgerVuwXv"

orig = input("Starting Location:")
dest = input("Destination: ")
routeType = input("Route Type(fastest, shortest, pedestrian, bicycle):")

url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest,"routeType":routeType})
print("URL: " + (url))
json_data = requests.get(url).json()
json_status = json_data["info"]["statuscode"]

if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Directions from " + (orig) + " to " + (dest))
        print("Trip Duration:   " + (json_data["route"]["formattedTime"]))
        print("Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        #print("Fuel Used (Ltr) " + str("{:.2f}".format((json_data["route"]["FuelUsed"])*3.78)))
        print("Are there Toll Roads ahead?: " + str(json_data["route"]["hasTollRoad"]))
        print("Will there be unpaved roads?: " + str(json_data["route"]["hasUnpaved"]))
        print("Are there any highways?: " + str(json_data["route"]["hasHighway"]))
        print("=============================================")

        directions = (orig) + " to " + (dest)
        tripDuration = (json_data["route"]["formattedTime"])
        kilometers = str("{:.2f}".format((json_data["route"]["distance"])*1.61))
        #fuelUsed = str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78))
        areThereTolls = str(json_data["route"]["hasTollRoad"])
        isPavedOrNot = str(json_data["route"]["hasUnpaved"])
        anyHighways  = str(json_data["route"]["hasHighway"])

        for each in json_data["route"]["legs"][0]["maneuvers"]:
          print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
        print("=============================================\n")

elif json_status == 402:
        print("********************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n")
elif json_status == 611:
        print("********************************************")
        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print("**********************************************\n")
else:
        print("**********************************************************************")
        print("For Staus Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")


app = Flask(__name__)
@app.route('/')
def main():
    return render_template('index.html', dir_html = directions, routeT_html = routeType, tripD_html = tripDuration, km_html = kilometers,  tolls_html = areThereTolls, pavedRoads_html=isPavedOrNot, highways_html=anyHighways)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)