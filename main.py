from instapy import InstaPy


# amount_number = 500
# work on line 4

session = InstaPy(username="mr.percys_palace", password="")
session.login()
session.like_by_tags(["travel", "adventure", "travelblogger"], amount=5)
session.set_do_follow(True, percentage=75)
session.set_do_comment(True, percentage=75)
# session.set_do_like(enabled=True, percentage=100)
session.set_comments(["Nice photo!", "<3", "Beautiful :heart_eyes:", "Follow me back!"])
session.set_relationship_bounds(enabled=True, max_followers=5000, max_following=3000, min_followers=30, min_following=30)
# session.follow_user_followers(['travelawesome'], amount=amount_number, randomize=False, interact=True, sleep_delay=300)
session.set_quota_supervisor(enabled=True, peak_comments_daily=240, peak_comments_hourly=21)

session.end()




