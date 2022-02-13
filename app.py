from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)

blog_post = [
    {
        "author": "Sheyzi",
        "title": "Post 1",
        "content": "Navbar navigation links build on our .nav options with their own modifier class and require the use of toggler classes for proper responsive styling. Navigation in navbars will also grow to occupy as much horizontal space as possible to keep your navbar contents securely aligned.",
        "date": "29th of April, 2021"
    },
    {
        "author": "Samuel",
        "title": "Post 2",
        "content": "Navbar navigation links build on our .nav options with their own modifier class and require the use of toggler classes for proper responsive styling. Navigation in navbars will also grow to occupy as much horizontal space as possible to keep your navbar contents securely aligned.",
        "date": "29th of April, 2021"
    },
    {
        "author": "Victoria",
        "title": "Post 3",
        "content": "Navbar navigation links build on our .nav options with their own modifier class and require the use of toggler classes for proper responsive styling. Navigation in navbars will also grow to occupy as much horizontal space as possible to keep your navbar contents securely aligned.",
        "date": "29th of April, 2021"
    },
    {
        "author": "Prosper",
        "title": "Post 4",
        "content": "Navbar navigation links build on our .nav options with their own modifier class and require the use of toggler classes for proper responsive styling. Navigation in navbars will also grow to occupy as much horizontal space as possible to keep your navbar contents securely aligned.",
        "date": "30th of April, 2021"
    },
]


@app.route('/')
def home():
    return render_template('home.html', posts=blog_post)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/add-post', methods=['GET', 'POST'])
def add_post():
    if request.method == "POST":
        title = request.form['title']
        author = request.form['author']
        content = request.form['content']

        new_post = {
            "title": title,
            "author": author,
            "content": content,
            "date": datetime.today()
        }

        blog_post.append(new_post)
        return redirect('/')

    return render_template('add-post.html')


if __name__ == "__main__":
    app.run(debug=True)
