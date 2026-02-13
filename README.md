# 💸 Personal Finance Chatbot

An AI-powered chatbot that helps users track expenses, manage budgets, and receive smart financial advice using natural language.

---

## 🚀 Features
- Natural language expense tracking
- Monthly budget management
- Category-wise spending analysis
- Budget advice & alerts
- Friendly chat interface

---

## 🛠️ Tech Stack
- NLP: Rasa, spaCy
- Backend: Flask, Pandas
- Frontend: Streamlit
- Storage: CSV (synthetic data)

---

## 🧠 How It Works
1. User enters a query in the chat UI
2. Rasa detects intent & entities
3. Custom actions call Flask APIs
4. Budget engine processes data
5. Response is returned to the user

---

## 🧩 Architecture
→ Rasa NLP
→ Custom Actions
→ Flask API
→ Budget Engine (Pandas)
→ Response

The system separates NLP, business logic, and UI to ensure scalability, maintainability, and clean data flow.

---

## ▶️ How to Run
1. Clone the repo
2. Install dependencies  
   ```bash
   pip install -r requirements.txt
3. Start Flask backend
   ```bash
   python backend/app.py
4. Start Rasa server
    ```bash
   rasa run --enable-api
   rasa run actions
5. Start Streamlit UI
   ```bash
   streamlit run ui/streamlit_app.py

![Run](tests/Screenshot%202026-02-13%20224224.png)

---

## 🔐 Data & Security
- Uses synthetic financial data
- No real bank credentials
- Input validation & error handling implemented

---

## 📌 Future Enhancements
- Spending prediction
- Email alerts
- Multi-user support
- Database integration

---

## 👤 Author

**Hrishikesh Ganji**



