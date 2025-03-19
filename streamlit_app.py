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
    st.title("🖥️ Beginner Coding Challenges: Step-by-Step Learning!")

    st.markdown("### 🚀 Watch this fun video to learn Python basics:")
    st.video("https://youtu.be/BX6_YBPr7Jw?si=Q81oeVDhKnctPA2A")
    st.markdown(
    """
    <style>
    iframe {
        width: 70% !important;
        height: auto !important;
    }
    """,
    unsafe_allow_html=True
)

    st.sidebar.title("🔍 Navigation")
    option = st.sidebar.radio("Go to:", ["Challenges", "CSE Dashboard"])
    st.markdown("""
    ### ✨ Now You're Ready!
    Select a coding challenge from the sidebar and start your coding journey.
    """)

    if option == "CSE Dashboard":
        view_responses()
    else:
        name = st.text_input("Enter Your Name:")
        st.markdown("""
        ## 🎯 Select Your Project to Start Learning:
        """)
        challenge = st.selectbox("Select a project:", ["Build a Simple Calculator", "Build a To-Do List App", "Guess the Number Game", "Siri Time - Design Thinking"])

        if challenge == "Build a Simple Calculator":
            st.subheader("🧮 Let's Build a Simple Calculator")
            st.markdown("""
            ### 🚀 Step-by-Step Guide:
            - **Step 1**: Ask the user to input two numbers (use `input()`)
            - **Step 2**: Ask the user which operation to perform (+, -, *, /).
            - Example:
            ```python
            num1 = float(input("Enter first number: "))
            ```
            3. Perform the calculation based on the chosen operation.
            4. Display the result clearly to the user.

            **Try coding this below! 👇**
            """)
            user_code = st.text_area("Enter your Python code here:", height=250)
            if st.button("Submit Calculator App Code"):
                save_response(name, challenge, user_code)
                st.success("✅ Your Calculator App code has been submitted!")

        elif challenge == "Build a To-Do List App":
            st.subheader("📋 Let's Build a To-Do List!")
            st.markdown("""
            ### 📌 Build your own Task List App:
            1. **Allow users to input tasks**.
            2. Store tasks in a list.
            - Example:
            ```python
            tasks = []
            tasks.append(input("Enter task: "))
            ```
            3. Display the tasks to users.
            4. Optionally let users mark tasks as completed or remove them.

            **Write your full Python code below:**
            """)

            user_code = st.text_area("Enter your Python code here:", height=250)
            if st.button("Submit To-Do List Code"):
                save_response(name, challenge, user_code)
                st.success("✅ Your To-Do List code has been submitted!")

        elif challenge == "Guess the Number Game":
            st.subheader("🎲 Build a Guess-the-Number Game")
            st.markdown("""
            ### Create an Interactive Guessing Game!
            1. Generate a random number between 1 and 100.
            - Example:
            ```python
            import random
            number = random.randint(1,100)
            ```
            2. Ask users to guess the number.
            3. Provide feedback: "Too high!", "Too low!", or "Correct!".
            4. Keep track of the number of attempts.

            **Give it a try below:**
            """)
            user_code = st.text_area("Enter your Python code here:", height=250)
            if st.button("Submit Guess Game Code"):
                save_response(name, challenge, user_code)
                st.success("✅ Your Guess Game code has been submitted!")

        elif challenge == "Siri Time - Design Thinking":
            st.subheader("🌍 Siri Time - Design Thinking")
            st.markdown("""
            ### Let's Solve Community Problems Together:
            1. Clearly describe the problem.
            2. Form a team and assign roles (leader, coder, designer, etc.).
            3. Plan your solution by outlining how you'd build an app.
            """)

            problem_statement = st.text_area("What's the community problem?")
            team_lead = st.text_input("Team Leader Name:")
            team_members = st.text_area("Team Members (comma-separated):")
            roles = st.text_area("Assign roles to each member:")

            if st.button("Submit Project Idea"):
                response = f"Problem: {problem_statement}\nLeader: {team_lead}\nMembers: {team_members}\nRoles: {roles}"
                save_response(name, challenge, response)
                st.success("✅ Your idea has been submitted! Start planning your coding solution now.")

if __name__ == "__main__":
    main()
