import frappe
from real_estate.real_estate.utils import sendmail
# (doc, recipients, msg, title, attachments=None):

# contact email agent from the preoperty page 
@frappe.whitelist(allow_guest=True)
def contact_agent(**args):
    print(args)
    print('called')

    return args