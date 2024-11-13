import frappe
from faker import Faker
import requests
import random

fake = Faker('en_IN')
import frappe
import random
import requests

def populate_house(fake):
    agents = [agent['name'] for agent in frappe.db.sql("""SELECT name FROM `tabAgent`;""", as_dict=True)]
    cities = [city['name'] for city in frappe.db.sql("""SELECT name FROM `tabCity`;""", as_dict=True)]
    property_types = [property['name'] for property in frappe.db.sql("""SELECT name FROM `tabproperty type`;""", as_dict=True)]
    amenities = [amenity['name'] for amenity in frappe.db.sql("""SELECT name FROM `tabProperty Amenity Item`;""", as_dict=True)]
    status = ["SALE", "RENT", "LEASE"]

    house_images = []

    # Fetching house images from Unsplash
    house_image_url = "https://api.unsplash.com/search/photos?client_id=nPRqzHwZ-ei3t38DzHb9PCxC2PFUBQUHFLYrbJ2EaLA&query=house&per_page=30&page=6"
    img_api = requests.get(house_image_url)
    
    house_images += [
        {
            "doctype": "property",
            "property_name": i.get("alt_description"),
            "image": i.get("urls").get("small"),
            "address": fake.address().replace("\n", ","),
            "agent": random.choice(agents),
            "city": random.choice(cities),
            "status": random.choice(status),
            "property_type": random.choice(property_types),
            "property_price": random.randint(1000000, 20000000),
            "discount": random.randint(0, 11),
            "description": fake.paragraph(nb_sentences=50, variable_nb_sentences=False),
            
            # Child table data for two random amenities
            "amenity": [
                {
                    "doctype": "Property Amenity Detail",
                    "amenity_name": amenity,
                    "amenity_price": random.randint(10000, 50000),
                    "amenity_discount": random.randint(0, 20),
                }
                for amenity in random.sample(amenities, 2)  # Randomly select 2 amenities
            ]
        }
        for i in img_api.json().get("results")
    ]
    
    # Insert each property with its amenities
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