# The 5Avoidr: A bot that only recognizes 25 out of the 26 letters of the alphabet as real characters

Welcome to my first Discord bot, inspired by [this subreddit!](https://www.reddit.com/r/AVoid5/) This bot started as a class assignment to create something with an API, and I wanted to explore Discord's Developer API. I might end up going further with it once I graduate. We'll see!

## Overview

The bot's actions are very simple. All he really does is take the `e`'s out of existing sentences, either by simply replacing them with a "-" or finding a synonym for the word and constructing new sentences without the letter "e" in them. 

## Discord API 

The Discord API, a RESTful API, allows for users to create applications using Discord's Developer Portal. This can be anything really, but most people use it to create bots. Through its API, there's a module named `discord.py` you can install for Python via `pip` and it has classes such as `Bot` and `Client` that will allow you to use a bot's token and log in and program logic for it. To read more, [click here.](https://discord.com/developers/docs/reference)

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

When the `translation` command is called, the bot takes the message above the command and turns each word into a synonym if one exists that doesn't have an "e" in it. For every word it can't find a synonym for, it'll add it back into the message it'll send. After the message, there will be a list of words for which synonyms could not be found.

#### abolish

This command works by taking the message and replacing every "e" with a "-" as shown in the above example.

#### count

This returns the number of "e's" that the bot has taken out of sentences.

#### sin

This just returns a GIF with the letter E in it!

#### origin

This provides a link to the above subreddit. 

### Known Bugs

In order to make v1.0 work, I used a couple of global variables. As such, my instance of the bot doesn't actually look at the second to last message in a specific channel. Rather, it looks at the second to last message it reads from any channel in any server it's in! So there's a couple of privacy concerns there that I plan to work on. That, and it doesn't play well yet with emojis. 

Another bug is that the dictionary it looks at is from a library called `nltk` and the "wordnet" package it uses sometimes just doesn't install for some reason. As such, I have to go to the project's command line and run `import nltk` and `nltk.download('wordnet')` to install it.

Lastly, the bot can be ran and stopped, and the "e-count" resets whenever it's stopped.



## Future Plans

I want to give this bot the ability to construct complete sentences and use appropriate synonyms instead of just grabbing the first synonym it sees and replacing it in the sentence. That, and to **stop using globals** because I have never seen a better reason against using globals until this project. I also plan on cleaning up the code and using Discord's API more effectively.

Eventually, maybe I'll be able to publish this bot for widespread use! We'll see. Overall, I'm pleased with this project and I'm happy I decided to create it.