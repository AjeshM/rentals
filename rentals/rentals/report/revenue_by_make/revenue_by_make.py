# Copyright (c) 2025, Ajesh Meshram and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
    frappe.errprint(filters)
    columns = [
        {"fieldname": "make", "label": "Make", "fieldtype": "Data"},
        {
            "fieldname": "total_revenue",
            "label": "Total Revenue",
            "fieldtype": "Currency",
            "options": "USD",
        },
    ]
    data = frappe.get_all(
        "Rental_Ride_Booking",
        fields=["SUM(total_amount)as total_revenue", "vehicle.make"],
        filters={"docstatus": 1},
        group_by="make",
    )
    chart = {
        "data": {
            "labels": [x.make for x in data],
            "datasets": [{"values": [x.total_revenue for x in data]}],
        },
        "type": "pie",
    }
    return columns, data, "Message Summary", chart, None
