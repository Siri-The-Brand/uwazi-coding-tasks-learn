import streamlit as st

def main():
    st.set_page_config(page_title="Fun Coding Challenges", page_icon="🔢", layout="centered")
    st.title("🖥️ Beginner Coding Challenges: Learn by Building!")
    
    st.markdown("""
    ## 🎯 Choose a Coding Challenge Below:
    1. **Simple Calculator** 🧮
    2. **Guess the Number Game** 🎲
    3. **To-Do List App** 📋
    """)
    
    challenge = st.selectbox("Select a challenge to work on:", ["Simple Calculator", "Guess the Number Game", "To-Do List App"])
    
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
    
    elif challenge == "Guess the Number Game":
        import random
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
    
    elif challenge == "To-Do List App":
        st.subheader("📋 To-Do List App")
        task = st.text_input("Enter a new task:")
        if 'tasks' not in st.session_state:
            st.session_state.tasks = []
        if st.button("Add Task"):
            if task:
                st.session_state.tasks.append(task)
        st.write("### Your Tasks:")
        for t in st.session_state.tasks:
            st.write(f"- {t}")

if __name__ == "__main__":
    main()
