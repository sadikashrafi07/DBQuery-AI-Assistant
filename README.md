# DBQuery AI Assistant

**Live Link:** [DBQuery AI Assistant Demo](https://dbquery-ai-assistant.streamlit.app/)

## Overview

The **DBQuery AI Assistant** is a conversational AI tool that allows users to query databases using natural language, making it easy to interact with both **SQLite** and **MySQL** databases. This project eliminates the need to write complex SQL queries by providing a user-friendly interface where users can ask database-related questions in plain English.

The project supports both local SQLite databases and remote MySQL databases. Users can select the database type, enter MySQL connection details, and interact with the system through an intuitive chat interface. The assistant is powered by **LangChain's SQL agent** and **Groq** language models, ensuring real-time responses and seamless interaction.

## Features

- **Natural Language Queries**: Users can interact with databases by asking questions in plain English.
- **Database Support**: Choose between local SQLite or remote MySQL databases with easy setup.
- **Real-Time Feedback**: Immediate responses with query results streamed in real-time.
- **Session History**: Keeps chat history for continuous conversation during a session.
- **Error Handling**: Graceful error messages for incorrect database credentials or invalid queries.

## Objectives

The main objectives of the **DBQuery AI Assistant** are:
- To simplify database interaction by translating natural language queries into SQL commands.
- To provide support for multiple database types (SQLite and MySQL).
- To deliver an intuitive user interface with real-time results.

## Problem Statement

Interacting with databases often requires knowledge of SQL, which can be challenging for non-technical users. The **DBQuery AI Assistant** addresses this by providing a natural language interface that translates user queries into SQL commands, streamlining database interactions.

## Tech Stack

- **Front-End**: Streamlit
- **Back-End**: Python
- **Databases**: SQLite and MySQL
- **Natural Language Processing**: LangChain SQL Agent
- **External API**: Groq API for language model processing

## Setup Instructions

### Prerequisites

- **Python 3.10+**
- **Streamlit**
- **MySQL** (if using MySQL as the database)
- **Docker** (optional, for containerization)

### Local Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repository/DBQuery-AI-Assistant.git
   cd DBQuery-AI-Assistant


2. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   - Create a `.env` file in the root directory and add your **Groq API key**:
     ```
     GROQ_API_KEY=your-groq-api-key
     ```

4. **Run the app**:
   ```bash
   streamlit run app.py
   ```

5. **Access the application**:
   - The app will be available at `http://localhost:8501`.


### Running with Docker

1. **Pull the Docker image**:
   ```bash
   docker pull sadiq07/dbquery-ai-assistant
   ```

2. **Run the Docker container**:
   ```bash
   docker run -d -p 80:8501 --env-file .env sadiq07/dbquery-ai-assistant
   ```

3. **Access the application**:
   - Visit `http://localhost:8501` in your browser.

> **Note**: Ensure that your .env file is in the same directory where you run the docker run command. This file should contain any necessary environment variables for your application to function correctly.

### MySQL Integration

To use a MySQL database:

1. Select "Connect to your MySQL Database" in the Streamlit sidebar.
2. Provide the following details in the sidebar:
   - MySQL Host
   - MySQL User
   - MySQL Password
   - MySQL Database name

> **Note**: Ensure that the MySQL server is running before attempting to connect. If the server is not operational, an error message will be displayed.

## Usage

1. **Choose the Database**: Select between the local SQLite database (`student.db`) or connect to a MySQL database using the sidebar.
2. **Input a Query**: Type your query in natural language into the chat interface. Example queries:
   - "Show all students in class A."
   - "What is the average marks of students in the Data Science class?"
   - "How many students scored above 80 in DEVOPS?"
3. **View Results**: The query results will be streamed in real-time in the chat interface.

## Feedback

We value your feedback and suggestions. If you have any ideas for improvement or need support, please reach out to us at angadimohammadsadiq@gmail.com.

## Conclusion

The **DBQuery AI Assistant** project simplifies database interactions by providing a natural language interface, enabling users to execute complex SQL queries without writing any code. The system's flexibility, efficiency, and ease of use make it a valuable tool for users who regularly interact with databases but may not have the technical expertise to write SQL.
