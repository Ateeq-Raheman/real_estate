import frappe

@frappe.whitelist()
def get_total_price():  
    total =  frappe.db.sql("""select sum(grand_total) as total from `tabproperty`""", as_dict = True)[0].total
    return total

@frappe.whitelist()
def get_property_price_by_status():
    price = frappe.db.sql("""select status,sum(grand_total) from `tabproperty` group by status order by status asc;""" )
    return price