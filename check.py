import os, sys

print("\n=== PlacePrep Environment Check ===\n")

# Check Python
print(f"Python: {sys.version.split()[0]}")

# Check Flask
try:
    import flask
    print(f"Flask: OK")
except ImportError:
    print("Flask: NOT INSTALLED - run: pip install flask werkzeug")
    sys.exit(1)

try:
    from werkzeug.security import generate_password_hash
    print(f"Werkzeug: OK")
except ImportError:
    print("Werkzeug: NOT INSTALLED - run: pip install werkzeug")
    sys.exit(1)

# Check file structure
required = {
    "app.py": "Backend",
    "templates/base.html": "Base layout",
    "templates/auth.html": "Auth page",
    "templates/dashboard.html": "Dashboard",
    "templates/profile.html": "Profile",
    "templates/mock_test.html": "Mock test",
    "templates/coding.html": "Coding lab",
    "templates/performance.html": "Performance",
    "templates/company_sets.html": "Company sets",
    "templates/notifications.html": "Notifications",
    "templates/admin.html": "Admin panel",
    "static/css/base.css": "CSS",
    "static/js/base.js": "JS",
}

print("\nFile check:")
all_ok = True
for path, name in required.items():
    exists = os.path.exists(path)
    status = "OK" if exists else "MISSING"
    print(f"  {'[OK]' if exists else '[!!]'} {path} ({name})")
    if not exists:
        all_ok = False

if all_ok:
    print("\nAll files present. Starting app...\n")
    from app import app, init_db
    init_db()
    app.run(debug=True, port=5000)
else:
    print("\nSome files are missing. Make sure you're running from the placement_platform/ folder.")
    print("cd placement_platform && python check.py\n")
