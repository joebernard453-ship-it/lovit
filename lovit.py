import streamlit as st
from PIL import Image

# 1. Page Configuration
st.set_page_config(page_title="Lovit Social", page_icon="❤️", layout="centered")
st.title("Lovit Social ❤️")

# 2. Database (Storage)
if 'posts' not in st.session_state:
    st.session_state.posts = []

# 3. Sidebar: Create New Post
with st.sidebar:
    st.header("➕ New Post")
    user = st.text_input("Your Username")
    caption = st.text_area("What's on your mind?")
    photo = st.file_uploader("Upload Photo", type=['jpg', 'png', 'jpeg'])
    
    if st.button("Post to Lovit"):
        if user and (caption or photo):
            # Create the post dictionary
            new_post = {
                "user": user,
                "text": caption,
                "image": photo,
                "likes": 0,
                "comments": []
            }
            st.session_state.posts.insert(0, new_post)
            st.success("Shared to Global Feed!")

# 4. Search Bar
search = st.text_input("🔍 Search feed...", placeholder="Search names or captions")

# 5. Global Feed Logic
st.header("Global Feed")

# Filter posts based on search
filtered = [p for p in st.session_state.posts if search.lower() in p['user'].lower() or search.lower() in p['text'].lower()]

if not filtered:
    st.info("No posts found.")
else:
    for i, p in enumerate(filtered):
        with st.container(border=True):
            st.subheader(f"👤 {p['user']}")
            if p['text']: st.write(p['text'])
            if p['image']: st.image(p['image'], use_container_width=True)
            
            # Interaction Row: Likes and Delete
            col1, col2 = st.columns([1, 1])
            if col1.button(f"❤️ {p['likes']} Likes", key=f"like_{i}"):
                p['likes'] += 1
                st.rerun()
            
            if col2.button("🗑️ Delete Post", key=f"del_{i}"):
                st.session_state.posts.pop(i)
                st.rerun()

            # Comment Section
            st.divider()
            for comment in p['comments']:
                st.caption(f"💬 {comment}")
            
            # Add new comment
            c_input = st.text_input("Write a comment...", key=f"c_in_{i}")
            if st.button("Reply", key=f"c_btn_{i}"):
                if c_input:
                    p['comments'].append(c_input)
                    st.rerun()
