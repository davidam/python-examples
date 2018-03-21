#!/usr/bin/python# -*- coding: utf-8 -*-

import subprocess
cmd = '''
/bin/tar -cvzf /var/backups/backup-$(date "+%Y-%m-%d").tar.gz /var/www/drupal
cd /var/www/drupal; drush sql-dump > /var/backups/drupalxs-$(date "+%Y-%m-%d").sql
'''
subprocess.check_output(cmd, shell=True)
