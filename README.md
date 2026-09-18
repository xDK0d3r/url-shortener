# URL Shortener

A **learning project**: a URL shortener web application built with **Python, FastAPI, SQLite, HTML and CSS**.

## Overview

This project converts long URLs into shorter, easier-to-share URLs.

When a user opens the generated short URL, the application looks up the original URL and redirects the user to its destination.

The project is being developed as part of my hands-on learning journey into **Python backend and web application development**.

## Features

* Create a short URL from a long URL
* Redirect short URLs to their original destinations
* Store URL mappings in SQLite
* Web interface using HTML and CSS
* FastAPI backend for handling application logic and HTTP requests

## Tech Stack

* **Python**
* **FastAPI**
* **SQLite**
* **HTML**
* **CSS**
* **Git & GitHub**

## How It Works

```text
Long URL
   ↓
FastAPI Backend
   ↓
Generate Short Code
   ↓
Store URL Mapping in SQLite
   ↓
Return Short URL
   ↓
User Opens Short URL
   ↓
FastAPI Finds Original URL
   ↓
Redirect to Original URL
```

## Project Structure

The project structure will be documented as the application develops.

## Development Status

**In Development**

This is a learning project focused on understanding how a complete web application works across the **frontend, backend, and database layers**.

The application is being developed incrementally, starting with the backend and database functionality before completing the web interface.

## What I'm Learning

Through this project, I'm practicing:

* FastAPI fundamentals
* REST API concepts
* HTTP methods and routing
* URL redirection
* SQLite database integration
* Backend application structure
* Connecting HTML/CSS with a Python backend
* Building and testing a complete web application

## Future Improvements

Potential improvements may include:

* URL expiration
* Click tracking
* Custom short codes
* Improved error handling
* Additional URL management features

## Author

**Dhanush K**
GitHub: [xDK0d3r](https://github.com/xDK0d3r)

## License

This project is licensed under the **MIT License**.

