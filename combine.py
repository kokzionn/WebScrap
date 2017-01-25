import json
import io

#travel-home-region-install
with open('merged_file.json', 'r') as data_file:
	data = json.load(data_file)
					
	#prettyprint
	#data = json.dumps(data, sort_keys=True, indent=4)
	#data[0]["OCBC"][3]["promotions"][1]["name"] to obtain merchant name
	#data[0]["OCBC"][3]["promotions"][1] access a particular promotion from a category
	#data[0]["OCBC"][3]["promotions"] all the promotions from one category
	#data[0]["OCBC"][3] choosing a particular category
	#print(len(data[1]["OCBC"]))
	#for i in range(len(data[0]["OCBC"])):
	#	if not (data[0]["OCBC"][i]):
	#		print("YES")
	#		print(i)
	#		del data([0]["OCBC"][i])
	
	content = data[0].copy()
	#content["promotions"].append(data[1]["promotions"])
	for i in range (0, len(data[1]["promotions"])):
		count = 129
		content["promotions"].insert(count, data[1]["promotions"][i])
		count += 1
	
	#content = json.dumps(content, sort_keys=True, indent=4)
	
#json	
with io.open("beforeFinal.json", "w", encoding='utf-8')as f:
	f.write(unicode(json.dumps(content, ensure_ascii=False)))
