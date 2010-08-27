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

## Using KeywordTweets

Save this file in your PATH. (Enable executing as a script if you're on *Nix.)

### Basic Use

Import it into your script and call the `get_tweets()` method, passing in the keyword you want to search. This returns a JSON object with your results.

The `format_tweets()` method takes your keyword and the JSON object produced by `get_tweets()` and formats it in HTML.

You can also call the `make_page()` method, passing in the keyword and the HTML output from `format_tweets()`, to generate a simple HTML page.

Example:

    import keywordtweets
    keyword = 'apples' # really interested in apples

    tweets = keywordtweets.get_tweets(keyword)
    # returns a JSON object of tweets

    markup = keywordtweets.format_tweets(keyword, tweets)
    # generates an HTML div of recent tweets featuring the word 'apples'

    fullpage = keywordtweets.make_page(keyword, tweets)
    # generates a basic HTML page that includes your tweets div

You can see an example of the output from the `make_page()` method in the included `sample_py.html` file.

### Ajax

Javascript security prevents AJAX requests from connecting to a different server than the one serving the HTML page. You will need to create a URL on your web server that polls twitter, e.g. using the `get_tweets()` method, and delivers the resulting JSON object in the HTTP response to the client.

The included `sample_ajax.html` file includes a javascript function for jQuery that will make an Ajax request to your web server to download the JSON object and convert it to HTML.
