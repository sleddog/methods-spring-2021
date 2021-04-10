import discord
import os
from nltk.corpus import wordnet
from keep_alive import keep_alive

#Code based on these two websites:
#https://www.geeksforgeeks.org/get-synonymsantonyms-nltk-wordnet-python/
#https://www.freecodecamp.org/news/create-a-discord-bot-with-python/
client = discord.Client()
second_to_last_message = "placholder"
count = 0
def abolish(words):
  global count
  if len(words) < 1:
    return ""
  else:
    letter = words[0]
    if letter == "e":
      count += 1
      return "-" + abolish(words[1:])
    else:
      return letter + abolish(words[1:])

def translate(sentence):
  global count
  translation = ""
  sentence = sentence.split(" ")
  bad_words = []
  for word in sentence:
    #punctuation removal from https://careerkarma.com/blog/python-remove-punctuation/
    word_no_punc = "".join(u for u in word if u not in ("?", ".", ";", ":", "!", ",", "-"))
    found = False
    if("e" in word_no_punc.lower()):
      for synonyms in wordnet.synsets(word_no_punc):
        if(found):
          break
        for syn in synonyms.lemmas():
          if "e" not in str(syn.name()).lower():
            found = True
            translation += str(syn.name()) + " "
            count += word_no_punc.count('e')
            break
      if(not found):
        translation += word + " "
        bad_words.append(word_no_punc)
    else:
      translation += word + " "
  if(len(bad_words) > 0):
    translation += "\n\n Big apology, my dictionary did not find any synonyms for:"
    for bad in bad_words:
      translation += "\n" + bad
  return translation

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    global second_to_last_message
    if message.author == client.user:
        return

    if message.content.startswith('&fg'):
      if('origin' in message.content):
        await message.channel.send("Inspiration for this bot is from this sub: https://www.reddit.com/r/AVoid5/")
      elif('translation' in message.content):
        await message.channel.send('Translating your unholy phrasing:')
        await message.channel.send(translate(second_to_last_message))
      elif('abolish' in message.content):
        await message.channel.send('Abolishing any fifthglyphs from your words:')
        await message.channel.send(abolish(second_to_last_message))
      elif('aid' in message.content):
        await message.channel.send('Commands in 5Avoidr v1.0:\nUse `&fg` to use my commands.\n\n`translation`: sub synonyms in for words that contain the unholy glyph.\n`abolish`: pulls all fifth glyphs out of your words.\n`count`: displays amount of unholy symbols this bot did away with.\n`sin`: don\'t.\n`origin`:display inspiration for this bot.\n\n Any commands will act upon words on display north of said command by a singular spot.')
      elif('sin' in message.content):
        await message.channel.send("https://tenor.com/view/enardo-logo-text-gif-14732944")
      elif('count' in  message.content):
        global count
        await message.channel.send("I did away with "+str(count) + " fifthglyphs so far.")
      else:
        await message.channel.send('Command not found. use `&fg aid` to look at my commands.')
      
    second_to_last_message = message.content

keep_alive()
client.run(os.getenv('TOKEN'))

