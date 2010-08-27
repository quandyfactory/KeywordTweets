#!/usr/bin/env python

__title__ = 'KeywordTweets, a simple script (with versions written in Python and Javascript) that returns recent tweets with a given keyword.'
__version__ = 0.1
__author__ = "Ryan McGreal ryan@quandyfactory.com"
__homepage__ = "http://quandyfactory.com/projects/71/keywordtweets"
__copyright__ = "(C) 2009 by Ryan McGreal. Licenced under GNU GPL 2.0\nhttp://www.gnu.org/licenses/old-licenses/gpl-2.0.html"

"""
KeywordTweets is a simple script (with versions written in Python and Javascript) that returns recent tweets with a given keyword.
"""

import json
import urllib

def get_tweets(keyword):

    url = 'http://search.twitter.com/search.json?q='

    page = urllib.urlopen('%s%s' % (url, keyword))
    blob = page.read()
    jsonblob = json.loads(blob)
    results = jsonblob['results']

    output = []
    addline = output.append

    addline('<div class="tweet_container">')
    addline('<h3>Recent #%s Tweets</h3>' % (keyword))

    for result in results:
        addline('<div class="tweet">')
        addline('  <div class="tweetphoto">')
        addline('    <a href="http://twitter.com/%s">' % (result['from_user']))
        addline('      <img src="%s" alt="%s" title="%s">' % (result['profile_image_url'], result['from_user'], result['from_user']))
        addline('    </a>')
        addline('  </div>')
        addline('  <div class="tweetstatus">')
        addline('    %s <em><a href="http://twitter.com/%s/status/%s">%s</a></em>' % (result['text'], result['from_user'], result['id'], result['created_at']))
        addline('  </div>')
        addline('</div>')

    return '\n'.join(output)


def make_page(keyword, html):
    """
    Takes the HTML generated by get_tweets() and puts it into a basic HTML page.
    """
    output = []
    addline = output.append

    addline('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">')
    addline('<html>')
    addline('<head>')
    addline('<title>Tweets for #%s</title>' % (keyword))
    addline('<style type="text/css">')
    addline('div.tweet_container { float: right; width: 400px; font-size: 0.8em; border: 2px solid darkblue; padding: 8px; height: 80%; overflow-y: scroll; }')
    addline('div.tweet_container h3 { margin: 0; padding: 0; text-align: center; color: darkblue; margin-bottom: 6px; padding-bottom: 6px; border-bottom: 2px solid darkblue; }')
    addline('div.tweet { clear: both; }')
    addline('div.tweetphoto { float:left; width: auto; margin: 0; padding: 0; }')
    addline('div.tweetphoto img { border: none; width: 48px; height: 48px; display: block; margin: 0; margin-bottom: 24px; margin-right: 8px; padding: 0; }')
    addline('div.tweetphoto a > img { border: 1px solid black; }')
    addline('</style>')
    addline('</head>')
    addline('<body>')

    addline(html)

    addline('</div>')
    addline('</body>')
    addline('</html>')
    return '\n'.join(output)
