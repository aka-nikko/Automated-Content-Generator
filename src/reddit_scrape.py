import praw
import random
from dotenv import load_dotenv
import os
from config import subred, ignore


def reddit_scrape():
    try:
        print("\nGetting AskReddit Posts...")
        content = {}

        #Secrets Are Saved in .env File
        load_dotenv()
        reddit = praw.Reddit(
            client_id=os.getenv("REDDIT_CLIENT_ID"),
            client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
            user_agent="Accessing AskReddit threads",
            username=os.getenv("REDDIT_USERNAME"),
            password=os.getenv("REDDIT_PASSWORD"),
        )

        #Set Subreddit as "askreddit" And Scrape Top 50 Posts
        askreddit = reddit.subreddit(subred)
        threads = askreddit.hot(limit=50)
        
        #Select One Random Post From The 50
        submission = list(threads)[random.randrange(0, 50)]
        print(f"Video Will Be: {submission.title}")

        #Clean Title of Any Special Character and New Lines
        cleaned_text = ""
        for char in submission.title:
            if char.isalnum() or char.isspace():
                cleaned_text += char
        cleaned_text = cleaned_text.replace('\n', ' ')

        #Make A Record So We Don't Create Same Video Again
        with open("assets/record.txt", "r") as f:
            lines = f.read().splitlines()
        if cleaned_text in lines:
            print("This Post Is Already Done")
        else:
            with open('assets/record.txt', 'a') as f:
                f.write("\n"+cleaned_text)

            #Save Post Data
            try:
                content["thread_url"] = submission.url
                content["thread_title"] = submission.title
                content["comments"] = []
                for top_level_comment in submission.comments:
                    if len(top_level_comment.body)>10 and len(top_level_comment.body)<250:
                        if not any(ele in top_level_comment.body for ele in ignore):
                            content["comments"].append(
                                {
                                    "comment_body": top_level_comment.body,
                                    "comment_url": top_level_comment.permalink,
                                    "comment_id": top_level_comment.id,
                                }
                            )

            except AttributeError as e:
                pass

            return content, cleaned_text
    
    except Exception as e:
        raise e