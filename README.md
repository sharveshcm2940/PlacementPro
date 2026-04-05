# PlacePrep - Placement Preparation Platform

A full-stack placement preparation platform built with Python Flask + HTML/CSS/JS.

## Features
- User Authentication (Sign Up / Login) with roles (Student / Admin)
- Student Profile with resume upload
- Mock Test Generator (Company-specific, difficulty, topics)
- Timed Test Interface with question navigator and auto-save
- Coding Lab with multi-language code editor and test cases
- Instant Results with section-wise analysis and explanations
- Performance Dashboard with score history and progress tracking
- Company-wise Practice Sets (TCS, Infosys, Amazon, Google, etc.)
- Admin Panel (user management, stats, question overview)
- Notifications system

## Project Structure

```
placement_platform/
├── app.py                    # Flask backend (all routes + API)
├── requirements.txt
├── placement.db              # SQLite DB (auto-created on first run)
├── templates/
│   ├── base.html             # Shared layout (sidebar, topbar, nav)
│   ├── auth.html             # Login / Sign Up page
│   ├── dashboard.html        # Student dashboard
│   ├── profile.html          # Student profile editor
│   ├── mock_test.html        # Mock test generator + test interface + results
│   ├── coding.html           # Coding lab with editor
│   ├── performance.html      # Performance analytics
│   ├── company_sets.html     # Company-wise practice sets
│   ├── notifications.html    # Notification center
│   └── admin.html            # Admin panel
└── static/
    ├── css/
    │   └── base.css          # Global styles
    ├── js/
    │   └── base.js           # Shared JS (toast, sidebar, notifications)
    └── uploads/              # Uploaded resumes
```

## Setup & Run

### 1. Install dependencies
```bash
pip install flask werkzeug
```

### 2. Run the app
```bash
cd placement_platform
python app.py
```

### 3. Open in browser
```
http://localhost:5000
```

## Default Credentials

| Role    | Email                    | Password   |
|---------|--------------------------|------------|
| Admin   | admin@placement.com      | admin123   |

Students can register from the Sign Up page.

## Pages & Navigation

| URL              | Page                      |
|------------------|---------------------------|
| /                | Login / Sign Up           |
| /dashboard       | Student Dashboard         |
| /profile         | My Profile                |
| /mock-test       | Mock Test Generator       |
| /coding          | Coding Lab                |
| /performance     | Performance Analytics     |
| /company-sets    | Company Practice Sets     |
| /notifications   | Notifications             |
| /admin           | Admin Panel (admin only)  |

## Notes
- The coding runner is simulated (sandboxed) — test cases are pre-validated.
  To enable real code execution, integrate Judge0 API or subprocess with sandboxing.
- Google OAuth requires configuring OAuth credentials in production.
- The SQLite DB is auto-initialized on first run.
