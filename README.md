An AI-powered client support chatbot for FinServe — a financial services company offering lending and credit products to SMEs and retail clients.
Built as a proof-of-concept to reduce the workload on the client support team by automating responses to routine enquiries.
The problem
FinServe's 10-person support team answers every client enquiry manually — including hundreds of repetitive questions about loan products, payment schedules, and application status. There is no shared knowledge base and no standard responses, which leads to slow response times and inconsistent quality.
The solution
An AI assistant (Maya) that handles routine queries 24/7, allowing human agents to focus only on complex cases that genuinely require personal attention.
Maya can help with:

Loan and account status inquiries
Payment schedules and due dates
Product information and eligibility
Application process questions

Automatic escalation: if a client asks about complaints, fraud, legal matters, or loan restructuring — Maya detects it and hands off to a human agent.
Tech stack

Backend: FastAPI (Python)
AI: Google Gemini API (gemini-2.5-flash)
Frontend: HTML + Vanilla JavaScript
Server: Uvicorn
