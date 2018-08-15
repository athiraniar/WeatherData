from datetime import timedelta, date
import random

#Period considered for generating test data
start_date = date(2017, 1, 1)
end_date = date(2017, 12, 31)

#Stations considered for generating test data
stations = {"ADL": "Adelaide","BRB": "Brisbane","CAN": "Canberra", "DAR": "Darwin",
            "HOB": "Hobart", "MEL": "Melbourne","PER": "Perth", "SYD": "Sydney",
            "OOL": "Gold Coast", "WOL": "Wollongong"}
#Reference for weather condition assumptions
#http://www.bom.gov.au/climate/averages/maps.shtml
#http://www.bom.gov.au/jsp/ncc/climate_averages/temperature/index.jsp?maptype=1&period=win#maps
#http://www.bom.gov.au/jsp/ncc/climate_averages/relative-humidity/index.jsp?maptype=1&period=an#maps
#http://www.bom.gov.au/jsp/awap/vprp/index.jsp?colour=colour&time=latest&step=0&map=vprph09&period=12month&area=nat

#Weather conditions assumed for generating test data
weather_conditions = {"Sunny": {"temperature": (32, 17), "pressure": (36, 2), "humidity": (70, 40)},
                      "Rainy": {"temperature": (21, 10), "pressure": (36, 2), "humidity": (70, 40)},
                      "Winter": {"temperature": (20, 10), "pressure": (36, 2), "humidity": (70, 40)}}

#Generate series of dates between the specified date range
def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

#Generate the weather conditions
def generateWeather():
    conditions = random.choice(weather_conditions.keys())
    parameters = weather_conditions[conditions]
    (tmin,tmax) = parameters["temperature"]
    (pmin,pmax) = parameters["pressure"]
    (hmin,hmax) = parameters["humidity"]
    weather_string = conditions + "|" + str(round(random.uniform(tmin,tmax))) + "|" + str(round(random.uniform(pmin,pmax))) + "|" + str(round(random.uniform(hmin,hmax)))
    return weather_string

#Generate the test data using the randomly generated station, date and weather conditions
def main():
    weatherFile = open("generated.dat", "w")

    for single_date in daterange(start_date, end_date):
        currdate = single_date.strftime("%Y-%m-%d")
        for key in stations:
            value = stations[key]
            weather_parameters = generateWeather()
            print(value + "|" + str(currdate) + "|" + weather_parameters)
            data_generated = value + "|" + str(currdate) + "|" + weather_parameters + "\n"
            weatherFile.write(data_generated)

    weatherFile.close()
    print("Completed generating the weather data successfully")
if __name__ == '__main__':
    main()
