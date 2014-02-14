#!/bin/bash
#
# This script was written by Alessandro Accardo
# This peace of software is licensed under the terms of the GNU GPL v3
# Copyright © Alessandro Accardo 2014. All rights reserved.
#

plasmapkg -r vacation-calculator.plasmoid
rm vacation-calculator.plasmoid
zip -r vacation-calculator.zip ./{README.md,LICENSE,metadata.desktop,contents}
mv vacation-calculator.zip vacation-calculator.plasmoid
plasmapkg -i vacation-calculator.plasmoid
plasmoidviewer vacation-calculator
