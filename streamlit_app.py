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

def view_responses():
    if os.path.exists(data_file):
        df = pd.read_csv(data_file)
        st.subheader("📊 Learner Responses Dashboard")
        st.dataframe(df)
    else:
        st.warning("No responses recorded yet.")

def main():
    st.set_page_config(page_title="Fun Coding Challenges", page_icon="🔢", layout="centered")
    st.title("🖥️ Beginner Coding Challenges: Learn by Building!")

    st.sidebar.title("🔍 Navigation")
    option = st.sidebar.radio("Go to:", ["Challenges", "CSE Dashboard"])

    if option == "📊 Dashboard":
        view_responses()
    else:
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
            2. **Choose Operation**: Ask the user to pick an operation (+, -, *, /).
            3. **Calculate and Show Result**.
            """)
            user_code = st.text_area("Enter your Python code here:", height=250)
            if st.button("Submit Calculator Code"):
                save_response(name, "Build a Simple Calculator", user_code)
                st.success("✅ Your calculator code has been submitted!")

        elif challenge == "Build a To-Do List App":
            st.subheader("📋 Build a To-Do List App")
            st.markdown("""
            Let's build an app to manage your daily tasks!
            1. Let users add tasks.
            2. Display tasks.
            3. Allow removing tasks.
            """)
            user_code = st.text_area("Enter your Python code here:", height=250)
            if st.button("Submit To-Do List Code"):
                save_response(name, "Build a To-Do List App", user_code)
                st.success("✅ Your to-do list code has been submitted!")

        elif challenge == "Guess the Number Game":
            st.subheader("🎲 Guess the Number Game")
            st.markdown("""
            Let's create a fun guessing game!
            1. Computer picks a random number between 1-100.
            2. User guesses the number.
            3. Provide feedback (Too high, too low, correct).
            """)
            user_code = st.text_area("Enter your Python code here:", height=250)
            if st.button("Submit Guess Game Code"):
                save_response(name, "Guess the Number Game", user_code)
                st.success("✅ Your game code has been submitted!")

        elif challenge == "Siri Time - Design Thinking":
            st.subheader("🌍 Siri Time - Design Thinking")
            problem_statement = st.text_area("Describe the community problem:")
            team_lead = st.text_input("Team Leader Name:")
            team_members = st.text_area("Team Members (comma-separated):")
            roles = st.text_area("Assign team roles:")
            if st.button("Save Project Idea"):
                response = f"Problem: {problem_statement}\nLead: {team_lead}\nMembers: {team_members}\nRoles: {roles}"
                save_response(name, "Siri Time - Design Thinking", response)
                st.success("✅ Your idea is saved!")

if __name__ == "__main__":
    main()
