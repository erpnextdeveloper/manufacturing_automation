# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe
import json
from frappe import _
from frappe.utils import flt, get_datetime, getdate, date_diff, cint, nowdate
from frappe.model.document import Document
from erpnext.manufacturing.doctype.bom.bom import validate_bom_no, get_bom_items_as_dict
from dateutil.relativedelta import relativedelta
from erpnext.stock.doctype.item.item import validate_end_of_life
from erpnext.manufacturing.doctype.workstation.workstation import WorkstationHolidayError
from erpnext.projects.doctype.timesheet.timesheet import OverlapError
from erpnext.stock.doctype.stock_entry.stock_entry import get_additional_costs
from erpnext.manufacturing.doctype.manufacturing_settings.manufacturing_settings import get_mins_between_operations
from erpnext.stock.stock_balance import get_planned_qty, update_bin_qty
from frappe.utils.csvutils import getlink
from erpnext.stock.utils import get_bin, validate_warehouse_company, get_latest_stock_qty
from erpnext.utilities.transaction_base import validate_uom_is_integer



@frappe.whitelist()
def after_submit_work_order(self,method):
	make_stock_entry(self.name,'Material Transfer for Manufacture')
	make_stock_entry(self.name,'Manufacture')


@frappe.whitelist()
def make_stock_entry(work_order_id, purpose, qty=None):
	work_order = frappe.get_doc("Work Order", work_order_id)
	if not frappe.db.get_value("Warehouse", work_order.wip_warehouse, "is_group") \
			and not work_order.skip_transfer:
		wip_warehouse = work_order.wip_warehouse
	else:
		wip_warehouse = None

	stock_entry = frappe.new_doc("Stock Entry")
	stock_entry.purpose = purpose
	stock_entry.work_order = work_order_id
	stock_entry.company = work_order.company
	stock_entry.from_bom = 1
	stock_entry.bom_no = work_order.bom_no
	stock_entry.set_posting_time=1
	stock_entry.posting_date=getdate(work_order.planned_start_date)
	stock_entry.use_multi_level_bom = work_order.use_multi_level_bom
	stock_entry.fg_completed_qty = qty or (flt(work_order.qty) - flt(work_order.produced_qty))
	if work_order.bom_no:
		stock_entry.inspection_required = frappe.db.get_value('BOM',
			work_order.bom_no, 'inspection_required')

	if purpose=="Material Transfer for Manufacture":
		stock_entry.to_warehouse = wip_warehouse
		stock_entry.project = work_order.project
	else:
		stock_entry.from_warehouse = wip_warehouse
		stock_entry.to_warehouse = work_order.fg_warehouse
		stock_entry.project = work_order.project
		if purpose=="Manufacture":
			additional_costs = get_additional_costs(work_order, fg_qty=stock_entry.fg_completed_qty)
			stock_entry.set("additional_costs", additional_costs)

	stock_entry.get_items()
	doc=stock_entry.submit()

