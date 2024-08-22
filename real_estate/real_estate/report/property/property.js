// Copyright (c) 2024, ateeq' and contributors
// For license information, please see license.txt

frappe.query_reports["property"] = {
	"filters": [
		{
			"fieldname": "propert_name",
			"label": ("Property name"),
			"fieldtype": "Data",
			"Width": 100,
			"reqd": 0
		},
		// {
		// 	"fieldname": "from",
		// 	"Label": ("From Date"),
		// 	"fieldtype": "Data",
		// 	"Width": 100,
		// 	"reqd": 0,
		// 	default: dateutil.year_start()

		// },
		// {
		// 	"fieldname": "to",
		// 	"Label": ("Property name"),
		// 	"fieldtype": "Date",
		// 	"Width": 100,
		// 	"reqd": 0,
		// 	default: dateutil.year_end()
		// },
		{
			"fieldname": "agent",
			"label": ("Agent name"),
			"fieldtype": "Link",
			"options": "Agent",
			"Width": 100,
			"reqd": 0,
		},
		{
			"fieldname": "status",
			"label": ("status"),
			"fieldtype": "Select",
			"options": ["SALE", "RENT", "LEASE"],
			"Width": 100,
			"reqd": 0,
		}

	]
};
