# copy pasta from
# https://realpython.com/blog/python/primer-on-jinja-templating/

from flask import Flask, render_template
app = Flask(__name__)

# this is what we'll have a story model as
class Story:
    def __init__(self, picture, article_link, headline, description):
        self.picture = picture
        self.article_link = article_link
        self.headline = headline
        self.description = description

@app.route("/")
def home():
    # fake "data" to display
    lorum_ipsum_str = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. "
    StoryA = Story("http://via.placeholder.com/350x250?text=image", "http://dailybruin.com/", "HEADLINE_A", lorum_ipsum_str)
    StoryB = Story("http://via.placeholder.com/350x250?text=image", "http://dailybruin.com/", "HEADLINE_B", lorum_ipsum_str)
    StoryC = Story("http://via.placeholder.com/350x250?text=image", "http://dailybruin.com/", "HEADLINE_C", lorum_ipsum_str)
    StoryD = Story("http://via.placeholder.com/350x250?text=image", "http://dailybruin.com/", "HEADLINE_D", lorum_ipsum_str)
    weekend_roundup_data = [StoryA, StoryB, StoryC, StoryD]
    preview_data = [StoryA, StoryB, StoryC]

    template_data = {
        "weekend_roundup": weekend_roundup_data,
        "preview": preview_data
    }
    return render_template('index.html', **template_data)

if __name__ == '__main__':
    app.run(debug=True)