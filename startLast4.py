import requests

params = {
  "api_key": "tm9UMvsN_Lmr",
  "send_email": "1"
}
r = requests.post("https://www.parsehub.com/api/v2/projects/t_B9NP3bkZrK/run", data=params)
