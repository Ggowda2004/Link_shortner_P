# FastLink – URL Shortener & Analytics Platform

FastLink is a full-stack URL shortening platform built with FastAPI, React, PostgreSQL, and Redis. The application allows users to generate short URLs, track click analytics, and redirect users efficiently using Redis caching. It also includes asynchronous request handling and rate limiting to improve performance, scalability, and reliability.

---

## Features

* Generate short URLs from long URLs
* Redirect users using short links
* Click analytics and tracking
* Redis-based caching for low-latency URL redirection
* Asynchronous FastAPI backend
* PostgreSQL database storage
* IP-based rate limiting
* React frontend for URL creation and analytics viewing
* RESTful API architecture

---

## Tech Stack

### Backend

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy
* Async SQLAlchemy
* Redis

### Frontend

* React
* JavaScript
* HTML
* CSS
* Axios

### Other Tools

* Git
* GitHub

---

## System Architecture

```text
Client
  │
  ▼
React Frontend
  │
  ▼
FastAPI Backend
  │
  ├─────────────► Redis Cache
  │
  ▼
PostgreSQL
```

---

## URL Redirection Flow

```text
User Request
     │
     ▼
Check Redis Cache
     │
 ┌───┴────┐
 │        │
Hit      Miss
 │        │
 ▼        ▼
Redirect  PostgreSQL Lookup
          │
          ▼
     Store in Redis
          │
          ▼
       Redirect
```

---

## Redis Caching

FastLink uses Redis as a high-performance caching layer for URL redirection.

### Cache Miss

1. User accesses a short URL.
2. Redis lookup fails.
3. Original URL is fetched from PostgreSQL.
4. URL mapping is stored in Redis.
5. User is redirected.

### Cache Hit

1. User accesses a short URL.
2. Redis returns the original URL.
3. User is redirected immediately.

This significantly reduces database queries and improves response times.

---

## Asynchronous Architecture

The backend uses:

* Async FastAPI endpoints
* Async SQLAlchemy sessions
* Async Redis operations

This allows the application to efficiently handle concurrent requests and improve overall throughput.

---

## Rate Limiting

To prevent abuse, FastLink implements IP-based rate limiting.

Examples:

* URL creation requests are limited per IP.
* Redirection requests are limited per IP.

This improves service reliability and protects backend resources.

---

## API Endpoints

### Create Short URL

```http
POST /shorten
```

Request:

```json
{
  "original_url": "https://example.com"
}
```

Response:

```json
{
  "short_url": "http://localhost:8000/abc123"
}
```

---

### Redirect URL

```http
GET /{short_code}
```

Redirects users to the original URL.

---

### Get All URLs

```http
GET /all_urls
```

Returns stored URLs and analytics information.

---

## Project Structure

```text
backend/
│
├── routes/
├── services/
├── models/
├── schemas/
├── database/
└── redis/

frontend/
│
├── src/
│   ├── components/
│   ├── pages/
│   ├── api/
│   └── App.jsx
```

---

## Future Improvements

* Custom aliases
* URL expiration support
* User authentication
* Analytics dashboard with charts
* QR code generation for shortened URLs
* Docker deployment
* CI/CD pipeline

---

## Learning Outcomes

This project helped strengthen skills in:

* FastAPI
* React
* PostgreSQL
* Redis
* Asynchronous programming
* REST API design
* Rate limiting
* Database design
* Caching strategies
* Full-stack application development

---

## Author

Gangadhar Gowda K M
