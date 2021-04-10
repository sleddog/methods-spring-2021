# The 5Avoidr: A bot that only recognizes 25 out of the 26 letters of the alphabet as real characters

Welcome to my first Discord bot, inspired by [this subreddit!](https://www.reddit.com/r/AVoid5/) This bot started as a class assignment to create something with an API, and I wanted to explore Discord's Developer API. I might end up going further with it once I graduate. We'll see!

## Overview

The bot's actions are very simple. All he really does is take the `e`'s out of existing sentences, either by simply replacing them with a "-" or finding a synonym for the word and constructing new sentences without the letter "e" in them. 



## Using the Bot

### Installation

This bot isn't officially published, so there's no way for any users besides Arnold to add it to servers. However, if you would like to recreate the bot, follow [these instructions](https://www.freecodecamp.org/news/create-a-discord-bot-with-python/) to set up an environment and learn how Discord's Developer portal works. You can copy the code from this folder into your environment and once you finish the tutorial, it should work!

### Commands

The bot looks for any message starting with `&fg` to start firing commands. Here is a list of the commands that show up when `&fg aid` is invoked:

* `translation`: sub synonyms in for words that contain the unholy glyph.
*  `abolish`: pulls all fifth glyphs out of your words.
*  `count`: displays amount of unholy symbols this bot did away with.
*  `sin`: don't.
*  `origin`:display inspiration for this bot.

The trick for each of these commands is that it looks at the message immediately preceding the command! For example:

```
Arnold @ 3:52PM: Test!
Arnold @ 3:52PM: &fg abolish
5Avoidr @ 3:52PM: Abolishing any fifthglyphs from your words:
5Avoidr @ 3:52PM: T-st!
```



#### translation

#### abolish

#### count

#### sin

#### origin