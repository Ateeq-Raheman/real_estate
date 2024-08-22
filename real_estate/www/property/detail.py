import frappe 

def get_context(context):
    # print(f"\n\n\n\n\n\n{frappe.form_dict}\n\n\n\n\n\n\n\n\n\n\n\n\n")
    try:
        docname = frappe.form_dict.docname
        context.property = frappe.get_doc("property",frappe.form_dict.docname)
        context.agent = frappe.get_doc("Agent", context.property.agent)
        related_properties = frappe.db.sql(f"""
        SELECT name, creation ,property_name, status, address, grand_total, image
        FROM `tabproperty`
        WHERE property_type="{context.property.property_type}"
        AND name  != '{context.property.name}'
        ORDER BY creation DESC LIMIT 3;
          """, as_dict= True) 
        context.related_properties = related_properties
    except Exception as e:
        frappe.local.flags.redirect_location = "/404" 
        raise frappe.Redirect

    return context  