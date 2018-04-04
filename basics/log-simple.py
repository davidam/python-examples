#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging, os
logging.basicConfig(filename='simple.log', level=logging.INFO)    
path = "/tmp/"
if (os.path.isdir(path)):
    print("Path is created")
    logging.info('Path is created')
