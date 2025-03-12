import streamlit as st
import random
import time

# Custom CSS for background image and font visibility
st.markdown(
    """
    <style>
    /* Set a background image */
    .stApp {
        background-image: url("https://i.pinimg.com/736x/34/32/22/343222b774334953928bcffdffa3f7c4.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;

    }
    /* Ensure all text is visible and readable */
    .stTitle, .stSubheader, .stMarkdown, .stRadio > div > label, .stButton > button {
        color: white !important;
    }
    
    /* Style the radio button options */
    .stRadio > div > label {
        font-size: 18px;
        padding: 10px;
    }
    /* Style the Submit button */
    .stButton > button {
        background-color: rgba(128, 128, 128, 0.8) !important;
        color: white !important;
        border: 1px solid white !important;
        font-size: 16px;
        padding: 10px 20px;
        border-radius: 5px;
    }
    /* Style success and error messages */
    .stSuccess, .stError {
        color: white !important;
        font-size: 18px;
        padding: 10px;
        border-radius: 5px;
    }
    .stSuccess {
        background-color: rgba(0, 128, 0, 0.8) !important;
    }
    .stError {
        background-color: rgba(255, 0, 0, 0.8) !important;
    }
    /* Style the sidebar */
    .stSidebar {
        background-image: url("https://img.freepik.com/premium-photo/close-up-palm-leaves-against-white-background_1048944-4691219.jpg?w=740");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    .stSidebar .stMarkdown h3 {
        color: white !important; /* Font color */
        background-color: rgba(0, 0, 0, 0.7); /* Semi-transparent background */
        padding: 10px; /* Add padding */
        border-radius: 10px; /* Rounded corners */
        text-align: center; /* Center-align text */
        border: 2px solid white; /* Add a border */
    }
    .stSidebar .stMarkdown {
        color: white !important; /* Font color for sidebar text */
        background-color: rgba(0, 0, 0, 0.7); /* Semi-transparent background */
        padding: 10px; /* Add padding */
        border-radius: 10px; /* Rounded corners */
        text-align: center; /* Center-align text */
        border: 2px solid white; /* Add a border */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title of the Quiz Application
st.title("📝 Quiz Application")

# Title of the programming language
st.title("📖 Python McQs")

# Define Quiz through Dictionary
questions = {
    1: {
        "question": "What is the output of `print(type([]))` in Python?",
        "options": ["A) <class 'list'>", "B) <class 'tuple'>", "C) <class 'dict'>", "D) <class 'set'>"],
        "answer": "A) <class 'list'>"
    },
    2: {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A) func", "B) define", "C) def", "D) function"],
        "answer": "C) def"
    },
    3: {
        "question": "What does the `len()` function do in Python?",
        "options": ["A) Returns the type of an object", "B) Returns the length of an object", "C) Converts a value to an integer", "D) Prints the object"],
        "answer": "B) Returns the length of an object"
    },
     4: {
        "question": "Which of the following is used to comment a single line in Python?",
        "options": ["A) //", "B) #", "C) /* */", "D) <!-- -->"],
        "answer": "B) #"
    },
    5: {
        "question": "What is the output of `print(2 ** 3)`?",
        "options": ["A) 6", "B) 8", "C) 9", "D) 23"],
        "answer": "B) 8"
    },
    6: {
        "question": "Which of the following is NOT a valid data type in Python?",
        "options": ["A) int", "B) float", "C) char", "D) str"],
        "answer": "C) char"
    },
    7: {
        "question": "What is the output of `print('Hello, World!'[7:12])`?",
        "options": ["A) World", "B) World!", "C) o, Wo", "D) Error"],
        "answer": "A) World"
    },
    8: {
        "question": "Which method is used to add an element to the end of a list?",
        "options": ["A) append()", "B) insert()", "C) add()", "D) extend()"],
        "answer": "A) append()"
    },
    9: {
        "question": "What is the output of `print(bool(0))`?",
        "options": ["A) True", "B) False", "C) 0", "D) None"],
        "answer": "B) False"
    },
    10: {
        "question": "Which module is used for working with regular expressions in Python?",
        "options": ["A) re", "B) regex", "C) pyregex", "D) string"],
        "answer": "A) re"
    },
    11: {
        "question": "What is the output of `print(10 / 3)`?",
        "options": ["A) 3", "B) 3.333", "C) 3.0", "D) 3.3333333333333335"],
        "answer": "D) 3.3333333333333335"
    },
    12: {
        "question": "Which of the following is used to open a file in Python?",
        "options": ["A) open()", "B) read()", "C) file()", "D) load()"],
        "answer": "A) open()"
    },
    13: {
        "question": "What is the output of `print('Python'.lower())`?",
        "options": ["A) PYTHON", "B) python", "C) Python", "D) Error"],
        "answer": "B) python"
    },
    14: {
        "question": "Which of the following is a mutable data type in Python?",
        "options": ["A) tuple", "B) str", "C) list", "D) int"],
        "answer": "C) list"
    },
    15: {
        "question": "What is the output of `print(3 * 'abc')`?",
        "options": ["A) abcabcabc", "B) abcabc", "C) abc3", "D) Error"],
        "answer": "A) abcabcabc"
    },
    16: {
        "question": "Which operator is used for exponentiation in Python?",
        "options": ["A) ^", "B) **", "C) //", "D) *"],
        "answer": "B) **"
    },
    17: {
        "question": "What is the output of `print(10 == '10')`?",
        "options": ["A) True", "B) False", "C) Error", "D) None"],
        "answer": "B) False"
    },
    18: {
        "question": "Which of the following is used to remove whitespace from the beginning and end of a string?",
        "options": ["A) trim()", "B) strip()", "C) remove()", "D) clean()"],
        "answer": "B) strip()"
    },
    19: {
        "question": "What is the output of `print(list(range(3)))`?",
        "options": ["A) [0, 1, 2]", "B) [1, 2, 3]", "C) [0, 1, 2, 3]", "D) [3]"],
        "answer": "A) [0, 1, 2]"
    },
    20: {
        "question": "Which of the following is used to handle exceptions in Python?",
        "options": ["A) try-except", "B) try-catch", "C) handle-except", "D) error-handle"],
        "answer": "A) try-except"
    }
    # Add the rest of your questions here...
}

# Convert dictionary values to a list
question_list = list(questions.values())

# Initialize session state variables
if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(question_list)
if "score" not in st.session_state:
    st.session_state.score = 0
if "answered_questions" not in st.session_state:
    st.session_state.answered_questions = set()
if "quiz_completed" not in st.session_state:
    st.session_state.quiz_completed = False

# Get Current Question
question = st.session_state.current_question

# Display the Question
if not st.session_state.quiz_completed:
    st.subheader(question["question"])

    # Create Radio Button
    selected_option = st.radio("Choose your answer", question["options"], key="answer")

    if st.button("Submit Answer"):
        if selected_option == question["answer"]:
            st.success("✅ Correct")
            st.session_state.score += 5  # Add 5 points for correct answer
        else:
            st.error(f"❌ Incorrect! The correct answer is {question['answer']}")
        
        # Mark the question as answered
        st.session_state.answered_questions.add(question["question"])
        
        # Check if all questions are answered
        if len(st.session_state.answered_questions) == len(question_list):
            st.balloons()
            st.success(f"🎉 Quiz Completed! Your total score is: {st.session_state.score}")
            st.session_state.quiz_completed = True  # Mark quiz as completed
        else:
            # Update the session state with a new random question
            remaining_questions = [q for q in question_list if q["question"] not in st.session_state.answered_questions]
            st.session_state.current_question = random.choice(remaining_questions)
            
            # Rerun the app to display the new question
            st.rerun()

# Display the current score
st.sidebar.markdown(f"### Your Current Score: {st.session_state.score}")

# Display a message in the sidebar if the quiz is completed
if st.session_state.quiz_completed:
    st.sidebar.markdown("### Thank you for completing the quiz! 🎉")






# import streamlit as st
# import random
# import time

# # Custom CSS for background image and font visibility
# st.markdown(
#     """
#     <style>
#     /* Set a background image */
#     .stApp {
#         background-image: url("https://images.unsplash.com/photo-1531685250784-7569952593d2?ixlib=rb-1.2.1&auto=format&fit=crop&w=1934&q=80");
#         background-size: cover;
#         background-position: center;
#         background-repeat: no-repeat;
#     }
#     /* Ensure all text is visible and readable */
#     .stTitle, .stSubheader, .stMarkdown, .stRadio > div > label, .stButton > button {
#         color: white !important;
#     }
#     /* Style the radio button options */
#     .stRadio > div > label {
#         font-size: 18px;
#         padding: 10px;
#     }
#     /* Style the Submit button */
#     .stButton > button {
#         background-color: rgba(128, 128, 128, 0.8) !important;
#         color: white !important;
#         border: 1px solid white !important;
#         font-size: 16px;
#         padding: 10px 20px;
#         border-radius: 5px;
#     }
#     /* Style success and error messages */
#     .stSuccess, .stError {
#         color: white !important;
#         font-size: 18px;
#         padding: 10px;
#         border-radius: 5px;
#     }
#     .stSuccess {
#         background-color: rgba(0, 128, 0, 0.8) !important;
#     }
#     .stError {
#         background-color: rgba(255, 0, 0, 0.8) !important;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Title of the Quiz Application
# st.title("📝 Quiz Application")

# # Title of the programming language
# st.title("📖 Python McQs")

# # Define Quiz through Dictionary
# questions = {
#     1: {
#         "question": "What is the output of `print(type([]))` in Python?",
#         "options": ["A) <class 'list'>", "B) <class 'tuple'>", "C) <class 'dict'>", "D) <class 'set'>"],
#         "answer": "A) <class 'list'>"
#     },
#     2: {
#         "question": "Which keyword is used to define a function in Python?",
#         "options": ["A) func", "B) define", "C) def", "D) function"],
#         "answer": "C) def"
#     },
#     3: {
#         "question": "What does the `len()` function do in Python?",
#         "options": ["A) Returns the type of an object", "B) Returns the length of an object", "C) Converts a value to an integer", "D) Prints the object"],
#         "answer": "B) Returns the length of an object"
#     },
#     4: {
#         "question": "Which of the following is used to comment a single line in Python?",
#         "options": ["A) //", "B) #", "C) /* */", "D) <!-- -->"],
#         "answer": "B) #"
#     },
#     5: {
#         "question": "What is the output of `print(2 ** 3)`?",
#         "options": ["A) 6", "B) 8", "C) 9", "D) 23"],
#         "answer": "B) 8"
#     },
#     6: {
#         "question": "Which of the following is NOT a valid data type in Python?",
#         "options": ["A) int", "B) float", "C) char", "D) str"],
#         "answer": "C) char"
#     },
#     7: {
#         "question": "What is the output of `print('Hello, World!'[7:12])`?",
#         "options": ["A) World", "B) World!", "C) o, Wo", "D) Error"],
#         "answer": "A) World"
#     },
#     8: {
#         "question": "Which method is used to add an element to the end of a list?",
#         "options": ["A) append()", "B) insert()", "C) add()", "D) extend()"],
#         "answer": "A) append()"
#     },
#     9: {
#         "question": "What is the output of `print(bool(0))`?",
#         "options": ["A) True", "B) False", "C) 0", "D) None"],
#         "answer": "B) False"
#     },
#     10: {
#         "question": "Which module is used for working with regular expressions in Python?",
#         "options": ["A) re", "B) regex", "C) pyregex", "D) string"],
#         "answer": "A) re"
#     },
#     11: {
#         "question": "What is the output of `print(10 / 3)`?",
#         "options": ["A) 3", "B) 3.333", "C) 3.0", "D) 3.3333333333333335"],
#         "answer": "D) 3.3333333333333335"
#     },
#     12: {
#         "question": "Which of the following is used to open a file in Python?",
#         "options": ["A) open()", "B) read()", "C) file()", "D) load()"],
#         "answer": "A) open()"
#     },
#     13: {
#         "question": "What is the output of `print('Python'.lower())`?",
#         "options": ["A) PYTHON", "B) python", "C) Python", "D) Error"],
#         "answer": "B) python"
#     },
#     14: {
#         "question": "Which of the following is a mutable data type in Python?",
#         "options": ["A) tuple", "B) str", "C) list", "D) int"],
#         "answer": "C) list"
#     },
#     15: {
#         "question": "What is the output of `print(3 * 'abc')`?",
#         "options": ["A) abcabcabc", "B) abcabc", "C) abc3", "D) Error"],
#         "answer": "A) abcabcabc"
#     },
#     16: {
#         "question": "Which operator is used for exponentiation in Python?",
#         "options": ["A) ^", "B) **", "C) //", "D) *"],
#         "answer": "B) **"
#     },
#     17: {
#         "question": "What is the output of `print(10 == '10')`?",
#         "options": ["A) True", "B) False", "C) Error", "D) None"],
#         "answer": "B) False"
#     },
#     18: {
#         "question": "Which of the following is used to remove whitespace from the beginning and end of a string?",
#         "options": ["A) trim()", "B) strip()", "C) remove()", "D) clean()"],
#         "answer": "B) strip()"
#     },
#     19: {
#         "question": "What is the output of `print(list(range(3)))`?",
#         "options": ["A) [0, 1, 2]", "B) [1, 2, 3]", "C) [0, 1, 2, 3]", "D) [3]"],
#         "answer": "A) [0, 1, 2]"
#     },
#     20: {
#         "question": "Which of the following is used to handle exceptions in Python?",
#         "options": ["A) try-except", "B) try-catch", "C) handle-except", "D) error-handle"],
#         "answer": "A) try-except"
#     }
# }
# # Convert dictionary values to a list
# question_list = list(questions.values())

# # Initialize a random question if none exists in the session state
# if "current_question" not in st.session_state:
#     st.session_state.current_question = random.choice(question_list)

# # Get Current Question
# question = st.session_state.current_question

# # Display the Question
# st.subheader(question["question"])

# # Create Radio Button
# selected_option = st.radio("Choose your answer", question["options"], key="answer")

# if st.button("Submit Answer"):
#     if selected_option == question["answer"]:
#         st.success("✅ Correct")
#     else:
#         st.error(f"❌ Incorrect! The correct answer is {question['answer']}")
    
#     time.sleep(3)
    
#     # Update the session state with a new random question
#     st.session_state.current_question = random.choice(question_list)
    
#     # Rerun the app to display the new question
#     st.rerun()






# import streamlit as st
# import random
# import time

# # Title of the Quiz Application
# st.title("📝 Quiz Application")

# # Title of the programming language
# st.title("📖 Python McQs")

# # Define Quiz through Dictionary
# questions = {
#     1: {
#         "question": "What is the output of `print(type([]))` in Python?",
#         "options": ["A) <class 'list'>", "B) <class 'tuple'>", "C) <class 'dict'>", "D) <class 'set'>"],
#         "answer": "A) <class 'list'>"
#     },
#     2: {
#         "question": "Which keyword is used to define a function in Python?",
#         "options": ["A) func", "B) define", "C) def", "D) function"],
#         "answer": "C) def"
#     },
#     3: {
#         "question": "What does the `len()` function do in Python?",
#         "options": ["A) Returns the type of an object", "B) Returns the length of an object", "C) Converts a value to an integer", "D) Prints the object"],
#         "answer": "B) Returns the length of an object"
#     },
#     4: {
#         "question": "Which of the following is used to comment a single line in Python?",
#         "options": ["A) //", "B) #", "C) /* */", "D) <!-- -->"],
#         "answer": "B) #"
#     },
#     5: {
#         "question": "What is the output of `print(2 ** 3)`?",
#         "options": ["A) 6", "B) 8", "C) 9", "D) 23"],
#         "answer": "B) 8"
#     },
#     6: {
#         "question": "Which of the following is NOT a valid data type in Python?",
#         "options": ["A) int", "B) float", "C) char", "D) str"],
#         "answer": "C) char"
#     },
#     7: {
#         "question": "What is the output of `print('Hello, World!'[7:12])`?",
#         "options": ["A) World", "B) World!", "C) o, Wo", "D) Error"],
#         "answer": "A) World"
#     },
#     8: {
#         "question": "Which method is used to add an element to the end of a list?",
#         "options": ["A) append()", "B) insert()", "C) add()", "D) extend()"],
#         "answer": "A) append()"
#     },
#     9: {
#         "question": "What is the output of `print(bool(0))`?",
#         "options": ["A) True", "B) False", "C) 0", "D) None"],
#         "answer": "B) False"
#     },
#     10: {
#         "question": "Which module is used for working with regular expressions in Python?",
#         "options": ["A) re", "B) regex", "C) pyregex", "D) string"],
#         "answer": "A) re"
#     },
#     11: {
#         "question": "What is the output of `print(10 / 3)`?",
#         "options": ["A) 3", "B) 3.333", "C) 3.0", "D) 3.3333333333333335"],
#         "answer": "D) 3.3333333333333335"
#     },
#     12: {
#         "question": "Which of the following is used to open a file in Python?",
#         "options": ["A) open()", "B) read()", "C) file()", "D) load()"],
#         "answer": "A) open()"
#     },
#     13: {
#         "question": "What is the output of `print('Python'.lower())`?",
#         "options": ["A) PYTHON", "B) python", "C) Python", "D) Error"],
#         "answer": "B) python"
#     },
#     14: {
#         "question": "Which of the following is a mutable data type in Python?",
#         "options": ["A) tuple", "B) str", "C) list", "D) int"],
#         "answer": "C) list"
#     },
#     15: {
#         "question": "What is the output of `print(3 * 'abc')`?",
#         "options": ["A) abcabcabc", "B) abcabc", "C) abc3", "D) Error"],
#         "answer": "A) abcabcabc"
#     },
#     16: {
#         "question": "Which operator is used for exponentiation in Python?",
#         "options": ["A) ^", "B) **", "C) //", "D) *"],
#         "answer": "B) **"
#     },
#     17: {
#         "question": "What is the output of `print(10 == '10')`?",
#         "options": ["A) True", "B) False", "C) Error", "D) None"],
#         "answer": "B) False"
#     },
#     18: {
#         "question": "Which of the following is used to remove whitespace from the beginning and end of a string?",
#         "options": ["A) trim()", "B) strip()", "C) remove()", "D) clean()"],
#         "answer": "B) strip()"
#     },
#     19: {
#         "question": "What is the output of `print(list(range(3)))`?",
#         "options": ["A) [0, 1, 2]", "B) [1, 2, 3]", "C) [0, 1, 2, 3]", "D) [3]"],
#         "answer": "A) [0, 1, 2]"
#     },
#     20: {
#         "question": "Which of the following is used to handle exceptions in Python?",
#         "options": ["A) try-except", "B) try-catch", "C) handle-except", "D) error-handle"],
#         "answer": "A) try-except"
#     }
# }

# # Convert dictionary values to a list
# question_list = list(questions.values())

# # Initialize a random question if none exists in the session state
# if "current_question" not in st.session_state:
#     st.session_state.current_question = random.choice(question_list)

# # Get Current Question
# question = st.session_state.current_question

# # Display the Question
# st.subheader(question["question"])

# # Create Radio Button
# selected_option = st.radio("Choose your answer", question["options"], key="answer")

# if st.button("Submit Answer"):
#     if selected_option == question["answer"]:
#         st.success("✅ Correct")
#     else:
#         st.error(f"❌ Incorrect! The correct answer is {question['answer']}")
    
#     time.sleep(3)
    
#     # Update the session state with a new random question
#     st.session_state.current_question = random.choice(question_list)
    
#     # Rerun the app to display the new question
#     st.rerun()




# import streamlit as st    # For the web interface
# import random             # For Randomizing the questions
# import time               # For the Timer

# # Title of the Quize Application

# st.title("📝 Quize Application")

# # DEfine quize Quistions ,options ,and answers in the form of the list of Dictionary
# questions ={
#      {
#         "question": "What is the output of `print(type([]))` in Python?",
#         "options": ["A) <class 'list'>", "B) <class 'tuple'>", "C) <class 'dict'>", "D) <class 'set'>"],
#         "answer": "A) <class 'list'>"
#     },
#      {
#         "question": "Which keyword is used to define a function in Python?",
#         "options": ["A) func", "B) define", "C) def", "D) function"],
#         "answer": "C) def"
#     },
#     {
#         "question": "What does the `len()` function do in Python?",
#         "options": ["A) Returns the type of an object", "B) Returns the length of an object", "C) Converts a value to an integer", "D) Prints the object"],
#         "answer": "B) Returns the length of an object"
#     },
#     {
#         "question": "Which of the following is used to comment a single line in Python?",
#         "options": ["A) //", "B) #", "C) /* */", "D) <!-- -->"],
#         "answer": "B) #"
#     },
#     {
#         "question": "What is the output of `print(2 ** 3)`?",
#         "options": ["A) 6", "B) 8", "C) 9", "D) 23"],
#         "answer": "B) 8"
#     },
#     {
#         "question": "Which of the following is NOT a valid data type in Python?",
#         "options": ["A) int", "B) float", "C) char", "D) str"],
#         "answer": "C) char"
#     },
#     {
#         "question": "What is the output of `print('Hello, World!'[7:12])`?",
#         "options": ["A) World", "B) World!", "C) o, Wo", "D) Error"],
#         "answer": "A) World"
#     },
#     {
#         "question": "Which method is used to add an element to the end of a list?",
#         "options": ["A) append()", "B) insert()", "C) add()", "D) extend()"],
#         "answer": "A) append()"
#     },
#     {
#         "question": "What is the output of `print(bool(0))`?",
#         "options": ["A) True", "B) False", "C) 0", "D) None"],
#         "answer": "B) False"
#     },
#     {
#         "question": "Which module is used for working with regular expressions in Python?",
#         "options": ["A) re", "B) regex", "C) pyregex", "D) string"],
#         "answer": "A) re"
#     },
#     {
#         "question": "What is the output of `print(10 / 3)`?",
#         "options": ["A) 3", "B) 3.333", "C) 3.0", "D) 3.3333333333333335"],
#         "answer": "D) 3.3333333333333335"
#     },
#     {
#         "question": "Which of the following is used to open a file in Python?",
#         "options": ["A) open()", "B) read()", "C) file()", "D) load()"],
#         "answer": "A) open()"
#     },
#     {
#         "question": "What is the output of `print('Python'.lower())`?",
#         "options": ["A) PYTHON", "B) python", "C) Python", "D) Error"],
#         "answer": "B) python"
#     },
#     {
#         "question": "Which of the following is a mutable data type in Python?",
#         "options": ["A) tuple", "B) str", "C) list", "D) int"],
#         "answer": "C) list"
#     },
#     {
#         "question": "What is the output of `print(3 * 'abc')`?",
#         "options": ["A) abcabcabc", "B) abcabc", "C) abc3", "D) Error"],
#         "answer": "A) abcabcabc"
#     },
#     {
#         "question": "Which operator is used for exponentiation in Python?",
#         "options": ["A) ^", "B) **", "C) //", "D) *"],
#         "answer": "B) **"
#     },
#     {
#         "question": "What is the output of `print(10 == '10')`?",
#         "options": ["A) True", "B) False", "C) Error", "D) None"],
#         "answer": "B) False"
#     },
#     {
#         "question": "Which of the following is used to remove whitespace from the beginning and end of a string?",
#         "options": ["A) trim()", "B) strip()", "C) remove()", "D) clean()"],
#         "answer": "B) strip()"
#     },
#     {
#         "question": "What is the output of `print(list(range(3)))`?",
#         "options": ["A) [0, 1, 2]", "B) [1, 2, 3]", "C) [0, 1, 2, 3]", "D) [3]"],
#         "answer": "A) [0, 1, 2]"
#     },
#     {
#         "question": "Which of the following is used to handle exceptions in Python?",
#         "options": ["A) try-except", "B) try-catch", "C) handle-except", "D) error-handle"],
#         "answer": "A) try-except"
#     }
# }
    


# # Initialize a random question if none exists in the session state
# if "current _question" not in st.session_state:
#     st.session_state.current_question = random.choice(questions)

# # Get Current Quesstion from session state
# question = st.session_state.current_question

# # Display the Question
# st.subheader(question["question"])

# # Create Radio Buttons for the multiple options
# sellected_option = st.radio("Choose your answer", question["options"],key="answer")

# # Submit button the check the answer
# if st.button("Submit Answer"):
#     # Check the answer if the answer is correct by comparing the selected option with the answer 
#     # in the questions dictionary
#     if sellected_option == question["answer"]:
#         st.success("✅ Correct")
#         st.balloons()
#     else:
#         st.error("❌ Incorrect ! the Correct answer is" + question["answer"])

# # wait for 3 seconds before showing the next question
#         time.sleep(3)

# # Select the new random question
#         st.session_state.current_question = random.choice(question)

# # Rerun the app to display the next question
#         st.rerun()