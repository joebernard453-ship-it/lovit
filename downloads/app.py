from flask import Flask, render_template, request, redirect
import cloudinary
import cloudinary.uploader

app = Flask(__name__)

# CONNECTED TO CLOUDINARY
cloudinary.config( 
  cloud_name = "dxuc8p32q", 
  api_key = "949877422135464", 
  api_secret = "uO9ntlAKuSstV_m7jJb8-K506_Y" 
)

posts = [{"name": "System", "text": "Photo sharing is officially LIVE!", "image": None}]

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/post', methods=['POST'])
def add_post():
    username = request.form.get('username')
    content = request.form.get('content')
    image_file = request.files.get('image')
    
    img_url = None
    if image_file and image_file.filename != '':
        # This sends the file to Cloudinary so it stays forever
        upload_result = cloudinary.uploader.upload(image_file)
        img_url = upload_result.get('secure_url')

    if username and content:
        posts.append({"name": username, "text": content, "image": img_url})
    return redirect('/')

@app.route('/delete/<int:post_id>', methods=['POST'])
def delete_post(post_id):
    if 0 <= post_id < len(posts):
        posts.pop(len(posts) - 1 - post_id)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
