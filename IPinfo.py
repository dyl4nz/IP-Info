import requests

# Branding

print("██ ██████        ██ ███    ██ ███████  ██████     ")
print("██ ██   ██       ██ ████   ██ ██      ██    ██    ")
print("██ ██████  █████ ██ ██ ██  ██ █████   ██    ██    ")
print("██ ██            ██ ██  ██ ██ ██      ██    ██    ")
print("██ ██            ██ ██   ████ ██       ██████  ██ ")
print("===================================================")
print(' /(_M_)\ ')
print('|       |')
print(' \/~V~\/')
print(' Not.dyz')
print("===================================================")
print("Some IP information is an estimate!! ")
print("The often inaccurate outputs are marked with an asterix (*)")
print("===================================================")

#############################################################################

# Return your public IP adress if you want to test your own
print("Your Public IP adress:")
response = requests.get("https://api.ipify.org?format=json")
if response.status_code == 200:
    data = response.json()
    ip_address = data["ip"]
    print(ip_address)
else:
    print("Could not retrieve, check your connection.")

#############################################################################

# Defines the function that retrieves information about the given ip from ip-api.com
def geolocate_ip(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)
# Handles exceptions
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error: HTTP request for IP information failed, check your connection.")

# Asks for IP adress to retrieve info on 
print("Supply IP address: ")
ip_address = input()
result = geolocate_ip(ip_address)

#############################################################################

# Prints the retrieved information neatly
print("Information:")
print("------------------------")
print("                        ")
print("Status:")
print(result.get("status"))
print("                        ")
print("------------------------")

print("                        ")
print("Country:")
print(result.get("country"))
print("                         ")
print("-------------------------")
print("                         ")
print("Country Code:")
print(result.get("countryCode"))
print("                        ")
print("------------------------")
print("                        ")
print("Region:")
print(result.get("region"))
print("                        ")
print("------------------------")
print("                        ")
print("Region Name:")
print(result.get("regionName"))
print("                        ")
print("------------------------")
print("                        ")
print("*City:")
print(result.get("city"))
print("                        ")
print("------------------------")
print("                        ")
print("*ZIP code:")
print(result.get("zip"))
print("                        ")
print("------------------------")
print("                        ")
print("*Latitude:")
print(result.get("lat"))
print("                        ")
print("------------------------")
print("                        ")
print("*Longitude:")
print(result.get("lon"))
print("                        ")
print("------------------------")
print("                        ")
print("Timezone:")
print(result.get("timezone"))
print("                        ")
print("------------------------")
print("                        ")
print("ISP:")
print(result.get("isp"))
print("                        ")
print("------------------------")
print("                        ")
print("Organization:")
print(result.get("org"))
print("                        ")
print("------------------------")
print("                        ")
print("*AS:")
print(result.get("as"))
print("                        ")
print("------------------------")
print("                        ")
print("Query:")
print(result.get("query"))
print("                        ")
print("------------------------")
print("Thank you for using! <3")
print("------------------------")
print("                        ")
input("Press Enter to quit\n")
