# Copyright (c) 2025, Technovate Solutions and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
    return get_columns(), get_data()

def get_data():
    return frappe.db.sql(""" SELECT sabe.serial_no, sabb.voucher_no, si.customer, si.posting_date, sii.item_code, si.company, sii.rate, si.party_code, si.sales_person
								FROM `tabSales Invoice` as si
								JOIN `tabSerial and Batch Bundle` as sabb ON sabb.voucher_no = si.name and sabb.voucher_type = "Sales Invoice"
								JOIN `tabSerial and Batch Entry` as sabe ON sabe.parent = sabb.name 
        						JOIN `tabSales Invoice Item` as sii ON sii.parent = si.name and sii.serial_and_batch_bundle = sabb.name""")

def get_columns():
    columns = [
		{
			"fieldname": "serial_no",
			"label": "Serial No",
			"fieldtype": "Link",
			"options": "Serial No",
			"width": 120,
		},
		{
			"fieldname": "item",
			"label": "Item",
			"fieldtype": "Link",
			"options": "Item",
			"width": 120,
		},
		{
			"fieldname": "item_code",
			"label": "Item Code",
			"fieldtype": "Data",
			"width": 120,
		},
		{
			"fieldname": "company_name",
			"label": "Company Name",
			"fieldtype": "Data",
			"width": 120,
		},
		{
			"fieldname": "invoice_id",
			"label": "Invoice No",
			"fieldtype": "Link",
			"options": "Sales Invoice",
			"width": 120,
		},
		{
			"fieldname": "posting_date",
			"label": "Date",
			"fieldtype": "Date",
			"width": 120,
		},
		{
			"fieldname": "customer",
			"label": "Customer",
			"fieldtype": "Link",
			"options": "Customer",
			"width": 120,
		},
		{
			"fieldname": "sales_rate",
			"label": "Sales Rate",
			"fieldtype": "Currency",
			"width": 120,
		},
		{
			"fieldname": "party_code",
			"label": "Party Code",
			"fieldtype": "Data",
			"width": 120,
		},
		{
			"fieldname": "salesman",
			"label": "Salesman",
			"fieldtype": "Link",
   			"options": "Sales Person",
			"width": 120,
		},
	]
    
    return columns
