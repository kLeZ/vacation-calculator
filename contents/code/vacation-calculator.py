#!/usr/bin/python -t
# -*- coding: utf-8 -*-
# coding=utf-8
#
# This script was written by Alessandro Accardo
# This peace of software is licensed under the terms of the GNU GPL v3
# Copyright © Alessandro Accardo 2014. All rights reserved.
#

import vobject
from event import *
from vacation import *

data = open("/home/kLeZ-hAcK/Calendario-KOrganizer/std.ics").read()
cal = vobject.readComponents(data, validate=True)
evts = Event.readCal(cal)
v = Vacation()
v.calculateMatured()
v.calculateAvailable(evts)
print v
