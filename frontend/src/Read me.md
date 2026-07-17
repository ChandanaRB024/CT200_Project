# 📄 CT200 AI Document Management System

## Overview

The CT200 AI Document Management System is a full-stack web application developed to automate document parsing, version comparison, and AI-powered functional test case generation.

The system imports technical documents written in Markdown, converts them into structured hierarchical nodes, stores them in a SQLite database, compares different document versions, and generates functional test cases for any selected document section using the Groq Large Language Model (LLM).

This project demonstrates the integration of document processing, database management, REST APIs, Artificial Intelligence, and a modern React frontend into a single application.

---

# Features

### Document Import
- Import Version 1 document
- Import Version 2 document
- Prevent duplicate document imports
- Store document metadata in SQLite

### Markdown Parsing
- Parse Markdown documents
- Extract headings and content
- Preserve hierarchical parent-child relationships
- Generate content hashes for every node

### Version Comparison
- Compare Version 1 and Version 2
- Identify Added sections
- Identify Removed sections
- Identify Modified sections
- Display comparison results through API

### Document Section Management
- Load all document sections
- Maintain heading hierarchy
- Store parent-child relationships
- Retrieve document nodes efficiently

### AI Test Case Generation
- Select any document section
- Generate functional test cases using Groq LLM
- Automatically scroll to generated results
- Store generated test cases for future access

### User Interface
- Modern React frontend
- Responsive design
- REST API integration
- Interactive dashboard
- AI-powered workflow

---

# Project Architecture

```
CT200_Project
│
├── app
├── config
├── data
├── database
├── frontend
├── llm
├── models
├── parser
├── routes
├── schemas
├── services
├── tests
├── utils
├── main.py
├── requirements.txt
└── README.md
```

---

# Tech Stack

## Frontend

- React.js
- Axios
- CSS3
- JavaScript
- Vite

## Backend

- FastAPI
- Python

## Database

- SQLite
- SQLAlchemy ORM

## AI Integration

- Groq API
- Llama 3.3 70B Versatile

## Other Libraries

- Markdown Parser
- dotenv
- Uvicorn

---

# Workflow

### Step 1

Import Version 1 Markdown document.

↓

### Step 2

Import Version 2 Markdown document.

↓

### Step 3

Parse Markdown document into hierarchical nodes.

↓

### Step 4

Store documents and nodes in SQLite database.

↓

### Step 5

Compare Version 1 and Version 2.

↓

### Step 6

Load document sections.

↓

### Step 7

Select any section.

↓

### Step 8

Generate AI-powered functional test cases.

↓

### Step 9

Display generated test cases on the frontend.

---

# Database Structure

## Documents Table

Stores:

- Document ID
- Document Name
- Version

---

## Nodes Table

Stores:

- Node ID
- Heading
- Body
- Level
- Parent ID
- Document ID
- Content Hash

---

## Test Cases Table

Stores:

- Test Case ID
- Node ID
- AI Generated Test Cases

---

# API Endpoints

## Import Version 1

```
POST /import/v1
```

Imports Version 1 document.

---

## Import Version 2

```
POST /import/v2
```

Imports Version 2 document.

---

## Compare Versions

```
GET /compare
```

Compares Version 1 and Version 2 documents.

---

## Load Nodes

```
GET /nodes/{document_id}
```

Returns all document sections.

---

## Generate Test Cases

```
GET /generate/{node_id}
```

Generates AI-based functional test cases.

---

# AI Prompt Workflow

The selected document section is sent to the Groq LLM.

The model:

- Reads the document section
- Understands the functionality
- Generates five functional test cases
- Returns structured test cases

---

# Key Functionalities

✔ Import document versions

✔ Parse Markdown documents

✔ Preserve document hierarchy

✔ Store structured data in SQLite

✔ Compare document versions

✔ Retrieve document sections

✔ Generate AI-powered functional test cases

✔ Display results through React frontend

---

# Project Modules

## Parser Module

Responsible for:

- Reading Markdown files
- Detecting headings
- Building hierarchy
- Generating hashes

---

## Database Module

Responsible for:

- Document storage
- Node storage
- Test case storage

---

## Comparison Module

Responsible for:

- Version comparison
- Added nodes
- Removed nodes
- Modified nodes

---

## AI Module

Responsible for:

- Groq API communication
- Prompt creation
- Functional test case generation

---

## Frontend Module

Responsible for:

- User Interface
- API communication
- Displaying document sections
- Displaying AI-generated test cases

---

# Advantages

- Automates document processing
- Reduces manual test case creation
- Supports version management
- AI-assisted software testing
- Easy to use
- Fast document comparison
- Scalable architecture

---

# Future Enhancements

- User Authentication
- PDF Upload Support
- Multiple Document Formats
- Export Test Cases to PDF
- Export to Excel
- Search Functionality
- Dashboard Analytics
- User Roles
- Cloud Database Integration
- Version History Tracking

---

# Project Outcome

The CT200 AI Document Management System successfully integrates document parsing, database management, version comparison, and Artificial Intelligence into a single full-stack application.

The system enables users to import document versions, compare modifications, explore document sections, and automatically generate functional test cases using Groq's Large Language Model, significantly reducing manual effort in software testing and document analysis.

---

# Author

**Chandana R B**

Information Science Engineering

CT200 AI Document Management System