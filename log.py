#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime
import logging
import os

# Se crea el nombre del log y se inicializa el logger
ID=datetime.datetime.now().strftime('LOG_%Y%m%d-%Hh%Mm')
logname="/tmp/LOGS/"+ID+".log"
os.makedirs(os.path.dirname(logname), exist_ok=True)
logger = logging.getLogger(__name__)
handler = logging.FileHandler(logname)
formatter = logging.Formatter('%(asctime)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.error(' cannot be built... maybe source input url is bad...', exc_info=False)
