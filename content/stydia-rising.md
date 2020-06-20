Title: Stydia Rising
Date: 2016-05-01
Modified: 2020-06-19
Lang: en
Category: Projects
Slug: projects/stydia-rising
Cover: images/articles/stydia-rising/Stydia Premiere hashtags limit 1.png
Tags: data analysis, python, sql, tableau, twitter
Summary: An analysis of Twitter reactions to the Teen Wolf S05E16 premiere.

# An Analysis of Twitter Reactions to the Teen Wolf S05E16 Premiere

This is my first data analysis project, completed in partial fulfillment of the requirements for the University of Michigan's Python Specialization program on Coursera.

The project is a spin-off of a Super Bowl 50 Twitter analysis that I came across while doing some research. I was particularly excited at the way they correlated the winning moment in the game to the spike in tweets that occurred at the same time. I wanted to adapt their project to my own domain: a favorite TV show of mine that had recently experienced a similar elation-inducing moment.

## Directory

Click the section you would like to jump to:

* [Description](#description)
* [Data](#data)
    * [Discovery](#discovery)
    * [Download](#download)
    * [Dissection](#dissection)
* [Discussion](#discussion)
    * [Debug](#debug)
    * [Directions](#directions)
    * [Disseminate](#disseminate)

## <a id="description"></a>Description

I analyzed 80,000+ tweets tagged #TeenWolf and 34,000+ tweets tagged #Stydia. "Stydia" is the blended couple name of Stiles and Lydia, two characters on the MTV drama Teen Wolf. Many fans of the show "ship" these two couples; short for "relationship," to "ship" someone means to hope that they will officially get together on the show.

In the "Lie Ability" (S05E16) episode of Teen Wolf, Stiles and Lydia share a moment together that could very well indicate them becoming an official couple at some time in the future. During the show, Stiles attempts to rescue Lydia, who encourages him to leave her since what he's trying to do is dangerous. Stiles tells Lydia to "please shut up and let [him] save [her] life." Fans refer to this kind of moment as the point when their ship "rises," i.e. gains legitimacy. Thus, this project is an analysis of the moment when "Stydia" started "rising."

I was curious to see how Twitter reacted during that moment on Teen Wolf. Would there be a spike in tweets similar to the moment when the Broncos won the Super Bowl? Here are a few other questions I wanted to answer:

* Can we classify a tweet as pro-Stydia or the reverse?
* Can we see an increase in tweets at the point where Stydia rises?
* What were the trending hashtags throughout the week?
* What hashtags were most frequently used along with #TeenWolf?
* Does the pattern of reaction repeat over several hours across the U.S. as the show airs in each respective timezone?
* What was the overall sentiment during the episode?

## <a id="data"></a>Data

### <a id="discovery"></a>Discovery

Before I started my project, I needed to **make sure that the data was even available** for collection. This is something that has slowed me down with previous projects. I started this project in March 2016, and the episode in question occurred at 9:00 PM EST on February 9, 2016.

I immediately his a roadblock. Twitter's API will only allow you to get tweets from no more than 7 days in the past. The tweets I wanted had occurred over a month before. At this point, **I was very tempted to give up.** I can't get the data, so I can't do the project, right?

Still, this was something I *really* wanted to look into, so I kept searching for a solution. Eventually I found one: [a Python project](https://github.com/Jefferson-Henrique/GetOldTweets-python/) that bypassed Twitter's API and used a browser search to pull past tweets.

Unfortunately, I hit a second roadblock when I realized that this program **wasn't doing exactly what I needed.** I wanted to cull tens of thousands of tweets, and it was taking me an unnecessarily long time to do it. I realized that his program was storing all of the tweets in a list and then retrieving them one by one; this was a terrible burden on my computer's memory that caused it to stall out more often than not.

I had to sit down and go the program to figure out where this was happening, and then I had to **figure out how to insert my own code** into it to get the program to do what I needed it to do.

Finally I was able to get the program to write the tweets out to an SQLite3 database in real time. In this way I culled 80,000+ tweets for the #TeenWolf hashtag over the course of 6 days, and 34,000+ tweets for the #Stydia hashtag over the same period of time.

### <a id="download"></a>Download

The coding portion of the project consisted of creating scripts to pull the tweets and write them to a database. Once I started the analysis, I create a few more scripts to help clean the data up and pull out the most important tweets.

Below is the code I added to the GetOldTweets program `TweetManager.py` file to write the tweets to a database:

```python
def getTweets(tweetCriteria):
  refreshCursor = ''
  # tweetDB = raw_input("Please enter database name: ")
  connect = sqlite3.connect("Stydia_Tweets.sqlite")
  cur = connect.cursor()
  count = 0

  while True:
    cur.execute('''
      INSERT OR IGNORE INTO Tweets (
        tweet_id, tweet_user, tweet_text, tweet_date, tweet_hash, tweet_RTs,
        tweet_faves, tweet_ment, tweet_loc, tweet_link
      ) VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )''', (
        tweet.id, tweet.username, tweet.text, tweet.date, tweet.hashtags,
        tweet.retweets, tweet.favorites, tweet.mentions, tweet.geo,
        tweet.permalink
      )
    )
    connect.commit()
    ...
```

I connected my script to the file, using it as a go-between from the program to the database.

My script is below:

```python
print "Project: Stydia Rising"
print "Object: Collect tweets."

import sys
# Appends the GetOldTweets manager so that I can import it
sys.path.append("C:\Users\jzp93\GetOldTweets-python-master")
import got
import sqlite3
import datetime

# tweetDB = raw_input("Please enter database name: ")
connect = sqlite3.connect("Stydia_Tweets.sqlite")
cur = connect.cursor()

# Creates the database
cur.executescript('''
  CREATE TABLE IF NOT EXISTS Tweets (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    tweet_id INTEGER,
    tweet_user TEXT,
    tweet_text TEXT,
    tweet_date TEXT,
    tweet_hash TEXT,
    tweet_RTs TEXT,
    tweet_faves TEXT,
    tweet_ment TEXT,
    tweet_loc TEXT,
    tweet_link TEXT);
  ''')

# Included time to track how long it took to collect data
print "Start: ", datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
print "Working..."

# User inputs which search term to query, i.e. "stydia" or "teenwolf"
query = raw_input("Please enter search term: ")

# From when to when? In my case, from 2016-02-08 until 2016-02-13.
start = raw_input("Please enter start date in YYYY-MM-DD format: ")
end = raw_input("Please enter end date in YYYY-MM-DD format: ")

# Taken straight from GOT documentation. Calls the got manager and creates
# a search query, much like you would do through Twitter's advanced search.
tweetCriteria = got.manager.TweetCriteria().setQuerySearch(
  query).setSince(start).setUntil(end)

# Used the following to check that the code was running. Commented it out for
# faster output.
tweet_info = got.manager.TweetManager.getTweets(tweetCriteria)
print tweet_info

print "Complete."
print "End: ", datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
```

The script produced a database of the following format:

<p align="center">
  <img src="/images/articles/stydia-rising/Tweets DB TeenWolf.png" alt="Tweets DB TeenWolf" width="100%">
  <p style="text-align:center;"><sup><em>Database containing tweets tagged or mentioning #teenwolf. 80,765 tweets collected from Feb. 8, 2016 to Feb. 13, 2016. All dates and times are Japan Standard Time. Note records 48,269 and 48,278 which refer to "Stydia rising."</em></sup>
  </p>
</p>

<p align="center">
  <img src="/images/articles/stydia-rising/Tweets DB Stydia.png" alt="Tweets DB Stydia" width="100%">
  <p style="text-align:center;"><sup><em>Database containing tweets tagged or mentioning #stydia. 34,348 tweets collected from Feb. 7, 2016 to Feb. 13, 2016. All dates and times are Japan Standard Time.</em></sup>
  </p>
</p>

### <a id="dissection"></a>Dissection

As I'm still currently taking machine learning courses, I'm not yet at the point where I feel comfortable performing sentiment analysis on the data. As such, those questions (whether a tweet is pro- or anti-Stydia, what the overall sentiment during the episode premiere was) will have to be saved for future research endeavors.

However, I was able to answer most of my original questions, as well as some other questions that I developed during the analysis.

Following in the footsteps of the [Super Bowl 50 Analysis](http://blog.aylien.com/post/140037240328/super-bowl-50-according-to-twitter-sentiment), I used Tableau to visualize my results.

#### Can we see an increase in tweets at the point where Stydia rises?

Undoubtedly, the answer is yes.

Below is a visualization of the tweet volume over time during the S05E16 premiere:

<p align="center">
  <img src="/images/articles/stydia-rising/Tweets During 5x16 Premiere.png" alt="Tweets During 5x16 Premiere" width="50%" height="" style="">
  <p style="text-align:center;"><sup><em></em></sup>
  </p>
</p>

There is an obvious spike in Twitter activity at around the 0:44 minute mark. This coincides with the exact scene during the premiere where Stiles says, "Lydia, please shut up and let me save your life." As Stydia fans in particular would react heavily to this scene, cross-referencing the #TeenWolf tweets with #Stydia tweets serve to bolster the argument that the Stydia scene is what everyone was reacting to. (A look at the database images above will show that this is indeed what fans were tweeting about at that moment.)

One of my original questions was whether or not this spike in reaction repeated itself throughout the week. Many shows will premiere at 9 PM in each subsequent time zone - meaning EST viewers will see the show before PST ones. However, this does not seem to be the case for <em>Teen Wolf</em>: of the 80,000 or so tweets pulling during the week, <strong>20,000 occurred during the hour of the 9 PM EST time slot alone</strong>, suggesting that the show airs at the same time across the US (indeed, a quick google search shows that <em>Teen Wolf</em> airs at 6 PM PST).

<p align="center">
  <img src="/images/articles/stydia-rising/TW week of.png" alt="Teen Wolf week of tweets" width="50%" height="" style="">
  <p style="text-align:center;"><sup><em>Spike in tweets during the S05E16 premiere only (9 PM EST~6 PM PST Feb. 9, corresponding 11 AM JST Feb. 10). Suggesting that S05E16 premiered in all time zones simultaneously.</em></sup>
  </p>
</p>

#### What were the most retweeted and liked tweets?

I used the following script to get the top 10 retweeted and liked tweets and write the links out to a text file:

```python
# -*- coding: UTF-8 -*-
import sqlite3

print "Starting."

# connect = sqlite3.connect("TeenWolf_Tweets.sqlite")
connect = sqlite3.connect("Stydia_Tweets.sqlite")
cur = connect.cursor()

cur.execute('''
  SELECT tweet_RTs, tweet_faves, tweet_ment, tweet_link FROM Tweets
  WHERE tweet_date BETWEEN "2016-02-10 11:00:00" AND "2016-02-10 11:59:59"
  ORDER BY cast(tweet_RTs as int) DESC LIMIT 10'''
  )

fhand = open('StydiaFaves.txt', 'w')

fhand.write("Top Ten Retweets:\n\r")

index = 1
for line in cur:
  fhand.write(str(index) + "\n")
  fhand.write("RTs: " + line[0] + "\n")
  fhand.write("Faves: " + line[1] + "\n")
  fhand.write("Mentions: " + line[2] + "\n")
  fhand.write("Link: " + line[3] + "\n\r")
  index = index + 1

cur.execute('''
  SELECT tweet_RTs, tweet_faves, tweet_ment, tweet_link FROM Tweets
  WHERE tweet_date BETWEEN "2016-02-10 11:00:00" AND "2016-02-10 11:59:59"
  ORDER BY cast(tweet_faves as int) DESC LIMIT 10'''
)

fhand.write("\n\rTop Ten Faves:\n\r")

index = 1
for line in cur:
  fhand.write(str(index) + "\n")
  fhand.write("RTs: " + line[0] + "\n")
  fhand.write("Faves: " + line[1] + "\n")
  fhand.write("Mentions: " + line[2] + "\n")
  fhand.write("Link: " + line[3] + "\n\r")
  index = index + 1

fhand.close()

print "Done."
```

I was a bit off with the newlines, but I could read the results, so I didn't change it.

Here are some of the results:

##### Top 5 #Stydia Tweets

<blockquote class="twitter-tweet">
<p dir="ltr" lang="en">Too many RT <a href="https://twitter.com/xxlaliter">@xxlaliter</a>: <a href="https://twitter.com/hollandroden">@hollandroden</a> FAVORITE STYDIA SCENE?!</p>
— holland roden (@hollandroden) <a href="https://twitter.com/hollandroden/status/697251993761386496">February 10, 2016</a></blockquote>
<blockquote class="twitter-tweet">
<p dir="ltr" lang="en">STYDIA HAS LITERALLY BEEN THERE SINCE THE BEGINNING AND IT AIN'T GOIN' ANYWHERE. <a href="https://twitter.com/hashtag/TEENWOLF?src=hash">#TEENWOLF</a></p>
— Tyler Hoechlin Army (@HoechlinArmy) <a href="https://twitter.com/HoechlinArmy/status/697250432708513792">February 10, 2016</a></blockquote>
<blockquote class="twitter-tweet">
<p dir="ltr" lang="en">Stiles asking Lydia to "wake up" is the new Ryan asking Marissa to "wake up" in Tijuana <a href="https://twitter.com/hashtag/TeenWolf?src=hash">#TeenWolf</a> <a href="https://twitter.com/hashtag/TheOC?src=hash">#TheOC</a> <a href="https://twitter.com/hashtag/Stydia?src=hash">#Stydia</a> <a href="https://t.co/K7xVxsKvW2">pic.twitter.com/K7xVxsKvW2</a></p>
— Samantha Highfill (@samhighfill) <a href="https://twitter.com/samhighfill/status/697252830021701632">February 10, 2016</a></blockquote>
<blockquote class="twitter-tweet">
<p dir="ltr" lang="en">Scott is the number one Stydia shipper <a href="https://twitter.com/hashtag/TeenWolf?src=hash">#TeenWolf</a></p>
— Becky | TW IS LIT (@xBreeTanner) <a href="https://twitter.com/xBreeTanner/status/697253454763286529">February 10, 2016</a></blockquote>
<blockquote class="twitter-tweet">
<p dir="ltr" lang="en">That Stydia scene had me like <a href="https://twitter.com/hashtag/TeenWolf?src=hash">#TeenWolf</a> <a href="https://t.co/dO4UYEM12p">pic.twitter.com/dO4UYEM12p</a></p>
— J (@dylanogposey) <a href="https://twitter.com/dylanogposey/status/697250893662650369">February 10, 2016</a></blockquote>

Those are the Stydia tweets. Now what about the ones that mention #TeenWolf...?

##### Top 5 #TeenWolf Tweets

<blockquote class="twitter-tweet">
<p dir="ltr" lang="en">"Please shut up and let me save your life." OMG HELP <a href="https://twitter.com/hashtag/TeenWolf?src=hash">#TeenWolf</a> <a href="https://t.co/YIRU9ztQk5">https://t.co/YIRU9ztQk5</a></p>
— TEEN WOLF (@MTVteenwolf) <a href="https://twitter.com/MTVteenwolf/status/697249631022006272">February 10, 2016</a></blockquote>
<blockquote class="twitter-tweet">
<p dir="ltr" lang="en">"Stiles saved me." THE TEARS WON'T STOP <a href="https://twitter.com/hashtag/TeenWolf?src=hash">#TeenWolf</a> <a href="https://t.co/DT22msCIH1">pic.twitter.com/DT22msCIH1</a></p>
— TEEN WOLF (@MTVteenwolf) <a href="https://twitter.com/MTVteenwolf/status/697253292980768771">February 10, 2016</a></blockquote>
<blockquote class="twitter-tweet">
<p dir="ltr" lang="en">YALL I AM AN EMOTIONAL MESS AND NO, IM NOT OKAY <a href="https://twitter.com/hashtag/TeenWolf?src=hash">#TeenWolf</a></p>
— TEEN WOLF (@MTVteenwolf) <a href="https://twitter.com/MTVteenwolf/status/697252749323407360">February 10, 2016</a></blockquote>
<blockquote class="twitter-tweet">
<p dir="ltr" lang="en">STOP IM CRYING WTF <a href="https://twitter.com/hashtag/TeenWolf?src=hash">#TeenWolf</a></p>
— TEEN WOLF (@MTVteenwolf) <a href="https://twitter.com/MTVteenwolf/status/697252958061404164">February 10, 2016</a></blockquote>
<blockquote class="twitter-tweet">
<p dir="ltr" lang="ht">LOLOLOL LIAM <a href="https://twitter.com/hashtag/TeenWolf?src=hash">#TeenWolf</a> <a href="https://t.co/1CuShuC7s6">pic.twitter.com/1CuShuC7s6</a></p>
— TEEN WOLF (@MTVteenwolf) <a href="https://twitter.com/MTVteenwolf/status/697245304186339328">February 10, 2016</a></blockquote>

Stydia for the win! 4 out of 5 of the most liked and retweeted tweets tagged #TeenWolf are in reference to Stydia. The most popular tweet even explicitly mentions Stiles' line, "Lydia, please shut up and let me save your life."

The most popular #TeenWolf tweets are also those tweeted by the official show Twitter, @MTVteenwolf. This makes sense, as many die-hard fans would love a chance to interact with show officials, even if it's something as simple as retweeting. In addition, many fans appreciate show officials tweeting their reactions to the show as well. In fact, the show creator as well as several of the actors frequently interact with their fans on Twitter, so it should come as no surprise that the most liked tweets come from the official MTV account.

#### What were the most popular hashtags during the premiere?

In addition to the most popular tweets, I was interested in the most popular hashtags used throughout the week. When first scrolling through the data, I noticed many hashtags (like #webelieveinstydia and #StydiaIsRising) that I hadn't expected.

The script I used to count the hashtags can be found below:

```python
# -*- coding: UTF-8 -*-
import sqlite3

print "Starting."

connect = sqlite3.connect("TeenWolf_Tweets.sqlite")
# connect = sqlite3.connect("Stydia_Tweets.sqlite")
cur = connect.cursor()

connect2 = sqlite3.connect("TW_Hashtags_PREMIERE.sqlite")
# connect2 = sqlite3.connect("Stydia_Hashtags_PREMIERE.sqlite")
cur2 = connect2.cursor()

cur2.execute('''DROP TABLE IF EXISTS Hashtags ''')

cur2.executescript('''
  CREATE TABLE IF NOT EXISTS Hashtags (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    hashtag TEXT,
    num_users INTEGER);''')

cur.execute('''
  SELECT tweet_hash FROM TeenWolf_Tweets WHERE tweet_date
  BETWEEN "2016-02-10 11:00:00" AND "2016-02-10 11:59:59"''')

hashtags = dict()

def get_hashtags(item):
  # Split the first index of the list (the hashtags) on the (#) symbol
  item = item[0].split('#')
  for tag in item:
    # Ignore empty values
    if len(tag) > 0:
      # Consolidates TeenWolf, teenwolf, TEENWOLF all as one hashtag
      tag = tag.lower().strip()
      try:
        # Add the hashtag to the dictionary
        hashtags[tag] = hashtags[tag] + 1
      except:
        hashtags[tag] = 1

# item is a list of values from the database; in this case, hashtags
for item in cur:
  # ignore entries with no hashtags
  if len(item[0]) &amp;amp;amp;gt; 0:
    get_hashtags(item)

for item in hashtags:
  cur2.execute('''
  INSERT OR IGNORE INTO Hashtags (hashtag, num_users) VALUES (?, ?)''',
  (item, hashtags[item]))
  connect2.commit()

connect2.commit()
print "Done."
```

I wrote the output to a database and imported it into Tableau in order to create a word cloud to visualize the frequencies.

**Most Frequently Used Hashtags Along with #TeenWolf During the S05E16 Premiere**

<p align="center">
  <img src="/images/articles/stydia-rising/TW Premiere hashtags limit 2.png" alt="TW Premiere hashtags" width="100%" height="" style="">
  <p style="text-align:center;"><sup><em>Showing hashtags used along with #TeenWolf during the hour of the S05E16 premiere. Hashtags with at least 2 counts are included.</em></sup>
  </p>
</p>

**Most Frequently Used Hashtags Along with #Stydia During the S05E16 Premiere**

<p align="center">
  <img src="/images/articles/stydia-rising/Stydia Premiere hashtags limit 1.png" alt="Stydia Premiere hashtags" width="100%" height="" style="">
  <p style="text-align:center;"><sup><em>Showing hashtags used along with #Stydia during the hour of the S05E16 premiere. Hashtags with at least 1 count are included.</em></sup>
  </p>
</p>

One of my original questions was to see what the trending hashtags were throughout the week. The visualizations for these are below.

**Most Frequently Used Hashtags Along with #TeenWolf (Feb. 8 - Feb. 13 JST)**

<p align="center">
  <img src="/images/articles/stydia-rising/TW Week of Hashtags limit 10.png" alt="TW Week of Hashtags limit 10" width="100%" height="" style="">
  <p style="text-align:center;"><sup><em>Showing hashtags used along with #TeenWolf during the week of Feb. 8 to Feb. 13. Hashtags with at least 10 counts are included.</em></sup>
  </p>
</p>

**Most Frequently Used Hashtags Along with #Stydia (Feb. 7 - Feb. 13 JST)**

<p align="center">
  <img src="/images/articles/stydia-rising/Stydia Week of Hashtags limit 5.png" alt="Stydia Week of Hashtags limit 5" width="100%" height="" style="">
  <p style="text-align:center;"><sup><em>Showing hashtags used along with #Stydia during the week of Feb. 7 to Feb. 13. Hashtags with at least 5 counts are included.</em></sup>
  </p>
</p>

Hashtags during the premiere of course focused on what was going on in the show (i.e. #puppystyle, #EscapeFromEichen). There was also a live chat going on with Holland Roden, the actress who plays Lydia, so #askholland was trending during the show as well.

However, as we look towards the rest of the week other hashtags start to crop up - for example, #KCA and #TheShannara#Chronicles - as viewers reference <em>Teen Wolf</em> in relation to other shows they watch (as well as to the Kids Choice Awards, which at the time were coming up in a few weeks).

Furthermore, the all-week #TeenWolf and #Stydia clouds show two very interesting hashtags: #BancoDeSeries and #TeenWolfPoland, respectively. I found out through my analysis that not only was <em>Teen Wolf</em> popular in the States; it seemed to have a sizable following worldwide!

#### Where else in the world was S05E16 watched?

I took the tweets for which location data was available and output their counts to a database using a modified version of the `hashtags.py` script. I then visualized the results on a map in Tableau. Note that I could only plot tweets for which location data was available; less than 4% of all tweets. However, the visualization did show me that *Teen Wolf* is indeed an international phenomenon.

<p align="center">
  <img src="/images/articles/stydia-rising/5x16 Around the World.png" alt="Teen Wolf around the world" width="100%" height="" style="">
  <p style="text-align:center;"><sup><em></em></sup>
  </p>
</p>

## <a id="discussion"></a>Discussion

I managed to answer most of my pressing questions. I successfully visualized Twitter data for my favorite show during one of the most influential episodes for Stydia shippers. I was able to make a contribution to my fandom and I am very proud of myself for that. I also learned how to use a new tool (Tableau) with which I felt quite uncomfortable at first, but with more practice I quickly got the hang of it.

Overall I am very happy with this project and consider it a great success!

### <a id="debug"></a>Debug

1. **It took entirely too long to get the GOT program working.** I spent way more time than necessary trying to pull the tweets. The very first thing I should have done when using somebody else's program is go through and read the code to see what it does. GOT has very little documentation so this should have been even more pressing. Next time I'll be sure to keep this in mind.
2. **I did not calculate how much RAM I would need to run the program.** When I was first working with the GOT model I kept getting disk I/O errors and my laptop kept stalling out. Of course once I got the tweets to write out to a DB in real time this wasn't an issue, but I think it's important to learn how to calculate RAM and such for when I will need it in the future.
3. **The project needed more organization.** Of course at the beginning I could not imagine the number of tweets I would get; the scope of the project evaded me at that time. While I did have separate directories for the code, the data, the documentation and the output, I could have done a better job keeping in its place. I ended up with a lot of files in the end, and a consistent naming scheme, for example, could have saved me a lot of confusion. I also may have benefited from using version control this time around. That is something I look forward to working more with in future projects.
4. **The project needed clearer definition.** All I knew was that I wanted to get tweets and I wanted to look at them at one point in time. I didn't specify at the beginning how many tweets I wanted to collected, the date and time I wanted them to be from, and what exactly I wanted to do with them. I ended up collecting more data than I needed (which is not necessarily a bad thing), and writing extra scripts towards the end of the analysis to do things I hadn't thought of before. While this is to be expected, next time I look forward to created a solid project plan so that I can know more clearly what I want to do with my data before I get it.

### <a id="directions"></a>Directions

1. **Perform sentiment analysis on the dataset.** This is something that I got from the Super Bowl 50 analysis that I wanted to try for myself. What was the overall sentiment during the S05E16 episode? Did it change over time? Can we tell if a tweet is pro- or anti-Stydia? Fandom has interesting ways of representing positive sentiment (for example, the phrase "STYDIA VINES HURT SO MUCH" should actually be interpreted positively), so I wonder how current text analytics tools would work on fandom-derived data.
2. **Consolidate the scripts into a seamless program.** This wasn't something I set out to do, but I think it could be helpful. I know that lots of programs exist already to perform Twitter analysis, but I might like to challenge myself by creating a version of my own.
3. **Issue a pull request to the GOT model.** I found it very helpful to be able to write the tweets out to a database in real time instead of reading them all into memory. I know that there are others out there who may also need to pull tens of thousands of tweets that were written in the past. I hope to adapt my code to a general usage and issue a pull request to the GOT model on GitHub so that others can benefit from this as well.

### <a id="disseminate"></a>Disseminate

* [Aylien's Super Bowl 50 Analysis](http://blog.aylien.com/post/140037240328/super-bowl-50-according-to-twitter-sentiment)
* [Tableau Public Visualization Tool](https://public.tableau.com/s/)
* [My interactive "Stydia Rising" dashboard on Tableau](https://public.tableau.com/profile/jaya.z.powell)
* [The Python model I used to get old tweets](https://github.com/Jefferson-Henrique/GetOldTweets-python/)
