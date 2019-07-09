# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "manufacturing_automation"
app_title = "Manufacturing Automation"
app_publisher = "BJJ"
app_description = "Automatic work order submit"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "maheshwaribhavesh95863@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/manufacturing_automation/css/manufacturing_automation.css"
# app_include_js = "/assets/manufacturing_automation/js/manufacturing_automation.js"

# include js, css files in header of web template
# web_include_css = "/assets/manufacturing_automation/css/manufacturing_automation.css"
# web_include_js = "/assets/manufacturing_automation/js/manufacturing_automation.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "manufacturing_automation.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "manufacturing_automation.install.before_install"
# after_install = "manufacturing_automation.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "manufacturing_automation.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
 	"Work Order": {
 		"on_submit": "manufacturing_automation.api.after_submit_work_order"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"manufacturing_automation.tasks.all"
# 	],
# 	"daily": [
# 		"manufacturing_automation.tasks.daily"
# 	],
# 	"hourly": [
# 		"manufacturing_automation.tasks.hourly"
# 	],
# 	"weekly": [
# 		"manufacturing_automation.tasks.weekly"
# 	]
# 	"monthly": [
# 		"manufacturing_automation.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "manufacturing_automation.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "manufacturing_automation.event.get_events"
# }

