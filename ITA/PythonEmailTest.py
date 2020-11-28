import requests
import json

api_url = """https://prod-10.southeastasia.logic.azure.com:443/workflows/1a280e980c7a44b4bc56163abe494341/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=jc1Vuab1AdeEU6cPIwL0B36CjslGonLdpTEUSC-agaA"""

json_obj = {
    "emailAddress":"john.paolo.flores@oocl.com",
    "agreementId": "ABC1234567",
    "chargeCodes": ["QWE","EWQ","MAMA"]
}
data = json.dumps(json_obj)
r = requests.post(api_url,json=json_obj)

print("response: ", r.text)