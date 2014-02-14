# -*- coding: utf-8 -*-
# coding=utf-8
#
# This script is written by Alessandro Accardo
# This peace of software is licensed under the terms of the GNU GPL v3
# Copyright © Alessandro Accardo 2014. All rights reserved.
#

from datetime import date

class Vacation:
	def __init__(self, totalVacations = 26.0):
		self.VacationsMatured = 0.0
		self.VacationsAvailable = totalVacations
		self.TotalVacations = totalVacations

	def calculateMatured(self):
		self.VacationsMatured = float((self.VacationsAvailable / 12.0) * date.today().month)

	def calculateAvailable(self, events):
		vacationsAvailable = self.TotalVacations
		for evt in filter(lambda e: e.Date.year == date.today().year, events):
			vacationsAvailable = vacationsAvailable - 1.0
			if (evt.Date.isoweekday() == 5):
				vacationsAvailable = vacationsAvailable - 1.0
		self.VacationsAvailable = vacationsAvailable

	def __str__(self):
		return 'Since today in this year there are %(VacationsMatured)f vacation days matured\nThere are still %(VacationsAvailable)f vacation days available' % { "VacationsMatured": self.VacationsMatured, "VacationsAvailable": self.VacationsAvailable }
