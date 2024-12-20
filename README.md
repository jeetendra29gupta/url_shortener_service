# URL Shortener Service

This project is a simple URL shortening service built with **Python** and **FastAPI**. The service allows users to shorten URLs and access original URLs via the shortened links. It also includes an API endpoint to return metrics about the top 3 domains used in the URLs stored in the system.

## Features

- Shorten URLs and return the shortened link.
- Redirect to the original URL when the shortened URL is accessed.
- Prevent duplicate shortened URLs for the same original URL.
- Metrics endpoint that returns the top 3 most frequent domains.
- Dockerized for easy deployment.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup](#setup)
  - [Local Setup](#local-setup)
  - [Docker Setup](#docker-setup)
- [Endpoints](#endpoints)
- [Testing](#testing)

---

## Technologies Used

- **FastAPI**: For building the RESTful API.
- **Uvicorn**: ASGI server to run the FastAPI application.
- **Pydantic**: For data validation.
- **SQLite**: In-memory database to store URL mappings.
- **Validators**: To validate the URLs.
- **Docker**: For containerization.
- **pytest**: For unit testing.

---

## Setup

### Local Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/jeetendra29gupta/url_shortener_service.git
   cd url_shortener_service
   ```

2. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application locally**:
   ```bash
   python main.py
   ```

4. The application will be accessible at `http://localhost:8181`.

---

### Docker Setup

1. **Build the Docker image**:
   ```bash
   sudo docker build -t url_shortener_service .
   ```

2. **Run the Docker container**:
   ```bash
   sudo docker run -d -p 8181:8181 url_shortener_service
   ```

3. **Access the API**:
   - The application will be running on `http://localhost:8181`.

---

## Endpoints

### `GET /`

- **Description**: Returns a "Hello, World!" message.
- **Response**:
  ```json
  {
      "message": "Hello, World!"
  }
  ```

### `POST /shorten`

- **Description**: Accepts a URL and returns a shortened version.
- **Request Body**:
  ```json
  {
      "url": "https://www.example.com"
  }
  ```
- **Response**:
  ```json
  {
      "original_url": "https://www.example.com",
      "shorten_url": "http://localhost:8181/abc123"
  }
  ```

### `GET /{shorten_url}`

- **Description**: Redirects to the original URL for the given shortened URL.
- **Example**: If the shortened URL is `abc123`, it will redirect to the original URL.

### `GET /metrics/`

- **Description**: Returns the top 3 domains based on the frequency of URLs shortened.
- **Response**:
  ```json
  {
      "example.com": 25,
      "github.com": 10,
      "google.com": 8
  }
  ```

---

## Testing

### Unit Tests

To ensure the functionality of the service, the project includes several unit tests. These tests are located in the `tests/` folder and use `pytest` as the testing framework.

### Running Tests

1. **Install the testing dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the tests**:
   ```bash
   pytest
   ```

---