# fetch.py

import requests
import os
import json
import io

params = {
  'api_key': 'tm9UMvsN_Lmr',
}
r = requests.get(
    'https://www.parsehub.com/api/v2/projects/tDbsc43foNBU/last_ready_run/data',
    params=params)

s = requests.get(
    'https://www.parsehub.com/api/v2/projects/t_B9NP3bkZrK/last_ready_run/data',
    params=params)

with io.open("ocbcWebScrap.json", "w", encoding='utf-8')as f:
	f.write(r.text)

with io.open("health-arts-petrol-travel-home-region-install.json", "w", encoding='utf-8')as f:
	f.write(s.text)
