import frappe


def execute():
    vehicles = frappe.db.get_all("Rental_Vehicle", pluck="name")
    for v in vehicles:
        vehicle = frappe.get_doc("Rental_Vehicle", v)
        vehicle.set_title()
        vehicle.save()

    frappe.db.commit()
