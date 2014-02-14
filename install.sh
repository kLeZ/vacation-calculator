#!/bin/bash
#
# This script was written by Alessandro Accardo
# This peace of software is licensed under the terms of the GNU GPL v3
# Copyright © Alessandro Accardo 2014. All rights reserved.
#

plasmapkg -r plasma-applet-vacation-calculator.plasmoid
rm plasma-applet-vacation-calculator.plasmoid
zip -r vacation-calculator.zip ./{README.md,LICENSE,metadata.desktop,contents}
mv vacation-calculator.zip plasma-applet-vacation-calculator.plasmoid
plasmapkg -i plasma-applet-vacation-calculator.plasmoid
plasmoidviewer vacation-calculator
