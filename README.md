+- Quick Overview ----------------------------------------------------+
      To form our database, we must:
      - Pull the top N rated anime (only what we consider relevant)
      - Pull a large set of active users
      - Retrieve each user's anime list
      To recommend, we simply run our single recommender script
+---------------------------------------------------------------------+

1. If you are lazy and don't care about recent anime, "anime_list.csv" is provided and will work just fine. There may be problems with this script. I'll try to fix them soon. Anyway... 

Run scraper2.py, this produces a list of the top 10,000 (trust me this is PLENTY, beyond just some of the hundreds is utter garbage). It should be clear when this script is finished. You will have a .csv of the current top N anime.

2. Run pull_users.py, this gets you a list of people who are currently active on MAL, in short. Run this with caution, knowing that EVERY USER has a list of variable amount. IMPORTANT: Realize that this is the one script that may introduce bias to your recommender, as this is your actual dataset that matters. If you run it all night, you may be getting a database full of degenerates. Consider what time of day you run this script because it collects CURRENTLY ONLINE USERS' data.

3. Run pull_lists.py. This gets you a list of a user's <Anime,Rating> pairs for each user in your csv (ONLY PULLS FROM 'COMPLETED'). This script takes the longest to run, and as stated - grows in duration dependent on how long you run the last script.

4. Run recommend.py. Set os.path.expanduser() to the correct .csv you wish to use as your dataset.
	Run as such: 'python recommend.py <MAL_USERNAME>'
