from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)
posts = [{"name": "System", "text": "Project Lovit is fixed!", "image": None}]

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/post', methods=['POST'])
def add_post():
    username = request.form.get('username')
    content = request.form.get('content')
    image = request.files.get('image')
    image_name = image.filename if image and image.filename != '' else None
    if username and content:
        posts.append({"name": username, "text": content, "image": image_name})
    return redirect('/')

@app.route('/delete/<int:post_id>', methods=['POST'])
def delete_post(post_id):
    if 0 <= post_id < len(posts):
        posts.pop(len(posts) - 1 - post_id)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
