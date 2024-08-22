# Copyright (c) 2024, ateeq' and contributors
# For license information, please see license.txt
from __future__ import unicode_literals
from frappe import _
import frappe


def execute(filters=None):
	# columns, data = [], []
	# return columns, data
	return get_columns, get_data(filters)

def get_columns():
	return[

	]