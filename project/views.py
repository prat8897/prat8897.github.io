from flask import render_template
from flask import request
from app import app, pages


@app.route('/')
def home():
    
    posts = [page for page in pages]
    return render_template('page.html', page=posts[0])

@app.route('/archive/')
def archive():
    
    posts = [page for page in pages if 'date' in page.meta]
    # Sort pages by date
    sorted_posts = sorted(posts, reverse=True,
        key=lambda page: page.meta['date'])
    return render_template('index.html', pages=sorted_posts)

@app.route('/comics/')
def comics():
    
    return render_template('comics.html', page=page)

@app.route('/about/')
def about():
    
    return render_template('about.html', page=page)

@app.route('/<path:path>/')
def page(path):
    
    # Path is the filename of a page, without the file extension
    # e.g. "first-post"
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)

@app.errorhandler(404)
def page_not_found(e):
    
    return render_template('404.html'), 404
