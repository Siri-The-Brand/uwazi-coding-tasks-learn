import streamlit as st
import pandas as pd
import random
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
    1. **Simple Calculator** 🧮
    2. **Guess the Number Game** 🎲
    3. **To-Do List App** 📋
    4. **Siri Time - Design Thinking** 🌍
    """)
    
    name = st.text_input("Enter Your Name:")
    challenge = st.selectbox("Select a challenge to work on:", ["Simple Calculator", "Guess the Number Game", "To-Do List App", "Siri Time - Design Thinking"])
    
    if challenge == "Simple Calculator":
        st.subheader("🧮 Simple Calculator")
        num1 = st.number_input("Enter the first number:", step=1.0)
        num2 = st.number_input("Enter the second number:", step=1.0)
        operation = st.selectbox("Choose an operation:", ["+", "-", "*", "/"])
        if st.button("Calculate"):
            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                result = num1 / num2 if num2 != 0 else "Error! Division by zero."
            st.success(f"✅ The result of {num1} {operation} {num2} is: {result}")
            save_response(name, "Simple Calculator", f"{num1} {operation} {num2} = {result}")
    
    elif challenge == "Guess the Number Game":
        st.subheader("🎲 Guess the Number Game")
        target_number = random.randint(1, 100)
        user_guess = st.number_input("Guess a number between 1 and 100:", min_value=1, max_value=100, step=1)
        if st.button("Check Guess"):
            if user_guess < target_number:
                st.warning("Too low! Try again.")
            elif user_guess > target_number:
                st.warning("Too high! Try again.")
            else:
                st.success("🎉 Congratulations! You guessed the correct number!")
            save_response(name, "Guess the Number Game", f"Guessed {user_guess}")
    
    elif challenge == "To-Do List App":
        st.subheader("📋 To-Do List App")
        task = st.text_input("Enter a new task:")
        if 'tasks' not in st.session_state:
            st.session_state.tasks = []
        if st.button("Add Task"):
            if task:
                st.session_state.tasks.append(task)
                save_response(name, "To-Do List App", task)
        st.write("### Your Tasks:")
        for t in st.session_state.tasks:
            st.write(f"- {t}")
    
    elif challenge == "Siri Time - Design Thinking":
        st.subheader("🌍 Siri Time - Design Thinking")
        st.markdown("""
        ## Identify a Problem in Your Community
        - Write down the problem you want to solve.
        - Form a team and assign roles.
        - Use coding to build a solution step by step!
        """)
        
        problem_statement = st.text_area("Describe the problem in your community:")
        team_lead = st.text_input("Enter Team Lead Name:")
        team_members = st.text_area("List your team members (comma-separated):")
        roles = st.text_area("Assign roles to team members:")
        
        if st.button("Save Idea"):
            response = f"Problem: {problem_statement}\nTeam Lead: {team_lead}\nMembers: {team_members}\nRoles: {roles}"
            save_response(name, "Siri Time - Design Thinking", response)
            st.success("✅ Your project idea has been saved! Start learning to code to build your solution.")
        
if __name__ == "__main__":
    main()
