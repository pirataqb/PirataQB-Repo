# -*- coding: utf-8 -*-

'''
    Genesis Add-on
    Copyright (C) 2015 lambda

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''


import re,urllib,json,time
from resources.lib.libraries import client
from resources.lib.libraries import captcha

def resolve(url):
    #try:

        if check(url) == False: return


        id = re.compile('//.+?/(?:embed|f)/([0-9a-zA-Z-_]+)').findall(url)[0]
        url = 'https://api.openload.io/1/file/dlticket?file=%s' % id
        result = client.request(url)
        result = json.loads(result)
        cap = result['result']['captcha_url']

        if not cap == None: cap = captcha.keyboard(cap)
        time.sleep(result['result']['wait_time'])

        url = 'https://api.openload.io/1/file/dl?file=%s&ticket=%s' % (id, result['result']['ticket'])

        if not cap == None:
            url += '&captcha_response=%s' % urllib.quote(cap)

        result = client.request(url)
        result = json.loads(result)

        bigOne = str(result).split('{')
        for i in range(len(bigOne)):
            smallerOne = bigOne[i].split(',')
            for u in range(len(smallerOne)):
                    niceOne = smallerOne[u].split(':')
                    for t in range(len(niceOne)):
                        if "u'https" in str(niceOne[t]):
                            Master = str(niceOne[t]).replace("u'","")+niceOne[t+1]

        #MasterUrl = urllib.unquote_plus(result["url"]).decode('utf-8')

        #print("This is?? : "+str(MasterUrl))

        url = result['result']['url'] + '?mime=true'

        return url
    #except:print("Something Went Wrong? Too mutch dopwnloads??")


def check(url):
    try:
        id = re.compile('//.+?/(?:embed|f)/([0-9a-zA-Z-_]+)').findall(url)[0]
        url = 'https://openload.co/embed/%s/' % id

        result = client.request(url)
        if result == None: return False
        if '>We are sorry!<' in result: return False
        return True
    except:
        return False


