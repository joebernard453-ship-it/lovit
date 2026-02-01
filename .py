st.title("Welcome to Lovit")
choice = st.radio("Choose an option:", ["Create Post", "View Feed", "Exit"])

if choice == "Create Post":
    st.write("Post creation area")

3. Run it as a Web App
Instead of running it with python lovit.py, you must use the Streamlit command:
python -m streamlit run lovit.py
website_name = "Lovit"
feed = [] # This is a 'List' to store all your posts

print("Welcome to " + website_name)

# 1. Start a loop that keeps the website running
while True:
    print("\n1. Create Post")
    print("2. View Feed")
    print("3. Exit")
    
    action = input("Choose (1/2/3): ")

    if action == "1":
        name = input("Your Name: ")
        text = input("What's on your mind? ")
        # Save the post to our feed list
        feed.append(name + ": " + text)
        print("Post saved!")

    elif action == "2":
        print("\n--- " + website_name + " Feed ---")
        if not feed:
            print("The feed is empty. Post something first!")
        else:
            for post in feed:
                print("📱 " + post)
                print("❤️ 0 Likes") # New posts start at 0
        print("-----------------------")

    elif action == "3":
        print("Goodbye!")
        break # This stops the loop and exits the app
