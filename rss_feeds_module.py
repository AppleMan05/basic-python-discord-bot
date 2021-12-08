def get_posts_details(rss=None):
    
    """
    Take link of rss feed as argument
    """
    if rss is not None:
        
          # import the library only when url for feed is passed
        import feedparser
          
        # parsing blog feed
        blog_feed = blog_feed = feedparser.parse(rss)
          
        # getting lists of blog entries via .entries
        posts = blog_feed.entries
          
        # dictionary for holding posts details
        posts_details = {"Blog title" : blog_feed.feed.title,
                        "Blog link" : blog_feed.feed.link}
          
        post_list = []
          
        # iterating over individual posts
        for post in posts:
            temp = dict()
              
            # if any post doesn't have information then throw error.
            try:
                temp["title"] = post.title
                temp["link"] = post.link
                temp["author"] = post.author
                temp["time_published"] = post.published
                temp["tags"] = [tag.term for tag in post.tags]
                temp["authors"] = [author.name for author in post.authors]
                temp["summary"] = post.summary
            except:
                pass
              
            post_list.append(temp)
          
        # storing lists of posts in the dictionary
        posts_details[0] = post_list 
          
        return posts_details # returning the details which is dictionary
    else:
        return None
        
