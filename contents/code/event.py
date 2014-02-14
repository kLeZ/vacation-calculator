# -*- coding: utf-8 -*-
# coding=utf-8
#
# This script is written by Alessandro Accardo
# This peace of software is licensed under the terms of the GNU GPL v3
# Copyright © Alessandro Accardo 2014. All rights reserved.
#

from datetime import date

class Event:
	def __init__(self, title = '', desc = '', evtdate = date.today()):
		self.Title = title
		self.Description = desc
		self.Date = evtdate

	def __str__(self):
		return "%s <%s> %s" % self.Title, self.Description, self.Date.strftime('%d %B %Y')

	@staticmethod
	def readCal(cal, desc = False):
		ret = list()
		for component in cal:
			for child in component.getChildren():
				#
				# BEGIN:VJOURNAL
				# DTSTAMP:20131018T174355Z
				# CREATED:20131018T174355Z
				# UID:libkcal-1002282423.811
				# LAST-MODIFIED:20131018T174355Z
				# DESCRIPTION:Influenza intestinale.
				# SUMMARY:Assenza
				# CATEGORIES:Malattia
				# DTSTART;VALUE=DATE:20131016
				# END:VJOURNAL
				#

				if child.name == 'VJOURNAL':
					e = Event()
					if hasattr(child, 'summary'):
						e.Title = child.summary.value.encode('utf-8')
					else: e.Title = ''
					if hasattr(child, 'description'):
						e.Description = child.description.value.encode('utf-8')
					else: e.Description = ''
					if hasattr(child, 'dtstart'):
						e.Date = child.dtstart.value
					else: e.Date = date.fromtimestamp(0)
					ret.append(e)
		return sorted(ret, key=lambda event: event.Date, reverse = desc)
