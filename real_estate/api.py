import frappe
# from real_estate.utils import sendmail
# (doc, recipients, msg, title, attachments=None):

# contact email agent from the preoperty page 
@frappe.whitelist(allow_guest=True)
def contact_agent(**args):
    doc = frappe.get_doc("property", args.get("property_name"))
    print(args)
    print('called')
    print(args.get('property_name'), args['property_name'])
    msg = f"From: {args.get('name')} <br> {args.get('email')} <br> {args.get('message')}"
    attachments = [frappe.attach_print(doc, doc.doctype, file_name = doc.name)]
    # frappe.sendmail( [args.get("agent_email")], args.get("message"), subject = "property enquiry" , attachments=attachments)
    frappe.sendmail(
    recipients=[args.get("agent_email")],
    subject="property enquiry",
    args=dict(
         message=args.get("message"),
    ),
)
    return "message sent to Agent you will be responded as soon as possible Thank you."
