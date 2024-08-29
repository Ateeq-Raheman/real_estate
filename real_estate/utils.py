import frappe
def paginate(doctype, page=1, conditions="", paginate_by=4):
    prev, next = 0, 0
    query = f"""
        SELECT name, property_name, status, address, grand_total, image 
        FROM `tab{doctype}` {conditions} 
        ORDER BY creation DESC
    """

    if page:
        page = int(page)
        properties = frappe.db.sql(
            query + f" LIMIT {(page*paginate_by)-paginate_by}, {paginate_by}", 
            as_dict=True
        )
        next_set = frappe.db.sql(
            query + f" LIMIT {page*paginate_by}, {paginate_by}", 
            as_dict=True
        )
        if next_set:
            prev, next = page - 1, page + 1
        else:
            prev, next = page - 1, 0
    else:
        count = frappe.db.sql(f"SELECT COUNT(name) as count FROM `tab{doctype}` {conditions};", as_dict=True)[0].count
        if count > paginate_by:
            prev, next = 0, 2
        properties = frappe.db.sql(query + f" LIMIT {paginate_by};", as_dict=True)

    return {
        "properties": properties,
        "prev": prev,
        "next": next,
    }
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# custom code for send mail code 

# def sendmail(doc, recipients, msg, title, attachments = None):
#     email_args = {
#         'recipients': recipients,
#         'message': msg,
#         'subject': title,
#         'reference_doctype': doc.doctype,
#         'reference_name': doc.name
#     }
    
#     if attachments:
#         email_args['attachments'] = attachments
    
#     frappe.enqueue(method = frappe.sendmail, queue = 'short', timeout = 300, **email_args)

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# self written code starts from here the above is the rectified code through the chatgpt

# def paginate(doctype, page=0, conditions = " ", paginate_by = 4):
#     prev,next,search = 0 , 0 , False
#     conditions = " "
#     query = f"""SELECT name, property_name, status , address , grand_total ,
#                 image FROM `tab{doctype}` {conditions} ORDER BY CREATION DESC """

#     if (page):
#         page = int(page)
#         properties = frappe.db.sql(query + f"""LIMIT {(page*paginate_by)-paginate_by}, {paginate_by}""", as_dict=True)
#         next_set = frappe.db.sql(query + f"""LIMIT {page*paginate_by}, {paginate_by}""", as_dict=True)
#         if(next_set):
#             prev, next = page-1, page+1
#         else:
#             prev, next = page-1, 0
#     else:
#         count = frappe.db.sql(f""" SELECT COUNT(name) as count FROM `tab{doctype}`; """ , as_dict = True)[0].count
#         if(count>paginate_by):
#             prev, next = 0,2
#         else:
#             pass
#         properties = frappe.db.sql(query+f"""LIMIT {paginate_by};""", as_dict = True)

#     if(conditions):search = True
#     return{
#         "properties" : properties,
#         "prev" : prev, 
#         "next":next,
#         "search":search,
#     }