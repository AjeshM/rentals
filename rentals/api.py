import frappe

# @frappe.whitelist(allow_guest=True)


@frappe.whitelist(allow_guest=True)
def get_emoji():
    return "💰"


def throw_emoji(doc, event):
    frappe.throw("🎯")


def send_payment_reminders():
    pass


def get_query_conditions_for_vehicle(user):
    # return "name=1"
    return ""
