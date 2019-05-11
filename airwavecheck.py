import requests
import argparse
import warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning

warnings.simplefilter('ignore',InsecureRequestWarning)
parser = argparse.ArgumentParser()
parser.add_argument('--url', action='store', dest='url', help='Specify the url to test.')
results = parser.parse_args()

url = results.url
r = requests.get(url,verify=False)
if "AirWave Management Platform" in r.text:
    url = str(results.url) + "/LOGIN"
    headers = {'Content-Type':'application/x-www-form-urlencoded;charset=utf-8'}
    data = "credential_0=admin&credential_1=admin&destination=/index.html"
    r = requests.post(url,data=data,headers=headers,verify=False)
    if r.status_code == 200:
        print("Successfully logged in using credentials 'admin:admin'")
    else:
        print("Interface Does Not Use Default Credentials")
else:
    print("Host does not seem to be running Aruba AirWave Management Platform")