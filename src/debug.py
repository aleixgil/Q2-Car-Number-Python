#coding: UTF-8

from colors import *
import time
from tabulate import *

class Debug(object):

	m = []

	def __init__(self, m = ""):
		if not m:
			table = []
			headers = [color.BOLD + "Time" + color.ENDC, color.BOLD + "Message" + color.ENDC]
			try:
				print color.BOLD + " ==== DEBUG INFORMATION ====" + color.ENDC
				for i in Debug.m:
					table_in = []
					table_in += [green(i[0])]
					table_in += [i[1]]
					table += [table_in]
				table_in = []
				table_in += [green(time.strftime('%X'))]
				table_in += [success('Printing Debug')]
				table += [table_in]
				print tabulate(table, headers, tablefmt='fancy_grid')
			except:
				table = [[green(time.strftime('%X')), error("Can't debug")]]
				print tabulate(table, headers, tablefmt='fancy_grid')
		else:
			try:
				m2 = [time.strftime('%X'), m]
				Debug.m += [m2]
			except:
				already = False
				for i in Debug.m:
					if i[1] == warning("Can't add message to debug"):
						already = True
				if not already:
					m2 = [time.strftime('%X'), warning("Can't add message to debug")]
					Debug.m += [m2]
