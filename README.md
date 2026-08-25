<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=270&section=header&text=Navneet%20TopTech%20Learning%20Hub&fontSize=46&fontColor=FFFFFF&fontAlignY=38&desc=AI-Powered%20Video%20Learning%20and%20Study%20Intelligence%20Platform&descAlignY=60&descSize=19&animation=fadeIn&color=0:0B1F4D,15:123B7A,35:0057D9,55:0EA5E9,75:10B981,100:047857" width="100%"/>
</p>


<div align="center">

# Navneet TopTech Learning Hub

### AI-Powered Video Learning, Notes Generation & Study Intelligence Platform

<img src="https://readme-typing-svg.herokuapp.com?font=Poppins&weight=600&size=22&duration=3200&pause=1000&color=0EA5E9&center=true&vCenter=true&width=1100&lines=Turn+Videos+Into+Complete+AI+Study+Kits;AI+Generated+Notes+and+Summaries;RAG+Powered+Chat+With+Video;AI+Quiz+and+Flashcard+Generation;Teacher+Lesson+Plans;Student+Revision+Intelligence;Smart+EdTech+Learning+Platform"/>

<br>

![Python](https://img.shields.io/badge/Python-3.11+-2563EB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-EdTech-0EA5E9?style=for-the-badge&logo=streamlit&logoColor=white)
![AI](https://img.shields.io/badge/Generative_AI-10B981?style=for-the-badge)
![LLM](https://img.shields.io/badge/LLM-OpenRouter-2563EB?style=for-the-badge)
![RAG](https://img.shields.io/badge/RAG-Video_Chat-22C55E?style=for-the-badge)
![FAISS](https://img.shields.io/badge/FAISS-Vector_Search-0EA5E9?style=for-the-badge)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-Database-1E40AF?style=for-the-badge)
![EdTech](https://img.shields.io/badge/EdTech-AI_Learning-059669?style=for-the-badge)

<br>

**Video Intelligence • Generative AI • RAG • LLM • Smart Notes • Quiz • Flashcards**

</div>

---

## Project Preview

<a href="https://www.loom.com/share/8667a808dd494aafa6b9063a7c9e2aeb" target="_blank">

<img src="https://raw.githubusercontent.com/snehal395jadhav/VIDYA_AI/main/Screenshot.png"  width="95%"/>

</a>

👉 [Click here to watch full screen demo](https://www.loom.com/share/8667a808dd494aafa6b9063a7c9e2aeb)

---

# Overview

**Navneet TopTech Learning Hub** is a production-style AI-powered EdTech SaaS platform designed for students, teachers, schools, coaching institutes, and modern digital learning environments.

The platform transforms educational videos into complete AI-powered study kits.

Users can provide a supported video source and automatically generate:

- AI Video Summaries
- Chapter-Wise Notes
- Key Learning Points
- Exam Questions
- MCQ Quizzes
- Flashcards
- Teacher Lesson Plans
- Student Revision Notes
- Mind Maps
- Timeline Notes
- Transcript-Based AI Chat
- Multiple Export Formats

The platform combines **Large Language Models, Retrieval-Augmented Generation, transcript intelligence, vector retrieval, automated assessment generation, and learning analytics** into a unified educational workspace.

---

# Core Features

- AI Video Understanding
- Automatic Transcript Extraction
- AI Notes Generation
- Smart Video Summarization
- Chapter Detection
- Key Point Extraction
- Exam Question Generation
- MCQ Quiz Generation
- AI Flashcards
- Teacher Lesson Plans
- Student Revision Notes
- Mind Map Generation
- Timeline Generation
- RAG-Powered Video Chat
- FAISS Vector Search
- TF-IDF Retrieval Fallback
- OpenRouter LLM Integration
- AI Title Detection
- AI Subject Detection
- Multi-Language Configuration
- Difficulty Selection
- Notes Style Selection
- Teacher Dashboard
- Student Dashboard
- Administrator Dashboard
- Learning Analytics
- Notes Library
- Export Management
- Activity Audit Logs
- API Usage Monitoring
- Light & Dark Mode
- Role-Based Access Control
- Secure Session Management

---

# Supported Video Sources

The application supports multiple learning-content sources:

```text
YouTube Video
      │
YouTube Playlist
      │
Direct MP4 URL
      │
Public Google Drive Video
      │
Uploaded Recording
      │
      ▼
Navneet TopTech Learning Hub
```

Supported sources include YouTube videos and playlists, direct MP4 URLs, public Google Drive links, and uploaded recordings. :contentReference[oaicite:1]{index=1}

---

# AI Learning Workflow

```text
Video / Recording
        │
        ▼
Source Validation
        │
        ▼
Video Type Detection
        │
        ▼
Transcript Extraction
        │
        ▼
Transcript Cleaning
        │
        ▼
Smart Chunking
        │
        ▼
Vector Indexing
        │
        ▼
LLM Processing
        │
        ├───────────────┐
        ▼               ▼
 AI Study Notes      RAG Index
        │               │
        ▼               ▼
 Quiz / Flashcards   AI Video Chat
        │               │
        └───────┬───────┘
                ▼
         Learning Library
                │
                ▼
             Export
```

The implemented pipeline validates the source, obtains a transcript, cleans and chunks it, indexes the chunks for RAG, generates learning material with OpenRouter, stores the results, and provides review/export capabilities. :contentReference[oaicite:2]{index=2}

---

# System Architecture

```text
                  STUDENT / TEACHER
                         │
                         ▼
              NAVNEET TOPTECH UI
                         │
                         ▼
                    STREAMLIT
                         │
          ┌──────────────┼──────────────┐
          │              │              │
          ▼              ▼              ▼
     VIDEO ENGINE   LEARNING ENGINE   USER SYSTEM
          │              │              │
          ▼              ▼              ▼
      Transcript        LLM         Authentication
          │              │              │
          ▼              ▼              ▼
       Chunking       OpenRouter       RBAC
          │              │              │
          └──────┬───────┘              │
                 ▼                      │
           VECTOR RETRIEVAL             │
                 │                      │
          ┌──────┴───────┐              │
          ▼              ▼              │
       FAISS          TF-IDF             │
          │              │              │
          └──────┬───────┘              │
                 ▼                      │
              RAG CHAT                  │
                 │                      │
                 └──────────┬───────────┘
                            ▼
                       SQLAlchemy
                            │
                            ▼
                         Database
```

---

# Generative AI Engine

The platform uses an LLM to convert raw educational transcripts into structured learning material.

```text
Transcript
    │
    ▼
Prompt Engineering
    │
    ▼
OpenRouter LLM
    │
    ├── Summary
    ├── Chapters
    ├── Key Points
    ├── Questions
    ├── MCQs
    ├── Flashcards
    ├── Lesson Plan
    ├── Revision Notes
    ├── Mind Map
    └── Timeline
```

The project generates eight note sections plus MCQs and flashcards using task-specific prompts and configurable language, difficulty, and notes style. :contentReference[oaicite:3]{index=3}

---

# RAG-Powered Chat With Video

One of the major AI features is **Chat With Video**.

Instead of asking a general-purpose chatbot, users can ask questions directly about the learning content.

```text
Student Question
       │
       ▼
Query Processing
       │
       ▼
Transcript Vector Search
       │
       ▼
Relevant Transcript Chunks
       │
       ▼
Context Construction
       │
       ▼
LLM
       │
       ▼
Transcript-Grounded Answer
```

The chatbot uses transcript chunks for grounding, with FAISS available for vector retrieval and a built-in TF-IDF fallback when FAISS is unavailable. :contentReference[oaicite:4]{index=4}

---

# Transcript Intelligence

The transcript pipeline follows:

```text
YouTube
   │
   ▼
YouTube Caption API
   │
   ├──── Captions Available ────► Transcript
   │
   └──── Captions Missing
                │
                ▼
             yt-dlp
                │
                ▼
              Audio
                │
                ▼
        Faster-Whisper
                │
                ▼
            Transcript
```

The project uses YouTube captions first and can fall back to `yt-dlp` audio extraction plus Whisper transcription. :contentReference[oaicite:5]{index=5}

---

# AI Notes Generator

The AI Notes Generator transforms transcripts into structured study material.

Generated content can include:

```text
AI SUMMARY
     │
     ├── Overview
     ├── Important Concepts
     ├── Chapter Notes
     ├── Key Points
     ├── Exam Questions
     ├── Revision Notes
     ├── Lesson Plan
     └── Timeline
```

---

# Smart Chapter Notes

Long videos can be transformed into chapter-oriented notes.

Example:

```text
Video
 │
 ├── Chapter 01
 │     ├── Summary
 │     └── Key Concepts
 │
 ├── Chapter 02
 │     ├── Summary
 │     └── Key Concepts
 │
 └── Chapter 03
       ├── Summary
       └── Key Concepts
```

---

# AI Quiz Center

The platform includes automatic quiz generation from educational video content.

```text
Video Transcript
       │
       ▼
AI Question Generator
       │
       ▼
MCQ Generation
       │
       ▼
Quiz Center
       │
       ▼
Student Assessment
```

The AI pipeline supports generation of 10+ MCQs as part of the learning kit. :contentReference[oaicite:6]{index=6}

---

# AI Flashcards

Important concepts can automatically be transformed into revision flashcards.

```text
┌────────────────────────────┐
│          QUESTION          │
│                            │
│ What is Machine Learning?  │
└────────────────────────────┘

             ▼ FLIP

┌────────────────────────────┐
│           ANSWER           │
│                            │
│ AI systems that learn      │
│ patterns from data.        │
└────────────────────────────┘
```

---

# Teacher Intelligence

Teachers can use the platform to transform educational videos into structured teaching material.

Capabilities include:

- AI Lesson Plans
- Chapter Notes
- Important Concepts
- Question Generation
- MCQ Generation
- Flashcards
- Revision Material
- Learning Content Library

---

# Student Learning Workspace

Students can use:

- AI Notes
- Smart Summaries
- Video Chat
- MCQ Practice
- Flashcards
- Revision Notes
- Mind Maps
- Timeline Notes
- Generated Content Library

---

# User Roles

The system provides role-aware experiences for:

| Role | Main Purpose |
|---|---|
| Admin | Platform administration |
| Teacher | Teaching & content generation |
| Student | Learning & revision |

The uploaded implementation defines Admin, Teacher, and Student roles with role-based dashboards. :contentReference[oaicite:7]{index=7}

---

# Admin Intelligence

The administrator panel supports:

- User Management
- User CRUD
- Content Oversight
- Activity Audit Logs
- AI Model Settings
- Branding Settings
- API Usage Counters
- System Reports

---

# Learning Analytics

The platform includes analytics capabilities for monitoring learning activity.

```text
Learning Activity
       │
       ▼
Database
       │
       ▼
Pandas Processing
       │
       ▼
Plotly Analytics
       │
       ▼
Dashboard
```

---

# AI Mind Maps

Learning content can be transformed into structured conceptual maps.

```text
                 MAIN TOPIC
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
      Concept A   Concept B   Concept C
          │          │          │
          ▼          ▼          ▼
       Detail      Detail      Detail
```

---

# Timeline Notes

For chronological educational content:

```text
Topic Start
    │
    ▼
Event 01
    │
    ▼
Event 02
    │
    ▼
Important Development
    │
    ▼
Final Outcome
```

---

# Smart Long-Video Processing

Long transcripts can exceed LLM context windows.

The application therefore uses a map-reduce-style condensation workflow for long content before generation. :contentReference[oaicite:8]{index=8}

```text
Long Transcript
       │
       ▼
Smart Chunking
       │
 ┌─────┼─────┐
 ▼     ▼     ▼
C1    C2    C3
 │     │     │
 ▼     ▼     ▼
AI    AI    AI
 │     │     │
 └─────┼─────┘
       ▼
Combined Context
       │
       ▼
Final Study Material
```

---

# OpenRouter LLM Integration

The platform uses OpenRouter for AI generation.

Example configuration:

```env
OPENROUTER_API_KEY=your_api_key_here
OPENROUTER_MODEL=your_model_name
```

The model can also be changed through the administrator's API and branding settings. :contentReference[oaicite:9]{index=9}

> Never commit real API keys or production credentials to GitHub.

---

# Vector Search

The RAG architecture supports:

```text
FAISS
```

with automatic fallback to:

```text
TF-IDF
```

Optional FAISS support can be installed with `faiss-cpu`; the built-in TF-IDF retriever remains available if it is absent. :contentReference[oaicite:10]{index=10}

---

# Database Architecture

The platform uses:

```text
SQLAlchemy
     │
     ▼
SQLite
```

The database stores application information and is automatically initialized on first run. :contentReference[oaicite:11]{index=11}

The architecture can also be configured for PostgreSQL. :contentReference[oaicite:12]{index=12}

---

# Security

Security capabilities include:

- Password Hashing
- Environment-Based Secrets
- Input Validation
- URL Validation
- ORM-Based Database Access
- Role-Based Access
- Session Timeout
- Safe Upload Handling
- Activity Logging

The project uses PBKDF2 password hashing through Passlib and role-aware access controls. :contentReference[oaicite:13]{index=13}

---

# Session Security

Authenticated users are protected by inactivity-based session expiration.

```text
Login
  │
  ▼
Authenticated Session
  │
  ▼
Activity Tracking
  │
  ├── Active ─────► Continue
  │
  └── Timeout ────► Logout
```

The main application checks the user's last activity and automatically expires inactive sessions according to the configured timeout. :contentReference[oaicite:14]{index=14}

---

# Export Engine

Generated learning material can be exported into:

```text
PDF
DOCX
TXT
Markdown
CSV
JSON
```

The project includes branded PDF output, DOCX, text, Markdown, quiz CSV, and JSON backup support. :contentReference[oaicite:15]{index=15}

---

# Application Modules

```text
Dashboard

Generate Notes

Generated Library

Notes Library

Quiz Center

Flashcards

Admin

Website

Settings
```

These routes are defined directly in the Streamlit application router. :contentReference[oaicite:16]{index=16}

---

# Technology Stack

| Layer | Technology |
|---|---|
| Programming | Python |
| Frontend | Streamlit |
| Generative AI | LLM |
| AI Gateway | OpenRouter |
| Video Processing | yt-dlp |
| Transcription | YouTube Transcript API |
| Speech-to-Text | Faster-Whisper |
| RAG | Transcript-Grounded RAG |
| Vector Search | FAISS |
| Retrieval Fallback | TF-IDF |
| Database ORM | SQLAlchemy |
| Database | SQLite |
| Analytics | Plotly |
| Data Processing | Pandas / NumPy |
| PDF Export | ReportLab |
| DOCX Export | python-docx |
| Security | Passlib / PBKDF2 |
| Configuration | python-dotenv |

The core dependency file includes Streamlit, Plotly, Pandas, NumPy, SQLAlchemy, python-dotenv, Passlib, requests, YouTube Transcript API, yt-dlp, ReportLab, and python-docx, with Faster-Whisper and FAISS available as optional extensions. :contentReference[oaicite:17]{index=17} :contentReference[oaicite:18]{index=18}

---

# Project Structure

```text
videomind_ai_notes/
│
├── app.py
│
├── config/
│   ├── settings.py
│   └── prompts.py
│
├── database/
│   ├── db.py
│   ├── models.py
│   └── crud.py
│
├── services/
│   ├── video_loader
│   ├── transcript
│   ├── ai_notes
│   ├── quiz
│   ├── flashcard
│   ├── mindmap
│   ├── vector_store
│   ├── chatbot
│   └── export
│
├── pages/
│   ├── landing
│   ├── login
│   ├── dashboard
│   ├── video_notes
│   ├── notes_library
│   ├── quiz_center
│   ├── flashcards
│   ├── admin_panel
│   └── settings
│
├── components/
│   ├── navbar
│   ├── cards
│   ├── charts
│   └── sidebar
│
├── assets/
│   └── styles.css
│
├── exports/
│
├── requirements.txt
├── .env.example
└── README.md
```

This structure follows the project's documented organization of configuration, database, services, pages, components, styling, and exports. :contentReference[oaicite:19]{index=19}

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/yourusername/navneet-toptech-learning-hub.git
```

```bash
cd navneet-toptech-learning-hub
```

---

## 2. Create Virtual Environment

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Configuration

Copy:

```text
.env.example
```

to:

```text
.env
```

Configure:

```env
OPENROUTER_API_KEY=your_api_key_here
OPENROUTER_MODEL=your_model_name

DATABASE_URL=sqlite:///videomind.db

APP_NAME=Navneet TopTech Learning Hub

ADMIN_EMAIL=your_admin_email
ADMIN_PASSWORD=your_secure_password

SESSION_TIMEOUT_MINUTES=60
```

The project uses an SQLite database named `videomind.db` by default. :contentReference[oaicite:20]{index=20}

---

# Run Application

```bash
streamlit run app.py
```

The main application identifies `app.py` as the Streamlit entry point. :contentReference[oaicite:21]{index=21}

---

# Optional Whisper Support

For videos without captions:

```bash
pip install faster-whisper
```

---

# Optional FAISS Support

For vector-based semantic retrieval:

```bash
pip install faiss-cpu
```

If FAISS is unavailable, the application can use its built-in TF-IDF retriever. :contentReference[oaicite:22]{index=22}

---

# AI Error Handling

The application includes handling for:

- Invalid Links
- Private Videos
- Missing Transcripts
- Audio Download Failures
- Missing API Keys
- AI Provider Failures
- API Rate Limits
- Empty Transcripts
- Over-Length Videos
- Unsupported Formats
- Database Errors

Failed videos can be marked as failed in the library rather than crashing the entire application. :contentReference[oaicite:23]{index=23}

---

# Enterprise Use Cases

### Schools

Generate learning material directly from educational videos.

### Teachers

Create lesson plans, quizzes, notes, and revision material.

### Students

Generate structured study material and chat directly with video content.

### Coaching Institutes

Transform lectures and recorded classes into reusable study resources.

### Digital Learning Platforms

Integrate AI-powered video intelligence into modern EdTech workflows.

---

# Business Benefits

- Faster Educational Content Creation
- Automated Study Material Generation
- Reduced Manual Note-Taking
- Personalized Learning Resources
- AI-Assisted Revision
- Automatic Assessment Creation
- Transcript-Grounded Question Answering
- Centralized Learning Library
- Teacher Productivity Enhancement
- Student Self-Learning Support

---

# Future Enhancements

- AI Voice Tutor
- Agentic AI Learning Assistant
- Multi-Agent Learning System
- Adaptive Learning Paths
- Personalized AI Tutor
- Student Performance Prediction
- Automated Difficulty Adaptation
- AI Doubt-Solving Agent
- Multi-Language Voice Support
- Real-Time Lecture Processing
- LMS Integration
- Google Classroom Integration
- Microsoft Teams Integration
- Mobile Application
- Parent Dashboard
- Teacher Analytics
- Advanced Learning Recommendations
- Knowledge Graph
- GraphRAG
- LangChain Integration
- LangGraph Agent Workflows
- PostgreSQL
- Cloud Deployment
- Docker
- Kubernetes

---

# Project Vision

```text
                   VIDEO
                     │
                     ▼
             AI UNDERSTANDING
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
        NOTES       QUIZ       RAG
          │          │          │
          ▼          ▼          ▼
      FLASHCARDS   EXAMS     AI CHAT
          │          │          │
          └──────────┼──────────┘
                     ▼
             SMART LEARNING
                     │
                     ▼
               BETTER OUTCOMES
```

---

# Developed By

<div align="center">

## SNEHAL LAXMAN JADHAV

### AI Engineer

### Navneet Education Limited

<br>

**Building Intelligent AI Solutions for Education**

</div>

---

<div align="center">

# Navneet TopTech Learning Hub

### Transform Every Video Into an Intelligent Learning Experience

**AI • LLM • RAG • OpenRouter • FAISS • Streamlit • Python • EdTech**

<br>

![AI Learning](https://img.shields.io/badge/AI_LEARNING-10B981?style=for-the-badge)

![RAG](https://img.shields.io/badge/RAG-0EA5E9?style=for-the-badge)

![LLM](https://img.shields.io/badge/LLM-2563EB?style=for-the-badge)

![Video AI](https://img.shields.io/badge/VIDEO_AI-22C55E?style=for-the-badge)

![EdTech](https://img.shields.io/badge/EDTECH-1D4ED8?style=for-the-badge)

![Enterprise AI](https://img.shields.io/badge/ENTERPRISE_AI-059669?style=for-the-badge)

</div>

<p align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&height=170&section=footer&color=0:0F766E,20:10B981,40:22C55E,60:0EA5E9,80:2563EB,100:1E3A8A" width="100%">
</p>
