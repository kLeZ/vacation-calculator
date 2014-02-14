# -*- coding: utf-8 -*-
# coding=utf-8
#
# This script is written by Alessandro Accardo
# This peace of software is licensed under the terms of the GNU GPL v3
# Copyright © Alessandro Accardo 2014. All rights reserved.
#

from PyQt4.QtCore import Qt
from PyKDE4.plasma import Plasma
from PyKDE4 import plasmascript

import vobject
from event import *
from vacation import *

class VacationCalculator(plasmascript.Applet):
	def __init__(self,parent,args=None):
		plasmascript.Applet.__init__(self,parent)
		data = open("/home/kLeZ-hAcK/Calendario-KOrganizer/std.ics").read()
		cal = vobject.readComponents(data, validate=True)
		evts = Event.readCal(cal)
		self.Vacation = Vacation()
		self.Vacation.calculateMatured()
		self.Vacation.calculateAvailable(evts)

	def init(self):
		self.setHasConfigurationInterface(False)
		self.resize(125, 125)
		self.setAspectRatioMode(Plasma.Square)

	def paintInterface(self, painter, option, rect):
		painter.save()
		painter.setPen(Qt.white)
		painter.drawText(rect, Qt.AlignVCenter | Qt.AlignHCenter, self.Vacation)
		painter.restore()

def CreateApplet(parent):
	return VacationCalculator(parent)
