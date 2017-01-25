import json
import io

#demo
with open('beforeFinal.json', 'r') as data_file:
	data = json.load(data_file)
	
	content = data

	#hardcoded to make catgories/subcategories array
	for i in range(len(content["promotions"])):
		if content["promotions"][i]["category"] == "Dining and Entertainment":
			content["promotions"][i]["category"] = ["Dining and Entertainment"]
		elif content["promotions"][i]["category"] == "Chinese New Year 2017":
			content["promotions"][i]["category"] = ["Chinese New Year 2017"]
		elif content["promotions"][i]["category"] == "WowDeals App: Exclusive Card Deals":
			content["promotions"][i]["category"] = ["WowDeals App: Excluesive Card Deals"]
		elif content["promotions"][i]["category"] == "0% Interest Instalment Plan":
			content["promotions"][i]["category"] = ["0% Interest Instalment Plan"]
		elif content["promotions"][i]["category"] == "Regional Privileges":
			content["promotions"][i]["category"] = ["Regional Privileges"]
		elif content["promotions"][i]["category"] == "Home and Office":
			content["promotions"][i]["category"] = ["Home and Office"]
		elif content["promotions"][i]["category"] == "Travel and Hotels":
			content["promotions"][i]["category"] = ["Travel and Hotels"]
		elif content["promotions"][i]["category"] == "Petrol and Automotives":
			content["promotions"][i]["category"] = ["Petrol and Automotives"]
		elif content["promotions"][i]["category"] == "Online Shopping":
			content["promotions"][i]["category"] = ["Online Shopping"]
		elif content["promotions"][i]["category"] == "Fashion and Accessories":
			content["promotions"][i]["category"] = ["Fashion and Accessories"]
		elif content["promotions"][i]["category"] == "Electronics and Gadgets":
			content["promotions"][i]["category"] = ["Electronics and Gadgets"]
		elif content["promotions"][i]["category"]== "Health and Beauty":
			content["promotions"][i]["category"] = ["Health and Beauty"]
		elif content["promotions"][i]["category"] == "What's New":
			content["promotions"][i]["category"] = ["What's New"]
		elif content["promotions"][i]["category"] == "Leisure and Arts":
			content["promotions"][i]["category"] = ["Leisure and Arts"]
		
	for j in range(len(content["promotions"])):
		try: 
			content["promotions"][j]["subcategory"]
		except KeyError:
			None
		else:
			if content["promotions"][j]["subcategory"] == "Asian":
				content["promotions"][j]["subcategory"] = ["Asian"]
			elif content["promotions"][j]["subcategory"] == "Bars and Wine":
				content["promotions"][j]["subcategory"] = ["Bars and Wine"]
			elif content["promotions"][j]["subcategory"] == "Cafes and Dessert":
				content["promotions"][j]["subcategory"] = ["Cafes and Dessert"]
			elif content["promotions"][j]["subcategory"] == "Chinese":
				content["promotions"][j]["subcategory"] = ["Chinese"]
			elif content["promotions"][j]["subcategory"] == "CNY 2017":
				content["promotions"][j]["subcategory"] = ["CNY 2017"]
			elif content["promotions"][j]["subcategory"] == "International":
				content["promotions"][j]["subcategory"] = ["International"]
			elif content["promotions"][j]["subcategory"] == "Japanese and Korean":
				content["promotions"][j]["subcategory"] = ["Japanese and Korean"]
			elif content["promotions"][j]["subcategory"] == "Wedding Banquet":
				content["promotions"][j]["subcategory"] = ["Wedding Banquet"]
			elif content["promotions"][j]["subcategory"] == "Western and European":
				content["promotions"][j]["subcategory"] = ["Western and European"]
			elif content["promotions"][j]["subcategory"] == "Online/Others":
				content["promotions"][j]["subcategory"] = ["Online/Others"]
			elif content["promotions"][j]["subcategory"] == "Ticketing":
				content["promotions"][j]["subcategory"] = ["Ticketing"]
			elif content["promotions"][j]["subcategory"] == "Travel & Hotels":
				content["promotions"][j]["subcategory"] = ["Travel & Hotels"]
			elif content["promotions"][j]["subcategory"] == "Arts & Performance":
				content["promotions"][j]["subcategory"] = ["Arts & Performance"]
			elif content["promotions"][j]["subcategory"] == "Attractions":
				content["promotions"][j]["subcategory"] = ["Attractions"]
			elif content["promotions"][j]["subcategory"] == "Movies & KTV":
				content["promotions"][j]["subcategory"] = ["Movies & KTV"]
			elif content["promotions"][j]["subcategory"] == "Sports":
				content["promotions"][j]["subcategory"] = ["Sports"]
			elif content["promotions"][j]["subcategory"] == "Others":
				content["promotions"][j]["subcategory"] = ["Others"]
			elif content["promotions"][j]["subcategory"] == "Online":
				content["promotions"][j]["subcategory"] = ["Online"]
			elif content["promotions"][j]["subcategory"] == "Hotel/Tour Packages":
				content["promotions"][j]["subcategory"] = ["Hotel/Tour Packages"]
			elif content["promotions"][j]["subcategory"] == "Staycation":	
				content["promotions"][j]["subcategory"] = ["Staycation"]
			elif content["promotions"][j]["subcategory"] == "Malaysia":
				content["promotions"][j]["subcategory"] = ["Malaysia"]
			elif content["promotions"][j]["subcategory"] == "Macau" :
				content["promotions"][j]["subcategory"] = ["Macau"]
			elif content["promotions"][j]["subcategory"] == "Hong Kong":
				content["promotions"][j]["subcategory"] = ["Hong Kong"]
			elif content["promotions"][j]["subcategory"] == "Education":
				content["promotions"][j]["subcategory"] = ["Education"]
			elif content["promotions"][j]["subcategory"] == "Health, Beauty & Wellness":
				content["promotions"][j]["subcategory"] = ["Health, Beuty & Wellness"]
			elif content["promotions"][j]["subcategory"] == "Insurance":
				content["promotions"][j]["subcategory"] = ["Insurance"]
			elif content["promotions"][j]["subcategory"] == "Shopping":
				content["promotions"][j]["subcategory"] = ["Shopping"]
			elif content["promotions"][j]["subcategory"] == "Travel":
				content["promotions"][j]["subcategory"] = ["Travel"]
		

	#content = json.dumps(content, sort_keys=True, indent=4)
	
	#print(content)
	
#json	
with io.open("Final.json", "w", encoding='utf-8')as f:
	f.write(unicode(json.dumps(content, ensure_ascii=False)))
