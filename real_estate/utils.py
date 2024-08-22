import frappe

def sendmail(doc, recipients, msg, title, attachments = None):
    email_args = {
        'recipients': recipients,
        'message': msg,
        'subject': title,
        'reference_doctype': doc.doctype,
        'reference_name': doc.name
    }
    
    if attachments:
        email_args['attachments'] = attachments
    
    frappe.enqueue(method = frappe.sendmail, queue = 'short', timeout = 300, **email_args)



# def paginate(doctype, page=0):
#     prev,next = 0 , 0 
#     conditions = ""
#     query = f"""SELECT name, property_name, status , address , grand_total , 
#                 image FROM `tab{doctype}` {conditions} ORDER BY CREATION DESC """
    

#     if (page):
#         pass
#     else:
#         count = frappe.db.sql(""" SELECT COUNT(name) as count FROM `tab{doctype}`; """ , as_dict = True)[0].count
#         if(count>4):
#             prev,next=0,2
#         else:
#             pass
#         properties = frappe.db.sql(query+"""LIMIT 4;""", as_dict = True)
#     return{
#         "properties" : properties,
#         "prev" : prev, 
#          "next":next
#     }