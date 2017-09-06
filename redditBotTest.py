import praw
import config
import re

pattern = re.compile("([bB][\S]*)[\s]([cC][\S]*)")
done = []

def syllables(word):
	count = 0
	vowels = 'aeiouy'
	word = word.lower().strip(".:;?!")
	if word[0] in vowels:
	    count +=1
	for index in range(1,len(word)):
	    if word[index] in vowels and word[index-1] not in vowels:
	        count +=1
	if word.endswith('e'):
		count -= 1
	if word.endswith('le'):
		count+=1
	if count == 0:
		count +=1
	return count

def bot_login():
	r = praw.Reddit(username = config.username,
			password = config.password,
			client_id = config.client_id,
			client_secret = config.client_secret,
			user_agent = "capitaladequacy's cumberbot")

	return r
	
def run_bot(r):
	for comment in r.subreddit("test").comments(limit = 25):
		match = re.search(pattern, comment.body)
		if match and len(comment.body.split())<10 and comment.id not in done:
			if syllables(match.group(1)) > 1 and syllables(match.group(2)) > 1:
				print("String found")
				done.append(comment.id)
				comment.reply("isn't he that actor?")

r = bot_login()
run_bot(r)