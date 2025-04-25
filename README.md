# FastAPI JWT Authentication Backend

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)

A secure REST API with JWT authentication, user management, and middleware support built with FastAPI.

---

## 🚀 Features

- 🔒 JWT Authentication (Bearer tokens)
- 👥 User management (CRUD operations)
- ⏱ Request logging middleware
- 🔄 CORS support
- 📚 Interactive API documentation
- ✅ Input validation with Pydantic models
- 🔐 Password hashing with Bcrypt

---

## 🛠 Tech Stack

- **Framework**: FastAPI
- **Authentication**: JWT (`python-jose`)
- **Password Hashing**: Passlib (`bcrypt`)
- **Server**: Uvicorn
- **Validation**: Pydantic

---

## 📁 Project Structure

```
fastapi-jwt-auth/
├── main.py            # Main application
├── auth.py            # Authentication utilities
├── models.py          # Data models and schemas
├── middleware.py      # Custom middleware
├── requirements.txt   # Dependencies
└── README.md          # Documentation
```

---

## 🧰 Installation

### 1. Clone the repository:
```bash
git clone https://github.com/mehtachandrashekhar/jwt-auth-fast-api
cd jwt-auth-fast-api
```

### 2. Create and activate a virtual environment:
```bash
# Linux/Mac
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
.env\Scriptsctivate
```

### 3. Install dependencies:
```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file:
```env
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## 🚦 Running the Server

```bash
uvicorn main:app --reload
```

The API will be available at: [http://localhost:8000](http://localhost:8000)

---

## 📖 API Documentation

- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🔌 API Endpoints

### 🔐 Authentication

**POST** `/token`  
_Obtain access token_

**Parameters (form-data):**
- `username`: johndoe  
- `password`: secret

---

### 👤 Users

**POST** `/users`  
_Create a new user_

**Request body (JSON):**
```json
{
  "username": "newuser",
  "email": "new@example.com",
  "full_name": "New User",
  "password": "secret"
}
```

**GET** `/users`  
_List all users (requires authentication)_

**GET** `/users/me`  
_Get current user details (requires authentication)_

---

## 🔍 Testing with Postman

### 1. Get Access Token:
- **Method**: POST  
- **URL**: `http://localhost:8000/token`  
- **Headers**:  
  `Content-Type: application/x-www-form-urlencoded`  
- **Body**:  
  ```
  username=johndoe
  password=secret
  ```

### 2. Access Protected Endpoints:
- Add header:  
  `Authorization: Bearer <your_token>`

---

## 👥 Default Users

| Username | Password | Status |
|----------|----------|--------|
| johndoe  | secret   | Active |
| alice    | secret   | Active |
| bob      | secret   | Active |

---

## ⚙️ Environment Variables

| Variable                     | Description         | Default |
|-----------------------------|---------------------|---------|
| `SECRET_KEY`                | JWT secret key      | -       |
| `ALGORITHM`                 | JWT algorithm       | HS256   |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Token expiry time | 30      |

---

## 📦 Dependencies

- `fastapi`
- `uvicorn`
- `python-jose[cryptography]`
- `passlib`
- `python-dotenv`

---

## 📄 License

**MIT License**

---

> This README includes:
> - Badges for visual appeal  
> - Clear feature list  
> - Complete installation instructions  
> - API documentation  
> - Postman testing guide  
> - Environment variables reference  
> - License information  

_You can customize it further by:_
- Adding deployment instructions  
- Including screenshots  
- Adding contribution guidelines  
- Adding links to related resources
