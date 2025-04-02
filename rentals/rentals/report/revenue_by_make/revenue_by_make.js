// Copyright (c) 2025, Ajesh Meshram and contributors
// For license information, please see license.txt

frappe.query_reports["Revenue by Make"] = {
	"filters": [
		{
			fieldname: "my_filter",
			label: "My filter",
			fieldtype:"Link",
			options:"Rental_Vehicle"
		}
	]
};
