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
    args, params = cmdline_config_cxi_reader.get_all('remove_shifts',
                   'setting pixel shifts along one direction to zero')
    params = params['remove_shifts']
    
    return args, params

if __name__ == '__main__':
    args, params = get_input()
    cxinam=str(args["filename"])
    npynam=cxinam[:-4]+".npy"
    array = params["array"]
    save(npynam,array)
    print(".npy file has been saved to location of .cxi file")
    print('display: '+params['h5_group']+'/') ; sys.stdout.flush()
