import frappe
from  real_estate.utils import paginate

def get_context(context):
    page = frappe.form_dict.page or 1  # Default to the first page if not provided
    conditions = []
    
    # Retrieve filter parameters from the form
    type = frappe.form_dict.get('type')
    status = frappe.form_dict.get('status')
    city = frappe.form_dict.get('city')

    # Build conditions based on available filters
    if type:
        conditions.append(f"property_type = '{type}'")
    if status:
        conditions.append(f"status = '{status}'")
    if city:
        conditions.append(f"city = '{city}'")
    
    # Join conditions with 'AND' if any condition is available
    conditions_str = " AND ".join(conditions)
    if conditions_str:
        conditions_str = f"WHERE {conditions_str}"

    # Pass to pagination
    pagination = paginate(doctype="property", page=page, conditions=conditions_str)
    
    context.properties = pagination.get("properties")
    context.cities = frappe.db.sql("""SELECT name FROM `tabcity`;""", as_dict=True)
    context.types = frappe.db.sql("""SELECT name FROM `tabproperty type`;""", as_dict=True)
    context.prev = pagination.get("prev")
    context.next = pagination.get("next")
    return context   


# self written code starts from here the above is the rectified code through the chatgpt

# def get_context(context):
#     page = frappe.form_dict.page
# #  check if search request
    # conditions = "" 
#     type,status,city = frappe.form_dict.type , frappe.form_dict.status , frappe.form_dict.city 
#     print(type, status, city,)
#     if(type and status and city,):
#         conditions = f""" WHERE property_type = '{type}', AND city = '{city}' , AND status = '{status}'"""
#  #pass to pagination 
#     print("inside the first if statement")
#     pagination = paginate(doctype = "property" , page = page, conditions = conditions) 
#     context.properties = pagination.get("properties")
#     context.cities = frappe.db.sql(""" SELECT name FROM `tabcity`; """, as_dict= True)
#     # context.status = frappe.db.sql(""" SELECT status FROM `tabstatus`; """, as_dict= True)
#     context.types =frappe.db.sql(""" SELECT name FROM `tabproperty type`; """, as_dict = True)
#     context.prev = pagination.get("prev")
#     context.next = pagination.get("next")
#     print(context.types,context.prev,context.properties)
#     print("end of the index.py")

#     return context
    # properties = frappe.db.sql(""" 
    #     SELECT name, property_name, status, address, grand_total, image FROM `tabproperty` ORDER BY creation DESC;""", 
    #     as_dict = True)
    # context.properties = properties   
    # 
    # 
    # 
    # 
    # def get_context(context):