from flask import Flask

app = Flask(__name__)


@app.route('/versi2')
def hello_world2():
    html = """
        <html>
            <h1>Welcome to our Librarys!</h1>
            {author_ul}
        </html>
    """
    authors = ["Naufal", "Paijo", "Parsiman", "Galih"]
    # build an <ul> with authors
    authors_list = "<ul>"
    authors_list += "\n".join([
        "<li>{author}</li>".format(author=author) for author in authors
    ])
    authors_list += "</ul>"
    print(authors_list)

    return html.format(author_ul=authors_list)
