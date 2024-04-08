import resilient as co3
import sys
# usage : python <this-python>.py <incident_number> <attachment_file_path>

# fill the followings
org_name = ""
soar_url = ""
user = ""
password = ""

inc_num = sys.argv[1]
att_file = sys.argv[2]

api_path = "/incidents/" + inc_num + "/attachments"

# login
client = co3.SimpleClient(org_name=org_name, base_url=soar_url, verify=False)
client.set_api_key(user, password)

# run attachment api
client.post_attachment(api_path, att_file)
