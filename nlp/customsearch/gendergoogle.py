#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2014 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Simple command-line example for Custom Search.

Command-line application that does a search.
"""

__author__ = 'jcgregorio@google.com (Joe Gregorio)'

import pprint
import argparse
from googleapiclient.discovery import build

parser = argparse.ArgumentParser()
parser.add_argument('name', help="Name to be detected")
#parser.add_argument('--gender', help="Male, female")
args = parser.parse_args()


def main():
  # Build a service object for interacting with the API. Visit
  # the Google APIs Console <http://code.google.com/apis/console>
  # to get an API key for your own application.
  filekey = open("apikey.txt", "r+")
  content = filekey.readline().rstrip()

  service = build("customsearch", "v1",
                  developerKey=content)

  res1 = service.cse().list(
      q=args.name+'+male',
#      cx='013315504628135767172:d6shbtxu-uo',
      cx='012930223948444503025:jc1-uqxxhcs',
    ).execute()
  print("Google results of %s as male: %s" % (args.name, res1['searchInformation']['totalResults']))
  res2 = service.cse().list(
      q=args.name+'+female',
#      cx='013315504628135767172:d6shbtxu-uo',
      cx='012930223948444503025:jc1-uqxxhcs',
    ).execute()
  print("Google results of %s as female: %s" % (args.name, res2['searchInformation']['totalResults']))

if __name__ == '__main__':
  main()
