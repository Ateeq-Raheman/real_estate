# Copyright (c) 2024, ateeq' and contributors
# For license information, please see license.txt




# class property(Document):
# 	def after_insert(self):
# 		frappe.msgprint((f"Document{self.name} has been inserted"));
	

# 	def validate(self):
# 		amenity_prices = 0
# 		for i in self.amenities:
# 			amenities_price += i.amenity_price
# 		discount = 0
# 		self.grand_total = In [53] : self.property_price + amenity_prices- ((0/100)*(self.property_price + amenity_prices))

import frappe
from frappe.model.document import Document
class property(Document):
    # pass

    def after_insert(self):
        frappe.msgprint(f"Document {self.name} has been inserted")

    def validate(self):
        amenity_prices = 0
        
        for i in self.amenity:
            # Ensure amenity_price is converted to a float or int
            amenity_prices += float(i.amenity_price)  # or int(), depending on your needs
        
        discount = 0  # Assuming discount calculation happens elsewhere or is defined later
        
        # Calculate the grand total using the correct variable name and proper arithmetic
        self.grand_total = self.property_price + amenity_prices - ((self.discount / 100) * (self.property_price + amenity_prices))
        
    #     # self.save()  # Save the changes to the document
    # def validate(self):
    # # Ensure property_price is not None
    #     if self.property_price is None:
    #         frappe.throw(("Property Price cannot be None"))
        
    #     # Calculate the total price for amenities
    #     amenity_prices = 0
    #     # for amenity in self.amenities:
    #     #     if amenity.amenity_price is not None:
    #     #         amenity_prices += amenity.amenity_price
        
    #     # Set a default value for discount if it is None
    #     if self.discount is None:
    #         self.discount = 0
        
    #     # Calculate grand total
    #     self.grand_total = self.property_price + amenity_prices - ((self.discount / 100) * (self.property_price + amenity_prices))
