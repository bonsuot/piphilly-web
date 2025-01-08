from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about/history.html')


@app.route('/beliefs')
def beliefs():
    return render_template('about/beliefs.html')


@app.route('/mission-vision')
def mission_vision():
    return render_template('about/mission-vision.html')


@app.route('/core-values')
def core_values():
    return render_template('about/core-values.html')


@app.route('/leadership')
def leadership():
    return render_template('about/leadership.html')


@app.route('/history')
def history():
    return render_template('about/history.html')


@app.route('/ministries/mens_ministry')
def mens_ministry():
    return render_template('ministries/mens_ministry.html')


@app.route('/ministries/womens_ministry')
def womens_ministry():
    return render_template('ministries/womens_ministry.html')


@app.route('/ministries/youth_and_pensa')
def youth_and_pensa():
    return render_template('ministries/youth_and_pensa.html')


@app.route('/ministries/childrens_ministry')
def childrens_ministry():
    return render_template('ministries/childrens_ministry.html')


@app.route('/ministries/evangelism')
def evangelism():
    return render_template('ministries/evangelism.html')


@app.route('/ministries/food_pantry')
def food_pantry():
    return render_template('ministries/food_pantry.html')


# New route for events
@app.route('/events')
def events():
    return render_template('events/events.html')


@app.route('/services')
def services():
    return render_template('services/services.html')


@app.route('/contact')
def contact():
    return render_template('contact/contact.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
