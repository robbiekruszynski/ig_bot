from instapy import InstaPy

session = InstaPy(username="mr.percys_palace", password="")
session.login()
session.like_by_tags(["travel", "adventure", "europe", "jellycat"], amount=5)
session.set_do_follow(True, percentage=50)
session.set_do_comment(True, percentage=50)
session.set_comments(["Nice photo!", "<3", "Beautiful :heart_eyes:", "Follow me back!"])
session.set_relationship_bounds(enabled=True, max_followers=8500)

session.set_quota_supervisor(enabled=True, peak_comments_daily=240, peak_comments_hourly=21)

session.end()