import glob, os, json, requests

username = os.getenv('username')
print("""
How to use:
Join a Roblox game and wait until the game fully loads
Run this script while in the game
Press enter when you are ready to pull the IP!
""")
try:
    input("Press [ENTER] to grab the IP!")
except SyntaxError:
    pass

print("\nGrabbing the information...")

list_of_files = glob.glob(r'C:\users\{}\AppData\Local\Roblox\logs\*'.format(username))
latest_file = max(list_of_files, key=os.path.getctime)
roblox_log = open(latest_file, 'r')

for line in roblox_log:
    if 'Connection accepted from' in line:
        line = line.replace('Connection accepted from', '')
        line2 = line.replace('|', ':')
        line3 = line2[25:]
        IPandPort = line3.split("]", 1)[1].strip()
        IP = IPandPort.split(":")[0]
        Port = IPandPort.split(":")[1]
        r = requests.get(f"https://ipwhois.app/json/{IP}")
        data = r.json()

        ip_country = data["country"]
        ip_continent = data["continent"]
        ip_city = data["city"]

        ip_org = data["org"]
        ip_isp = data["isp"]

        print("====GEOGRAPHY====")
        print("Country: " + ip_country)
        print("Continent: " + ip_continent)
        print("City: " + ip_city)
        print("\n")
        print("====TECHNOLOGY===")
        print("IP: " + IP)
        print("Port: " + Port)
        print("ORG: " + ip_org)
        print("ISP: " + ip_isp)
