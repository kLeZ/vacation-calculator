# -*- coding: utf-8 -*-
# coding=utf-8
#
# This script was written by Alessandro Accardo
# This peace of software is licensed under the terms of the GNU GPL v3
# Copyright © Alessandro Accardo 2014. All rights reserved.
#
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyKDE4.plasma import Plasma
from PyKDE4 import plasmascript
from PyKDE4 import kdeui

import os
import vobject

from event import *
from vacation import *
from config_ui import *

class VacationCalculator(plasmascript.Applet):
	def __init__(self,parent,args=None):
		plasmascript.Applet.__init__(self,parent)

	def init(self):
		self.setHasConfigurationInterface(False)

		self.icalpath = "%s/Calendario-KOrganizer/std.ics" % os.path.expanduser("~/")
		self.totalVacationDays = 26.0

		self.resize(400, 100)
		self.setAspectRatioMode(Plasma.Square)

		data = open(self.icalpath).read()
		cal = vobject.readComponents(data, validate=True)
		evts = Event.readCal(cal)
		self.Vacation = Vacation(self.totalVacationDays)
		self.Vacation.calculateMatured()
		self.Vacation.calculateAvailable(evts)

	def paintInterface(self, painter, option, rect):
		painter.save()
		painter.setPen(Qt.black)
		painter.drawText(rect, Qt.AlignVCenter | Qt.AlignHCenter, QString(str(self.Vacation)))
		painter.restore()

def CreateApplet(parent):
	return VacationCalculator(parent)
