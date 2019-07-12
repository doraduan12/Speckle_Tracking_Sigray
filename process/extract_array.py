"""
"""

#! /usr/bin/env python
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from numpy import save
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
    args, params = cmdline_config_cxi_reader.get_all('extract_array',
                   'exporting an array')
    params = params['extract_array']
    print(args.filename)
    
    return args, params

if __name__ == '__main__':
    args, params = get_input()
    cxinam=str(args.filename)
    print("!!!!!!!!!!!!!!!!!!!!!!this is the cxinam",cxinam)
    npynam=cxinam[:-4]+".npy"
    array = params["array"]
    save(npynam,array)
    out = {'output' : array}
    cmdline_config_cxi_reader.write_all(params, args.filename, out, apply_roi=False)
    print(".npy file has been saved to location of .cxi file")
    print('display: '+params['h5_group']+'/output') ; sys.stdout.flush()
