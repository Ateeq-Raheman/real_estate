# Copyright (c) 2024, ateeq' and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


# class property(Document):
# 	def after_insert(self):
# 		frappe.msgprint((f"Document{self.name} has been inserted"));
	

# 	def validate(self):
# 		amenity_prices = 0
# 		for i in self.amenities:
# 			amenities_price += i.amenity_price
# 		discount = 0
# 		self.grand_total = In [53] : self.property_price + amenity_prices- ((0/100)*(self.property_price + amenity_prices))


class property(Document):
    # pass

    def after_insert(self):
        frappe.msgprint(f"Document {self.name} has been inserted")

    # def validate(self):
    #     amenity_prices = 0
    #     for i in self.amenities:
    #         amenity_prices += i.amenity_price
    #     discount = 0  # Assuming you will calculate discount elsewhere or this needs to be defined
    #     # Calculate the grand total
    #     self.grand_total = self.property_price + amenity_prices - ((0 / 100) * (self.property_price + amenity_prices))
