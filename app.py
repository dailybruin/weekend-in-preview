# copy pasta from
# https://realpython.com/blog/python/primer-on-jinja-templating/

from flask import Flask, render_template
app = Flask(__name__)

# this is what we'll have a story model as
class Story:
    def __init__(self, picture, headline, description):
        self.picture = picture
        self.headline = headline
        self.description = description

@app.route("/")
def home():
    # fake "data" to display
    StoryA = Story("http://via.placeholder.com/350x250", "HEADLINE_A", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore")
    StoryB = Story("http://via.placeholder.com/350x250", "HEADLINE_B", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore")
    StoryC = Story("http://via.placeholder.com/350x250", "HEADLINE_C", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore")
    StoryD = Story("http://via.placeholder.com/350x250", "HEADLINE_D", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore")
    weekend_roundup_data = [StoryA, StoryB, StoryC, StoryD]

    template_data = {
        "weekend_roundup": weekend_roundup_data
    }
    return render_template('index.html', **template_data)

if __name__ == '__main__':
    app.run(debug=True)