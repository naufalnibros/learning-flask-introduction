from flask import Flask
from flask import render_template_string  # added

app = Flask(__name__)


@app.route('/versi3')
def hello_world3():
    library_name = "Poe"
    html = """
        <html>
            <h1>Welcome to {{library_name}} library!</h1>
        </html>
    """
    rendered_html = render_template_string(html, library_name=library_name)
    authors = ["Alan Poe", "Jorge L. Borges", "Mark Twain"]
    # Using an <ul> tag add the authors using the template engine
    return rendered_html
