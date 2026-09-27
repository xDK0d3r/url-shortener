# URL Shortener

A simple URL Shortener web application built with **Python, FastAPI, Jinja2, and SQLite**.

This project was built as a **learning project** to practice backend web development, database integration, and serving HTML pages with FastAPI.

## Live Demo

**Live Demo:** https://url-shortener-k5ed.onrender.com

## Features

* Enter a long URL and generate a short URL
* Store shortened URLs in SQLite
* Redirect short URLs to their original destinations
* Simple HTML + CSS user interface
* Server-side rendering using Jinja2
* Basic handling for empty URL input

## Tech Stack

* **Python**
* **FastAPI** — Web framework
* **Jinja2** — HTML templating
* **SQLite** — Database
* **HTML**
* **CSS**

## How It Works

1. The user enters a long URL into the web interface.
2. FastAPI receives the submitted URL.
3. The application generates a short code.
4. The short code and original URL are stored in SQLite.
5. The application displays the shortened URL.
6. When the short URL is opened, FastAPI looks up the corresponding original URL.
7. The user is redirected to the original URL.

## Project Structure

```text
url-shortener/
├── main.py
├── database.py
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── .gitignore
├── LICENSE
└── README.md
```

## Running Locally

Clone the repository and enter the project directory.

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Start the development server:

```bash
uvicorn main:app --reload
```

Open the application in your browser:

```text
http://127.0.0.1:8000
```

## Database

The application uses SQLite to store shortened URLs.

The database contains:

* `short_code` — Unique identifier for the shortened URL
* `original_url` — The original URL to redirect to

The SQLite database file is generated locally and is not included in the repository.

## Project Status

**V1 — Complete**

> ### Current V1 Scope
>
> The current version completes the core URL-shortening workflow:
>
> * **URL shortening** — Generate a unique 6-character short code for a submitted URL.
> * **SQLite storage** — Store the short code and original URL in the database.
> * **URL redirection** — Open a short URL and redirect to its original destination.
> * **Web interface** — Provide a simple HTML + CSS interface for creating shortened URLs.
> * **Server-side rendering** — Use Jinja2 templates with FastAPI.
> * **Input handling** — Handle empty URL submissions through the web interface.
>
> The project intentionally keeps the V1 scope simple and focused on the fundamental URL-shortening workflow.

Future versions may include additional features such as URL management, expiration, analytics, and other enhancements.

## License

This project is licensed under the **MIT License**.

## Author

**Dhanush K | xDK0d3r**

This project was created as part of my journey learning Python backend and web development.

