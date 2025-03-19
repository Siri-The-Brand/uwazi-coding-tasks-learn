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
        ### Instructions:
        Write Python code to create a calculator that:
        - Takes two numbers as input.
        - Lets the user choose an operation (add, subtract, multiply, divide).
        - Displays the result.
        """)
        user_code = st.text_area("Enter your Python code here:", height=250)
        if st.button("Submit Calculator Code"):
            save_response(name, "Build a Simple Calculator", user_code)
            st.success("✅ Your calculator code has been submitted!")

    elif challenge == "Build a To-Do List App":
        st.subheader("📋 Build a To-Do List App")
        st.markdown("""
        ### Instructions:
        Write Python code for a to-do list app that:
        - Lets the user add new tasks.
        - Shows a list of all tasks.
        - Allows tasks to be marked as completed or removed.
        """)
        user_code = st.text_area("Enter your Python code here:", height=250)
        if st.button("Submit To-Do List Code"):
            save_response(name, "Build a To-Do List App", user_code)
            st.success("✅ Your to-do list code has been submitted!")

    elif challenge == "Guess the Number Game":
        st.subheader("🎲 Guess the Number Game")
        st.markdown("""
        ### Instructions:
        Write Python code for a game where:
        - The program selects a random number between 1 and 100.
        - The user tries to guess the number.
        - The program provides feedback (too high, too low, correct).
        """)
        user_code = st.text_area("Enter your Python code here:", height=250)
        if st.button("Submit Guess the Number Code"):
            save_response(name, "Guess the Number Game", user_code)
            st.success("✅ Your guess-the-number game code has been submitted!")

    elif challenge == "Siri Time - Design Thinking":
        st.subheader("🌍 Siri Time - Design Thinking")
        st.markdown("""
        ## Identify a Problem in Your Community
        - Clearly describe the problem.
        - Form a team and assign roles.
        - Plan to build an app using coding to solve this problem step-by-step.
        """)

        problem_statement = st.text_area("Describe the problem in your community:")
        team_lead = st.text_input("Enter Team Lead Name:")
        team_members = st.text_area("List your team members (comma-separated):")
        roles = st.text_area("Assign roles to team members:")

        if st.button("Save Project Idea"):
            response = f"Problem: {problem_statement}\nTeam Lead: {team_lead}\nMembers: {team_members}\nRoles: {roles}"
            save_response(name, "Siri Time - Design Thinking", response)
            st.success("✅ Your project idea has been saved! Now start coding your solution.")

if __name__ == "__main__":
    main()
