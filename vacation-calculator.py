#!/usr/bin/python -t
# -*- coding: utf-8 -*-
# coding=utf-8
#
# This script is written by Alessandro Accardo
# This peace of software is licensed under the terms of the GNU GPL v3
# Copyright © Alessandro Accardo 2014. All rights reserved.
#
import vobject
from datetime import date

class Event:
	def printEvent(evt):
		print evt.Title + ' <' + evt.Description + '> ' + evt.Date.strftime('%d %B %Y')


data = open("/home/kLeZ-hAcK/Calendario-KOrganizer/std.ics").read()

cal = vobject.readComponents(data, validate=True)

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
				e.Title = child.summary.value
			else: e.Title = ''
			if hasattr(child, 'description'):
				e.Description = child.description.value
			else: e.Description = ''
			if hasattr(child, 'dtstart'):
				e.Date = child.dtstart.value
			else: e.Date = date.fromtimestamp(0)
			e.printEvent()
