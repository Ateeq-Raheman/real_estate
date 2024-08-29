import frappe
from faker import Faker
import requests
import random

fake = Faker('en_IN')
# # fake.seed(0) #this will raise a type error.

# # agent_image_url = "https://api.unsplash.com/search/photos?client_id=nPRqzHwZ-ei3t38DzHb9PCxC2PFUBQUHFLYrbJ2EaLA&query=headshot"
# # agent_image_data = requests.get(agent_image_url)
# # agent_image_data_json = agent_image_data.json()
# # print(agent_image_data_json)
# # agent_images = [i['urls']['small'] for i in agent_image_data_json['results']]
# # single_image_url = agent_image_data_json.get("results")[0].get("urls").get("small")
# # print(single_image_url)
# # number_of_images = len(agent_image_data_json.get("results"))
# # print(number_of_images)
# # agent_images = [i.get("urls").get("small") for i in agent_image_data_json.get("results")]
# # print(agent_images)
# # agent_images = []
# # for _ in range(2):
# #     agent_image_url = "https://api.unsplash.com/search/photos?client_id=nPRqzHwZ-ei3t38DzHb9PCxC2PFUBQUHFLYrbJ2EaLA&query=headshot"
# #     img_api = requests.get(agent_image_url)
# #     agent_images += [i.get("urls").get("small") for i in agent_image_data.json().get("results")]
# # print(agent_images)
# # len(agent_images)
# # def populate_agent(agents_images , fake):
# #     for img in agents_images:
# #         agent = frappe.get_doc({
# #             "doctype": "Agent",
# #             "email": fake.profile().get("mail"),
# #             "agent_name":fake.profile().get("name"),
# #             "phone": fake.phone_number(),
# #             "image": img
# #         })
# #         agent.insert(ignore_permissions=True)
# #         frappe.db.commit()
# # populate_agent(agent_images, fake)


# # # new code for importing the images for house 


# def populate_house(fake):
#     agents = [agent.name for agent in frappe.db.sql(""" SELECT name FROM `tabAgent` ;""", as_dict=True)]
#     cities = [city.name for city in frappe.db.sql(""" SELECT name FROM `tabCity` ;""", as_dict=True)]
#     property_types = [property.name for property in frappe.db.sql(""" SELECT name FROM `tabproperty type` ;""", as_dict=True)]
#     # amenities = frappe.db.sql("""SELECT amenity,amenity_price FROM `tabproperty Amenity Item`;""", as_dict = True)
#     # amenities = frappe.db.sql(""" SELECT amenity, amenity_price  FROM `tabProperty Amenity Item` ;""", as_dict=True)
#     status = ["SALE" , "RENT" , "LEASE"]

#     house_images = []

#     for n in range(2):
#         house_image_url = "https://api.unsplash.com/search/photos?client_id=nPRqzHwZ-ei3t38DzHb9PCxC2PFUBQUHFLYrbJ2EaLA&query=mansions"
#         img_api = requests.get(house_image_url)
#         house_images += [
#         {
#             "doctype":"property",
#             "property_name": i.get("alt_description"),  # Corrected: Added missing colon
#             "image": i.get("urls").get("small"),
#             "address": fake.address().replace("\n", ","),
#             "agent": random.choice(agents),
#             "status": random.choice(status),
#             "property_type": random.choice(property_types),
#             "property_price": random.randint(1000000, 20000000),
#             "discount": random.randint(0, 11),
#             "description": fake.paragraph(nb_sentences=10, variable_nb_sentences=False),
#             # "amenities": amenities[random.randint(0, len(amenities) - 1)],
#         }
#         for i in img_api.json().get("results")   
#     ]
#     for p in house_images:
#         # try:    
#             doc_name = "property"
#             pr = frappe.get_doc(p)
#             property_name = pr.name
#             existing_property = frappe.get_all('property', filters={'name': property_name})
#             if not existing_property:
#                 # Proceed with insert
#                 pr.insert(ignore_permissions=True)
#             else:
#                 # Handle the duplicate case
#                 print("Property already exists")

#             pr.insert(ignore_permissions=True)
#             print("Inserted property" , pr.name)
#         # except Exception as e:
#             # print("Error while inserting property" , e)
#         # print(pr)
#     frappe.db.commit()
    
         


# populate_house(fake)



import frappe
import random
import requests

def populate_house(fake):
    agents = [agent['name'] for agent in frappe.db.sql(""" SELECT name FROM `tabAgent`;""", as_dict=True)]
    cities = [city['name'] for city in frappe.db.sql(""" SELECT name FROM `tabCity`;""", as_dict=True)]
    property_types = [property['name'] for property in frappe.db.sql(""" SELECT name FROM `tabproperty type`;""", as_dict=True)]
    amenities = frappe.db.sql("""SELECT amenity, amenity_price FROM `tabProperty Amenity Item`;""", as_dict=True)
    status = ["SALE", "RENT", "LEASE"]

    house_images = []

    for n in range(1):
        house_image_url = "https://api.unsplash.com/search/photos?client_id=nPRqzHwZ-ei3t38DzHb9PCxC2PFUBQUHFLYrbJ2EaLA&query=mansions"
        img_api = requests.get(house_image_url)
        house_images += [
            {
                "doctype": "property",
                "property_name": i.get("alt_description"),  # Corrected: Added missing colon
                "image": i.get("urls").get("small"),
                "address": fake.address().replace("\n", ","),
                "agent": random.choice(agents),
                "city": random.choice(cities),
                "status": random.choice(status),
                "property_type": random.choice(property_types),
                "property_price": random.randint(1000000, 20000000),
                "discount": random.randint(0, 11),
                "description": fake.paragraph(nb_sentences=50, variable_nb_sentences=False),
                "amenities": amenities[random.randint(0, len(amenities) - 1)],
            }
            for i in img_api.json().get("results")   
        ]
    
    for p in house_images:
        try:
            pr = frappe.get_doc(p)
            property_name = pr.property_name
            existing_property = frappe.get_all('property', filters={'property_name': property_name})
            if not existing_property:
                # Proceed with insert
                pr.insert(ignore_permissions=True)
                print("Inserted property:", pr.name)
            else:
                # Handle the duplicate case
                print("Property already exists:", property_name)
        except Exception as e:
            print("Error while inserting property:", e)

    frappe.db.commit()

populate_house(fake)




# # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# #    rearanged code from the chatgpt

# # /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# # import frappe
# # from faker import Faker
# # import requests
# # import random

# # # Initialize Faker
# # fake = Faker('en_IN')
# # fake.seed_instance(0)  # Corrected: Use seed_instance instead of seed for Faker

# # # Fetch house images from Unsplash API
# # house_image_url = "https://api.unsplash.com/search/photos?client_id=nPRqzHwZ-ei3t38DzHb9PCxC2PFUBQUHFLYrbJ2EaLA&query=mansions"
# # house_image_data = requests.get(house_image_url)
# # house_image_data_json = house_image_data.json()

# # # Extract URLs of small-sized images
# # house_images = [i['urls']['small'] for i in house_image_data_json['results']]

# # def populate_house(fake):
# #     agents = [agent['name'] for agent in frappe.db.sql(""" SELECT name FROM `tabAgent`; """, as_dict=True)]
# #     cities = [city['name'] for city in frappe.db.sql(""" SELECT name FROM `tabCity`; """, as_dict=True)]
# #     property_types = [property['name'] for property in frappe.db.sql(""" SELECT name FROM `tabproperty type`; """, as_dict=True)]
# #     amenities = frappe.db.sql("""SELECT amenity, amenity_price FROM `tabproperty Amenity Item`;""", as_dict=True)
# #     status = ["sale", "rent", "lease"]

# #     house_images = []

# #     for i in house_image_data_json['results']:
# #         house_data = {
# #             "property_name": i.get("alt_description"),
# #             "image": i.get("urls").get("small"),
# #             "address": fake.address().replace("\n", ","),
# #             "agent": random.choice(agents),
# #             "status": random.choice(status),
# #             "property_type": random.choice(property_types),
# #             "property_price": random.randint(1000000, 20000000),
# #             "discount": random.randint(0, 10),
# #             "description": fake.paragraph(nb_sentences=10, variable_nb_sentences=False),
# #             "amenities": [amenities[random.randint(0, len(amenities) - 1)]],
# #         }
# #         house_images.append(house_data)

# #     for house in house_images:
# #         house_doc = frappe.get_doc({
# #             "doctype": "property",
# #             "property_name": house["property_name"],
# #             "status": house["status"],
# #             "address": house["address"],
# #             "grand_total": house["property_price"],
# #             "image": house["image"],
# #             "description": house["description"],
# #             "agent": house["agent"],
# #             "property_type": house["property_type"],
# #             "discount": house["discount"],
# #             "amenities": house["amenities"],
# #         })
# #         house_doc.insert(ignore_permissions=True)
# #         frappe.db.commit()

# #     print(house_images)

# # populate_house(fake)

# # /////////////////////////////////////////////////////////////////////////////////////////////////////



# # [amenities[random.randint(0, len(amenities) -1)]]
#     # for img in house_images:
#     #     house = frappe.get_doc({
#     #         "doctype": "property",
#     #         "property_name": "House" + str(frappe.db.count("property")+1),
#     #         # "status": "Available",
#     #         "address": fake.address(),
#     #         "grand_total": random.randint(1000000, 2000000),
#     #         "image": img
#     #     })
#         # frappe.db.commit()

#                 # house_image_data = requests.get(house_image_url)
#         # house_image_data_json = house_image_data.json()
#         # print(house_image_data_json)
#         # house_images = [i['urls']['small'] for i in house_image_data_json['results']]
#         # single_image_url = house_image_data_json.get("results")[0].get("urls").get("small")
#         # print(single_image_url)
#         # number_of_images = len(house_image_data_json.get("results"))
#         # print(number_of_images)
#         # house_images = [i.get("urls").get("small") for i in house_image_data_json.get("results")]
#         # print(house_images)

#         # print("inside the for loop 1")
# # import requests
# # import random
# # from faker import Faker

# # def get_house_images():
# #     fake = Faker()
# #     house_images = []
# #     house_image_url = "https://api.unsplash.com/search/photos?client_id=nPRqzHwZ-ei3t38DzHb9PCxC2PFUBQUHFLYrbJ2EaLA&query=mansions"

# #     try:
# #         response = requests.get(house_image_url)
# #         response.raise_for_status()
# #         house_image_data_json = response.json()
# #         images = house_image_data_json.get("results")

# #         for image in images:
# #             print(f"Processing image: {image.get('alt_description')}")
# #             house_image = {
# #                 "property_name": image.get("alt_description"),
# #                 "image": image.get("urls").get("small"),
# #                 "address": fake.address().replace("\n", ","),
# #                 "agent": fake.name(),
# #                 "status": random.choice(["sale", "rent", "lease"]),
# #                 "property_type": fake.word(),
# #                 "property_price": random.randint(1000000, 20000000),
# #                 "discount": random.randint(0, 11),
# #                 "description": fake.paragraph(nb_sentences=10, variable_nb_sentences=False),
# #                 "amenities": fake.text()
# #             }
# #             house_images.append(house_image)

# #     except requests.exceptions.RequestException as e:
# #         print(f"Error: {e}")

# #     return house_images

# # house_images = get_house_images()
# # print(house_images)

# # house_image_url = "https://api.unsplash.com/search/photos?client_id=nPRqzHwZ-ei3t38DzHb9PCxC2PFUBQUHFLYrbJ2EaLA&query=mansions"
# # house_image_data = requests.get(house_image_url)
# # house_image_data_json = house_image_data.json()
# # print(house_image_data_json)
# # house_images = [i['urls']['small'] for i in house_image_data_json['results']]
# # single_image_url = house_image_data_json.get("results")[0].get("urls").get("small")
# # print(single_image_url)
# # number_of_images = len(house_image_data_json.get("results"))
# # print(number_of_images)
# # house_images = [i.get("urls").get("small") for i in house_image_data_json.get("results")]
# # print(house_images)
# # # house_images = []
# # # agents = [agent.name for agent in frappe.db.sql(""" SELECT name FROM `tabproperty type` ;""", as_dict=True)]
# # # status = ["sale" , "rent" , "lease"]
# # # for n in range(50):
# # #     house_image_url = "https://api.unsplash.com/search/photos?client_id=nPRqzHwZ-ei3t38DzHb9PCxC2PFUBQUHFLYrbJ2EaLA&query=mansions"
# # #     img_api = requests.get(house_image_url)
# # #     house_images += [
# # #         {"property_name"i.get("alt_description"),
# # #          "image":i.get("urls").get("small"),
# # #          "address" : fake.address(),replace("\n",","), "property_name":i.get("alt_description")},
# # #          "agent" : random.choice(agents),
# # #          "status" : random.choice(status),
         
# # #         } ]
# # # for i in house_image_data.json().get("results")]
# # # print(house_images)
# # # len(house_images)