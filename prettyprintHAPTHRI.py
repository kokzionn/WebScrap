import json
import io

#travel-home-region-install
with open('health-arts-petrol-travel-home-region-install.json', 'r') as data_file:
	data = json.load(data_file)
	
	#deletes categories field
	for i in range(len(data["OCBC"])):
		del data["OCBC"][i]["category"]
			
	#deletes extra curly brackets
	for j in range((len(data["OCBC"]))-8, -1, -1):
		del data["OCBC"][j]

	#merging promotions of all catgories
	content = data["OCBC"][0].copy()
	
	for i in range (1,len(data["OCBC"])):
		for j in range (0, len(data["OCBC"][i]["promotions"])):
			count = len(data["OCBC"][0]["promotions"])
			content["promotions"].insert(count, data["OCBC"][i]["promotions"][j])
			count += 1
	
	#prettyprint
	#content = json.dumps(content, sort_keys=True, indent=4)
	

#json	
with io.open("updatedHAPTHRI-file.json", "w", encoding='utf-8')as f:
	f.write(unicode(json.dumps(content, ensure_ascii=False)))
