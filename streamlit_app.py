import streamlit as st
import pandas as pd
import os

data_file = "user_responses.csv"

def save_response(name, challenge, response):
    if not os.path.exists(data_file):
        df = pd.DataFrame(columns=["Name", "Challenge", "Response"])
    else:
        df = pd.read_csv(data_file)
    new_data = pd.DataFrame([{"Name": name, "Challenge": challenge, "Response": response}])
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv(data_file, index=False)

def main():
    st.set_page_config(page_title="Fun Coding Challenges", page_icon="🔢", layout="centered")
    st.title("🖥️ Beginner Coding Challenges: Learn by Building!")

    st.markdown("""
    ## 🎯 Choose a Coding Challenge Below:
    1. **Build a Simple Calculator** 🧮
    2. **Build a To-Do List App** 📋
    3. **Guess the Number Game** 🎲
    4. **Siri Time - Design Thinking** 🌍
    """)

    name = st.text_input("Enter Your Name:")
    challenge = st.selectbox("Select a challenge to work on:", ["Build a Simple Calculator", "Build a To-Do List App", "Guess the Number Game", "Siri Time - Design Thinking"])

    if challenge == "Build a Simple Calculator":
        st.subheader("🧮 Build a Simple Calculator")
        st.markdown("""
        ### 🛠️ Let's Build a Calculator!
        Imagine you're building a simple calculator app. Follow these steps:
        1. **Get Inputs**: Ask the user for two numbers.
        2. **Choose Operation**: Ask the user which operation (+, -, *, /) they want to perform.
        3. **Calculate & Display**: Perform the calculation and show the result.
        
        💡 *Tip*: Use Python `input()` function to get user inputs.
        """)
        user_code = st.text_area("Enter your Python code here:", height=250)
        if st.button("Submit Calculator Code"):
            save_response(name, "Build a Simple Calculator", user_code)
            st.success("✅ Your calculator code has been submitted!")

    elif challenge == "Build a To-Do List App":
        st.subheader("📋 Build a To-Do List App")
        st.markdown("""
        Let's build a cool To-Do list app together!
        1. **Add Tasks**: Let the user type tasks.
        2. **Show Tasks**: Display the list of tasks clearly.
        3. **Manage Tasks**: Allow the user to remove tasks when they're done.
        """)
        user_code = st.text_area("Enter your Python code here:", height=250)
        if st.button("Submit To-Do List Code"):
            save_response(name, "Build a To-Do List App", user_code)
            st.success("✅ Your To-Do List code has been submitted!")

    elif challenge == "Guess the Number Game":
        st.subheader("🎲 Guess the Number Game")
        st.markdown("""
        ### Let's create a fun game!
        - The computer picks a random number from 1 to 100.
        - The user tries to guess it.
        - The computer gives hints: too high, too low, or correct!
        """)
        user_code = st.text_area("Enter your Python code here:", height=250)
        if st.button("Submit Guess the Number Game Code"):
            save_response(name, "Guess the Number Game", user_code)
            st.success("✅ Your game code has been submitted!")

    elif challenge == "Siri Time - Design Thinking":
        st.subheader("🌍 Siri Time - Design Thinking")
        st.markdown("""
        ## Let's Solve a Real-World Problem!
        Follow these steps:
        1. Clearly describe a real problem in your community.
        2. Form a team and pick a leader.
        3. Assign roles and responsibilities.
        3. Plan an app idea to solve this problem.
        """)
        problem_statement = st.text_area("What's the problem in your community?")
        team_lead = st.text_input("Who's the Team Leader?")
        team_members = st.text_area("List your team members (comma-separated):")
        roles = st.text_area("Assign roles to each member:")

        if st.button("Save Project Idea"):
            response = f"Problem: {problem_statement}\nTeam Lead: {team_lead}\nMembers: {team_members}\nRoles: {roles}"
            save_response(name, "Siri Time - Design Thinking", response)
            st.success("✅ Your idea is saved! Let's start coding!")

if __name__ == "__main__":
    main()
