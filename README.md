# 🤖 GenAI Chatbot SaaS

A full-stack AI-powered chatbot built during the **SaaS Bootcamp**. This application uses **FastAPI** as the backend and **HTML, CSS, and JavaScript** as the frontend. It integrates the **Google Gemini API** to generate intelligent responses in real time and is configured for deployment on **Vercel**.

---

## 🚀 Features

* 🤖 AI-powered chatbot using Google Gemini
* 💬 Real-time conversations
* 🎨 Modern and responsive user interface
* 🌙 Dark/Light mode toggle
* ➕ New Chat functionality
* ⚡ FastAPI REST API backend
* ☁️ Vercel deployment ready
* 🔐 Environment variable support

---

## 🛠️ Tech Stack

### Frontend

* HTML5
* CSS3
* JavaScript (ES6)

### Backend

* Python
* FastAPI
* Google Gemini API
* Pydantic
* Uvicorn
* Python Dotenv

### Deployment

* Vercel
* Git & GitHub

---

## 📁 Project Structure

```text
genai-chatbot-saas/
│
├── backend/
│   ├── index.py
│   ├── gemini_service.py
│   └── config.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── app.js
│
├── .vercel/
│   └── project.json
│
├── .gitignore
├── requirements.txt
├── vercel.json
├── .env
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/genai-chatbot-saas.git
```

### 2. Navigate to the project folder

```bash
cd genai-chatbot-saas
```

### 3. Install the required dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

```env
GEMINI_API_KEY=your_gemini_api_key
MODEL_NAME=gemini-2.5-flash
```

### 5. Run the backend server

```bash
uvicorn backend.index:app --reload
```

Open your browser and access:

```
http://127.0.0.1:8000
```

FastAPI Documentation:

```
http://127.0.0.1:8000/docs
```

---

## 📡 API Endpoint

### POST `/api/chat`

**Request**

```json
{
  "message": "Hello!"
}
```

**Response**

```json
{
  "reply": "Hello! How can I help you today?"
}
```

---

## ☁️ Deployment

This project is configured for deployment on **Vercel**.

### Deploy Steps

1. Push the project to GitHub.
2. Import the repository into Vercel.
3. Add your environment variables:

   * `GEMINI_API_KEY`
   * `MODEL_NAME`
4. Click **Deploy**.

> **Note:** Never commit your `.env` file or the `.vercel` folder to GitHub because they contain local configuration and sensitive information.

---

## 📚 Learning Outcomes

Through this project, I learned:

* Full-stack SaaS application development
* FastAPI backend development
* Google Gemini API integration
* REST API development
* Frontend development with HTML, CSS, and JavaScript
* API communication using Fetch API
* Environment variable management
* Git & GitHub workflow
* Vercel deployment

---

## 🔮 Future Improvements

* User Authentication
* Chat History
* Markdown Support
* Image Upload Support
* Multiple AI Models
* Conversation Export
* Better Error Handling

---

## 👩‍💻 Author

**Swati Jadhav**




