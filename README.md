# AI-First CRM HCP Module

An AI-first Customer Relationship Management (CRM) module designed to help field representatives log and manage interactions with Healthcare Professionals (HCPs).

The application provides two ways to manage HCP interactions:

- A structured interaction form
- A conversational AI assistant

The AI assistant is built using LangGraph and Groq. It understands natural-language requests, dynamically selects the appropriate tool, performs database operations, and returns contextual responses to the user.

The application also supports AI-assisted form autofill using structured data returned by the agent tools.

---

## Features

### Structured HCP Interaction Form

Field representatives can manually record interaction details including:

- HCP
- Interaction type
- Interaction date
- Interaction time
- Attendees
- Topics discussed
- Materials shared
- Samples distributed
- Sentiment
- Outcomes
- Follow-up actions
- Summary

### AI Assistant

Users can interact with the CRM using natural language.

Example:

```text
Log a meeting interaction with Dr. Kumar on 2026-07-15.
We discussed Product A efficacy.
The sentiment was positive.
The doctor showed interest.
Follow up next week.
```

The AI agent can understand the request, select the appropriate LangGraph tool, perform the required database operation, and return the result to the React application.

For supported interaction operations, structured tool results can also be used to update the interaction form.

---

## Tech Stack

### Frontend

- React
- Redux Toolkit
- Axios
- Material UI Icons
- CSS
- Vite

### Backend

- Python
- FastAPI
- SQLAlchemy
- Pydantic

### AI and Agent Framework

- LangGraph
- LangChain Core
- Groq
- Llama 3.3 70B Versatile

### Database

- MySQL
- PyMySQL

---

## System Architecture

```text
User
  |
  |
React UI
  |
  |
Redux State Management
  |
  |
Backend
  |
  |
LangGraph
  |
  +----------------------+
  |                      |
  |                      |
Groq LLM          LangGraph Tools
                         |
                         |
                      Database
```

---

## AI Agent Workflow

```text
    User enters a button to forward a request
              |
              |
       POST /agent/chat
              |
              |
        FastAPI Router
              |
              |
       LangGraph Agent
              |
              |
     Groq LLM understands
       the user request
              |
              |
   LLM selects a suitable tool
              |
              |
      Tool performs action
              |
              |
           Database
              |
              |
      Tool result returned
              |
              |
    AI generates a response
              |
              |
        React UI displays
          the response
```

---

## LangGraph Tools

The AI agent contains five tools.

### 1. `log_interaction`

Creates a new HCP interaction in the CRM database.

The LLM extracts structured interaction information from the user's natural-language request and passes the required values to the tool.

Example:

```text
Log a meeting interaction with Dr. Kumar on 2026-07-15.
We discussed Product A efficacy.
The sentiment was positive.
Follow up next week.
```

### 2. `edit_interaction`

Updates an existing HCP interaction.

Only the fields provided by the user are modified.

Example:

```text
Edit interaction 1.
Change the sentiment to Neutral and change the follow-up action to schedule a meeting next month.
```

### 3. `get_interaction`

Retrieves the details of an existing interaction using its interaction ID.

Example:

```text
Show me the details of interaction 1.
```

### 4. `summarize_interaction`

Retrieves interaction information from the database and provides the context required for the AI assistant to generate a concise professional summary.

Example:

```text
Summarize interaction 1.
```

### 5. `suggest_follow_up`

Uses existing interaction context such as topics discussed, sentiment, outcomes, and current follow-up actions to help the AI assistant suggest an appropriate next action.

Example:

```text
Suggest the next follow-up for interaction 1.
```

---

## REST API Endpoints

The backend provides the following API endpoints:

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/agent/chat` | Send a natural-language request to the AI agent |
| `POST` | `/interactions` | Create a new interaction |
| `GET` | `/interactions` | Retrieve interactions |
| `PUT` | `/interactions/{id}` | Update an existing interaction |
| `GET` | `/hcps` | Retrieve available HCPs |

To Checked This Methods Are In

```text
Postman
```

---

## Project Structure

```text
project-root/
|
├── backend/
    │
    ├── app/
    │   ├── agent/
    │   │   ├── graph.py
    │   │   └── tools.py
    │   │
    │   ├── models/
    │   │   ├── hcp.py
    │   │   └── interaction.py
    │   │
    │   ├── routers/
    │   │   ├── agent.py
    │   │   ├── hcp.py
    │   │   └── interaction.py
    │   │
    │   ├── schemas/
    │   │   ├── agent.py
    │   │   ├── hcp.py
    │   │   └── interaction.py
    │   │
    │   ├── database.py
    │   └── main.py
    │
    └── requirements.txt
```

> The exact files inside individual folders may vary depending on the implementation.

---

## Prerequisites

Before running the project, install:

- Python 3.10 or later
- Node.js
- npm
- MySQL
- Git

You will also need a valid Groq API key.

---

## Environment Configuration

Create a `.env` file inside the `backend` directory.

```env
GROQ_API_KEY=your_groq_api_key
DATABASE_URL=mysql+pymysql://your_username:your_password@localhost:3306/your_database_name
```

Replace:

```text
your_groq_api_key
your_username
your_password
your_database_name
```

with your local configuration.

### Important

Never commit the `.env` file or expose your API key and database credentials in GitHub.

---

## Backend Setup

Open a terminal and change into the backend directory:

```bash
cd backend
```

Create a Python virtual environment

```bash
python3 -m venv env
```

Activate the virtual environment on macOS or Linux:

```bash
source env/bin/activate
```

For Windows:

```bash
env\Scripts\activate
```

Install the required Python dependencies:

```bash
pip install -r requirements.txt
```

Start the FastAPI backend:

```bash
uvicorn app.main:app --reload
```

---

## Frontend Setup

Open another terminal and change into the frontend directory:

```bash
cd frontend
```

Install the frontend dependencies:

```bash
npm install
```

Start the Vite development server:

```bash
npm run dev
```

---

## Running the Complete Application

Run the backend in one terminal:

```bash
cd backend
source env/bin/activate
uvicorn app.main:app --reload
```

Run the frontend in another terminal:

```bash
cd frontend
npm install
npm run dev
```

Then open:

```text
http://localhost:5173
```

---

## Eg: AI Prompts

### Log an Interaction

```text
Log a Meeting interaction with Dr. Kumar on 2026-07-15.
We discussed Product A efficacy.
The sentiment was Positive.
The doctor showed interest.
Follow up next week.
```

### Edit an Interaction

```text
Edit interaction 1.
Change the sentiment to Neutral and change the follow-up action to schedule a meeting next month.
```

### Get Interaction Details

```text
Show me the details of interaction 1.
```

### Summarize an Interaction

```text
Summarize interaction 1.
```

### Suggest a Follow-up

```text
Suggest the next follow-up for interaction 1.
```

---

## Testing

### Test the REST APIs

Start the backend and open:

```text
http://127.0.0.1:8000/docs
```
or

```text
Postman
```


Test:

```text
GET  /hcps
POST /interactions
GET  /interactions
PUT  /interactions/{id}
POST /agent/chat
```

### Test the AI Agent

Use the React AI assistant to test all five tools:

```text
Log a meeting interaction with Dr. Kumar on 2026-07-15.
```

```text
Edit interaction 1 and change the sentiment to Neutral.
```

```text
Show me interaction 1.
```

```text
Summarize interaction 1.
```

```text
Suggest the next follow-up for interaction 1.
```

### Test Error Handling

Try requesting an interaction that does not exist:

```text
Show me interaction 99999.
```

Try logging an interaction for an HCP that does not exist in the database:

```text
Log an interaction with Dr. Unknown.
```

The application should return an appropriate error response instead of creating hardcoded data.

---

## AI-Assisted Form Autofill

When supported agent tools return structured interaction data, the frontend stores the result in Redux.

```text
AI Tool Result
      |
      |
POST /agent/chat Response
      |
      |
React Chat Component
      |
      |
Redux Form State
      |
      |
Interaction Form Autofill
```

This allows the structured form and conversational AI assistant to work together.

---

## Dynamic Data Handling

The application does not depend on hardcoded AI responses.

- HCP information is retrieved from the MySQL database.
- New interactions are stored in the database.
- Existing interactions can be updated dynamically.
- Interaction details can be retrieved dynamically.
- Summaries are generated using stored interaction context.
- Follow-up suggestions are generated using interaction context.
- The LLM dynamically selects the appropriate LangGraph tool based on the user's request.

---

## CORS Configuration

The FastAPI backend allows the React development application to communicate with the API.

During local development, the frontend typically runs at:

```text
http://localhost:5173
```

and the backend runs at:

```text
http://127.0.0.1:8000
```

---

## Security

Sensitive information must be stored in environment variables.

Do not commit:

- Groq API keys
- Database passwords
- `.env` files
- Virtual environments
- `node_modules`


---

## Future Improvements

Possible future improvements include:

- User authentication and role-based access control
- HCP creation and management screens
- Persistent AI conversation history
- Advanced HCP interaction analytics
- Dashboard and reporting features
- Voice-based interaction logging
- Automated follow-up scheduling
- Deployment using cloud infrastructure

---

## Author

Aswin babu K M

---

## License

This project was developed as a technical assignment and demonstration project.