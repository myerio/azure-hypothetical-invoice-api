# Hypothetical Invoice API

A lightweight, containerized FastAPI project demonstrating how to build and structure a simple REST API using:

- FastAPI  
- SQL Server (Dockerized)  
- Docker Compose  
- Clean environment‑based configuration  

This project is **hypothetical**, uses **fake credentials**, and contains **no real data**.  
It is designed for **learning, experimentation, and portfolio presentation**.

---

## 🚀 Features

- FastAPI backend with automatic interactive documentation  
- SQL Server running in a Docker container  
- Clean project structure ready for extension  
- Example Docker Compose configuration  
- Safe handling of environment variables  
- Minimal, easy‑to‑understand codebase  


![API Flow Diagram](docs/flow-diagram.png)

---

## 🧱 Project Structure

```
.
├── app.py
├── Dockerfile
├── requirements.txt
├── docker-compose.example.yml
├── .gitignore
└── README.md
```

### Not included in the repository:
- `docker-compose.yml` (ignored for safety)
- Any real credentials
- Any real data

---

## 🐳 Running the Project with Docker

### 1. Install prerequisites
- Docker Desktop  
- Python 3.10+ (optional, only if running locally)

---

### 2. Create your own `docker-compose.yml`

Copy the example file:

```bash
cp docker-compose.example.yml docker-compose.yml
```

Update the environment variables inside the file:

```yaml
SA_PASSWORD=YourPassword123!
DB_PASSWORD=YourPassword123!
```

These values are **fake** and safe for local development.

---

### 3. Start the containers

```bash
docker-compose up --build
```

This will:

- Start SQL Server  
- Build and run the FastAPI application  
- Expose the API at **http://localhost:8000**

---

## 📘 API Documentation

Once running, access the interactive docs:

### Swagger UI  
```
http://localhost:8000/docs
```

## 🗄 Database

The API connects to a SQL Server instance running inside Docker.  
A persistent volume is used:

```
sql_data:/var/opt/mssql
```

This ensures your database survives container restarts.

---

## 🔐 Security Notes

- Passwords are fake  
- No sensitive data is included  
- Real `docker-compose.yml` is intentionally excluded  
- Only the safe example file is committed  

This mirrors real‑world best practices for handling secrets.

---

## 🧩 Extending the Project

You can easily add:

- CRUD endpoints  
- Authentication  
- Database migrations  
- Seed scripts  
- Real invoice models  
- Frontend integration  

The project is intentionally minimal so you can build on top of it.

---

## 🧑‍💻 Author

**Gabriel**  
Backend developer exploring FastAPI, Docker, and clean API design.

---

## 📄 License

This project is provided for educational and portfolio purposes.  
Feel free to fork, modify, and experiment.
