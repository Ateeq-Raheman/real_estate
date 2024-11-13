import frappe

def get_context(context):
    context.title = "Frappe-Vue"

@frappe.whitelist(allow_guest=True)
def get_properties():
    return frappe.db.sql(""" 
        SELECT name, property_name, property_type, status, address, grand_total, image, city FROM `tabproperty` LIMIT 100;""", 
        as_dict = True)
    # print(properties)
    