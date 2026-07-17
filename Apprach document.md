# CT200 AI Document Management System
## Project Approach Document

---

# 1. Problem Statement

Organizations often maintain multiple versions of technical documents. Manually identifying differences between document versions and preparing functional test cases is a time-consuming and error-prone process.

The objective of this project is to automate document management by parsing structured documents, comparing different versions, and generating AI-powered functional test cases for selected document sections.

---

# 2. Project Objective

The main objectives of this project are:

- Import multiple versions of technical documents.
- Parse Markdown documents into structured sections.
- Preserve document hierarchy.
- Store parsed data in a database.
- Compare document versions.
- Automatically identify document changes.
- Generate functional test cases using Artificial Intelligence.
- Provide an easy-to-use web interface.

---

# 3. Overall Approach

The project follows a modular architecture where each module performs a specific task.

The overall workflow is:

Document Import

↓

Markdown Parsing

↓

Hierarchy Extraction

↓

Database Storage

↓

Version Comparison

↓

Section Selection

↓

AI Test Case Generation

↓

Display Results

---

# 4. System Architecture

```
                User

                  │

                  ▼

        React Frontend

                  │

                  ▼

           FastAPI Backend

      ┌────────┼────────┐

      ▼        ▼        ▼

 Parser     Database     AI Service

      │        │          │

      ▼        ▼          ▼

 Markdown   SQLite      Groq LLM
```

---

# 5. Module-wise Approach

## Module 1: Document Import

### Purpose

Import different versions of technical documents.

### Steps

- User clicks Import Version 1.
- Backend checks whether Version 1 already exists.
- If not found, it imports the document.
- The same process is repeated for Version 2.

---

## Module 2: Markdown Parsing

### Purpose

Convert Markdown documents into structured nodes.

### Steps

- Read Markdown file.
- Detect headings.
- Detect heading level.
- Extract body content.
- Preserve hierarchy.
- Generate content hash.

Output:

Structured document nodes.

---

## Module 3: Database Storage

### Purpose

Store parsed document information.

### Tables Used

### Documents

Stores:

- Document Name
- Version

### Nodes

Stores:

- Heading
- Body
- Level
- Parent ID
- Content Hash

### Test Cases

Stores:

- Node ID
- Generated Test Cases

---

## Module 4: Version Comparison

### Purpose

Compare Version 1 and Version 2.

### Comparison Logic

The application compares document nodes using their content hashes.

Possible outcomes:

- Added Section
- Removed Section
- Modified Section
- Unchanged Section

---

## Module 5: Load Document Sections

### Purpose

Display all document sections.

### Steps

- Fetch nodes from SQLite.
- Build hierarchical structure.
- Display document headings.
- Allow user interaction.

---

## Module 6: AI Test Case Generation

### Purpose

Automatically generate functional test cases.

### Workflow

User selects a document section.

↓

Frontend sends Node ID.

↓

Backend fetches section content.

↓

Prompt is created.

↓

Groq API is called.

↓

Groq generates test cases.

↓

Backend returns response.

↓

Frontend displays results.

---

# 6. AI Workflow

The selected document section is passed to the Groq Large Language Model.

The AI model:

- Reads the section
- Understands the functionality
- Identifies possible scenarios
- Generates five functional test cases

Output includes:

- Test Case ID
- Title
- Objective
- Preconditions
- Test Steps
- Expected Result
- Priority

---

# 7. Database Workflow

```
Markdown File

      │

      ▼

Parser

      │

      ▼

Structured Nodes

      │

      ▼

SQLite Database

      │

      ▼

Frontend
```

---

# 8. Frontend Workflow

User opens application.

↓

Imports documents.

↓

Compares versions.

↓

Loads document sections.

↓

Selects a section.

↓

Clicks Generate Test Cases.

↓

Generated results are displayed.

---

# 9. Technologies Used

## Frontend

- React.js
- Axios
- CSS
- Vite

---

## Backend

- FastAPI
- Python

---

## Database

- SQLite
- SQLAlchemy ORM

---

## AI

- Groq API
- Llama 3.3 70B Versatile

---

## Other Tools

- Markdown Parser
- Uvicorn
- dotenv

---

# 10. Folder Structure

```
CT200_Project

│

├── frontend

├── routes

├── services

├── parser

├── database

├── models

├── llm

├── config

├── utils

├── data

├── tests

├── main.py

└── README.md
```

---

# 11. Project Workflow Summary

```
Import Document

        │

        ▼

Parse Markdown

        │

        ▼

Create Document Nodes

        │

        ▼

Store in SQLite

        │

        ▼

Compare Versions

        │

        ▼

Load Sections

        │

        ▼

Select Section

        │

        ▼

Generate AI Test Cases

        │

        ▼

Display Results
```

---

# 12. Advantages

- Automates document management.
- Reduces manual effort.
- Supports multiple document versions.
- Preserves document hierarchy.
- Generates AI-powered functional test cases.
- Simple and interactive user interface.
- Easy to extend for future enhancements.

---

# 13. Limitations

- Supports Markdown documents only.
- Uses SQLite for local storage.
- AI generation depends on internet connectivity.
- Designed for structured technical documents.

---

# 14. Future Enhancements

- PDF document upload.
- DOCX support.
- User authentication.
- Export test cases to PDF.
- Export to Excel.
- Search functionality.
- Dashboard analytics.
- Cloud database integration.
- User roles and permissions.
- Version history tracking.

---

# 15. Conclusion

The CT200 AI Document Management System provides an automated solution for document version management and AI-assisted functional test case generation.

The system combines Markdown parsing, hierarchical data management, SQLite storage, version comparison, FastAPI backend services, React frontend, and Groq Large Language Model integration to simplify software documentation analysis and significantly reduce manual testing effort.

The modular architecture makes the application scalable, maintainable, and suitable for future enhancements.