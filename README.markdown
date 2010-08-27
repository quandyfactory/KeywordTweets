##KeywordTweets

KeywordTweets is a simple script (with versions written in Python and Javascript) that returns recent tweets with a given keyword.

###Author

* Author: Ryan McGreal
* Email: [ryan@quandyfactory.com](mailto:ryan@quandyfactory.com)
* Homepage: [http://quandyfactory.com/projects/71/keywordtweets](http://quandyfactory.com/projects/71/keywordtweets)
* Repository: [http://github.com/quandyfactory/keywordtweets](http://github.com/quandyfactory/keywordtweets)

###This Version

* Version: 0.1
* Release Date: 2010-08-26

###Revision History

####Version 0.1

* Release Date: 2010-08-26
* Changes:
    * First commit

##Using KeywordTweets

Save this file in your PATH. (Enable executing as a script if you're on *Nix.) Import it into your program, and call the get_tweets() method (default keyword is "HamOnt").

Example:

    import keywordtweets
    tweets = keywordtweets.get_tweets('apples')
    # generates an HTML div of recent tweets featuring the word 'apples'

    fullpage = keywordtweets.make_page(tweets)
    # generates a basic HTML page that includes your tweets div

That's is, really.
