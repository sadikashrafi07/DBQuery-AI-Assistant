import streamlit as st
from pathlib import Path
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_community.utilities import SQLDatabase
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler
from sqlalchemy import create_engine
import sqlite3
from langchain_groq import ChatGroq
from dotenv import load_dotenv  # Import dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Set page configuration with a page icon loaded from a file or fallback to an emoji
page_icon_path =  Path("images/Page Icon.webp")

# Try to read the icon file, fallback to an emoji if file is not found
try:
    with open(page_icon_path, "rb") as f:
        page_icon = f.read()
except FileNotFoundError:
    page_icon = "🦜"  # Fallback emoji if the icon is not found

st.set_page_config(page_title="LangChain: Chat with SQL DB", page_icon=page_icon)

st.title("🦜 LangChain: Chat with SQL DB")

# Database options
LOCALDB = "USE_LOCALDB"
MYSQL = "USE_MYSQL"

# Sidebar for database selection
radio_opt = ["Use SQLite 3 Database - Student.db", "Connect to your MySQL Database"]
selected_opt = st.sidebar.radio(label="Choose the DB you want to chat with", options=radio_opt)

# Initialize variables for MySQL connection details (default None)
mysql_host = mysql_user = mysql_password = mysql_db = None

# Database selection logic
if selected_opt == radio_opt[1]:
    db_uri = MYSQL
    mysql_host = st.sidebar.text_input("Provide MySQL Host")
    mysql_user = st.sidebar.text_input("MySQL User")
    mysql_password = st.sidebar.text_input("MySQL Password", type="password")
    mysql_db = st.sidebar.text_input("MySQL Database")
else:
    db_uri = LOCALDB

# Fetch the API key from environment variables
api_key = os.getenv("GROQ_API_KEY")
print(f"Loaded API Key: {api_key}")  # Debug print to check API Key

if not db_uri:
    st.info("Please enter the database information and URI.")
    st.stop()

if not api_key:
    st.info("Please configure the Groq API Key in the environment.")
    st.stop()

# Initialize the LLM model (backend)
llm = ChatGroq(groq_api_key=api_key, model_name="Llama3-8b-8192", streaming=True)

# Database configuration function with caching to avoid redundant connections
@st.cache_resource(ttl="2h")
def configure_db(db_uri, mysql_host=None, mysql_user=None, mysql_password=None, mysql_db=None):
    if db_uri == LOCALDB:
        dbfilepath = (Path(__file__).parent / "student.db").absolute()
        creator = lambda: sqlite3.connect(f"file:{dbfilepath}?mode=ro", uri=True)
        return SQLDatabase(create_engine("sqlite:///", creator=creator))
    elif db_uri == MYSQL:
        if not (mysql_host and mysql_user and mysql_password and mysql_db):
            st.error("Please provide all MySQL connection details.")
            st.stop()
        return SQLDatabase(create_engine(f"mysql+mysqlconnector://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_db}"))

# Configure the database connection (cached for faster future access)
db = configure_db(db_uri, mysql_host, mysql_user, mysql_password, mysql_db)

# Initialize the toolkit
toolkit = SQLDatabaseToolkit(db=db, llm=llm)

# Create the SQL agent (without specifying agent type)
agent = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=False, # Disable verbose mode to reduce overhead
    max_iterations=40,  # Increase the number of iterations
    max_execution_time=150 # Increase the time limit (in seconds)
)

# Message history handling
if "messages" not in st.session_state or st.sidebar.button("Clear message history"):
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

# Display chat messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Handle user input for SQL queries
user_query = st.chat_input(placeholder="Ask anything from the database")

if user_query:
    # Add user query to message history
    st.session_state.messages.append({"role": "user", "content": user_query})
    st.chat_message("user").write(user_query)

    # Generate and display response from the agent
    with st.chat_message("assistant"):
        streamlit_callback = StreamlitCallbackHandler(st.container())
        response = agent.run(user_query, callbacks=[streamlit_callback])

        # Add assistant's response to message history and display it
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.write(response)
