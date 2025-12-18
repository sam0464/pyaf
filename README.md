🌤️ SanchAI Weather Assistant

An AI-powered weather assistant built as part of a **Tech Assessment** using **React, FastAPI, LangChain, and OpenRouter**.  
Users can ask natural language questions like *“What’s the weather in Pune today?”* and receive intelligent, conversational weather responses.

---

## 🚀 Project Overview

**SanchAI Weather Assistant** is a minimal yet powerful full-stack application that demonstrates:

- End-to-end AI application development
- Frontend–Backend integration
- LLM tool calling using LangChain
- Clean React UI with FastAPI backend

This project is designed to showcase **real-world AI engineering skills** suitable for internship and entry-level AI/ML roles.

---

## 🧠 Key Features

- 🌍 Ask weather of **any city** in natural language  
- 🤖 **LLM-powered reasoning** to identify city names  
- 🔧 Tool calling via **LangChain Agent**
- ⚡ Fast and lightweight **FastAPI backend**
- 🎨 Simple and clean **React frontend**
- 🔑 Uses **OpenRouter API** for LLM responses

---

## 🛠️ Tech Stack

### Frontend
- React.js
- JavaScript
- Axios
- HTML / CSS

### Backend
- FastAPI
- Python 3.10+
- LangChain
- OpenRouter
- Uvicorn
- python-dotenv

---

## 🔁 Application Flow

1. User enters a query such as:
   - “What’s the weather of Pune?”
   - “Weather in Mumbai today”

2. React frontend sends the query to the FastAPI backend.

3. Backend:
   - Passes the query to a **LangChain Agent**
   - Extracts the city name
   - Calls the weather tool
   - Uses LLM to generate a natural response

4. The generated response is returned to the frontend and displayed to the user.



