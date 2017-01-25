import json
import io

#theRest
with open('ocbcWebScrap.json', 'r') as data_file:
	data = json.load(data_file)
	
	#deletes categories field
	for i in range(len(data["OCBC"])-1):
		del data["OCBC"][i+1]["category"]
			
	#deletes extra curly brackets
	for j in range((len(data["OCBC"]))-1, 9, -1):
		del data["OCBC"][j]
	
	'''
	to delete empty category (not working)
	for i in range(len(data["OCBC"])):
		if not data["OCBC"][i]:
			#print("YES")
	'''
	#hard code method to delete empty categories		
	del data["OCBC"][2]
	del data["OCBC"][3]

	#to join all categories under promotions
	content = data["OCBC"][1].copy()	

	for i in range (2,7):
		for j in range (0, len(data["OCBC"][i]["promotions"])):
			count = len(data["OCBC"][2]["promotions"])
			content["promotions"].insert(count, data["OCBC"][i]["promotions"][j])
			count += 1

	contentLength = len(content["promotions"])
	content["promotions"].insert(contentLength, data["OCBC"][0])

	#prettyprint
	#content = json.dumps(content, sort_keys=True, indent=4)
	
	#print(data)
	

#json	
with io.open("updatedOCBC-file.json", "w", encoding='utf-8')as f:
	f.write(unicode(json.dumps(content, ensure_ascii=False)))
