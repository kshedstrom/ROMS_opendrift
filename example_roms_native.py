#!/usr/bin/env python
"""
ROMS native reader
==================================
"""

import numpy as np
import subprocess
from datetime import datetime, timedelta, date
from opendrift.readers.reader_ROMS_native import Reader
from opendrift.models.oceandrift import OceanDrift
import sys

o = OceanDrift(loglevel=20)  # Set loglevel to 0 for debug information

flist = ['/import/AKWATERS/kshedstrom/gridpak/Arctic2/Arctic4_plus.nc']

#year = sys.argv[1]
#month = sys.argv[2]
year = '2001'
month = '03'

#%%
# Creating and adding reader for Nordic 4km current dataset
#nordic_native = reader_ROMS_native.Reader(o.test_data_folder() +
#    '2Feb2016_Nordic_sigma_3d/Nordic-4km_SLEVELS_avg_00_subset2Feb2016.nc')
r = Reader('/import/AKWATERS/kshedstrom/Arctic4/run16/averages/arctic4_avg_' + year + '-03*nc', gridfile='/import/AKWATERS/kshedstrom/gridpak/Arctic2/grid_Arctic_4.nc')
o.add_reader(r)

#%%
# Seed elements at defined positions, depth and time
o.seed_elements(lon=-168.4, lat=66.65, radius=10000, number=600,
                time=datetime(2001, 3, 1))

#%%
# Running model
#o.run(time_step=3600)
o.run(time_step=timedelta(minutes=30),
       duration=timedelta(days=25))

#%%
# Print and plot results, with lines colored by particle depth
print(o)
o.plot(linecolor='z', fast=True)
#o.animation()
