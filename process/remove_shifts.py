"""
"""

#! /usr/bin/env python
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

# make an example cxi file
# with a small sample and small aberations

import sys, os
base = os.path.join(os.path.dirname(__file__), '..')
root = os.path.abspath(base)
sys.path.insert(0, os.path.join(root, 'utils'))

#import pyximport; pyximport.install()
import cmdline_config_cxi_reader

import numpy as np
import h5py

def get_input():
    args, params = cmdline_config_cxi_reader.get_all('remove_shifts',
                   'setting pixel shifts along one direction to zero')
    params = params['remove_shifts']
    
    return args, params

if __name__ == '__main__':
    args, params = get_input()

    pixel_shifts = params["pixel_shifts"]
    remove_direction = int(params["direction"])

    new_pixel_shifts = pixel_shifts
    new_pixel_shifts[remove_direction,:,:] = np.zeros_like(new_pixel_shifts[remove_direction,:,:])

    out = {'pixel_shifts' : new_pixel_shifts}
    cmdline_config_cxi_reader.write_all(params, args.filename, out, apply_roi=False)
    print('display: '+params['h5_group']+'/pixel_shifts') ; sys.stdout.flush()
