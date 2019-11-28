# Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.

import requests
import json
from bs4 import BeautifulSoup
url = 'https://prod-11.southeastasia.logic.azure.com:443/workflows/221b5af682e3482bb5ab578edc284dba/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=MlLcPuZHlFlGtNuVj02isa24kyhln2aMYzo7QQbWTnA'
json_obj = {
    "job_name": "edi_bex_messaging_handlerSS",
  	"job_err_msg": "Unhandled exception error",
  	"return_code": 500,
  	"job_status": "Failed",
  	"env":"dev"
}
data = json.dumps(json_obj)
r = requests.post(url,json= json_obj)

print("response: ", r.text)