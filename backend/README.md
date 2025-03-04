# University Attendance System - Backend

Backend implementation for the University Attendance Automation System using FastAPI, PostgreSQL, and QR code-based verification with geofencing.

## Features

- QR Code generation for class sessions
- Geofencing verification
- WiFi-based location validation
- Attendance tracking and reporting
- JWT-based authentication
- PostgreSQL database integration

## Prerequisites

- Python 3.9+
- PostgreSQL 13+
- Virtual environment (recommended)

## Installation

1. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a PostgreSQL database:
```sql
CREATE DATABASE attendance_db;
```

4. Set up environment variables:
```bash
# Copy the example env file
cp .env.example .env

# Edit the .env file with your configurations
```

5. Initialize the database:
```bash
python scripts/setup_db.py
```

## Configuration

Create a `.env` file in the root directory with the following variables:

```ini
# Database Configuration
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=attendance_db

# JWT Configuration
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# WiFi Configuration
ALLOWED_WIFI_SSIDS=["UNIVERSITY_WIFI", "CAMPUS_WIFI"]

# Geofence Configuration
DEFAULT_GEOFENCE_RADIUS=50

# Server Configuration
HOST=0.0.0.0
PORT=8000
```

## Running the Application

1. Start the development server:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

2. Access the API documentation:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Project Structure

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   │   └── models.py
│   ├── services/
│   │   ├── attendance_service.py
│   │   ├── geofence_service.py
│   │   ├── qr_service.py
│   │   └── report_service.py
│   └── utils/
├── scripts/
│   └── setup_db.py
├── requirements.txt
├── Dockerfile
└── .env
```

## API Endpoints

### Authentication
- `POST /api/auth/login` - User login
- `POST /api/auth/register` - User registration

### Attendance
- `POST /api/attendance/verify` - Verify and record attendance
- `GET /api/attendance/history` - Get attendance history

### Class Management
- `POST /api/class/generate-qr` - Generate QR code for class
- `GET /api/class/sessions` - Get class sessions

### Reports
- `GET /api/reports/attendance` - Generate attendance reports

## Docker Support

1. Build the Docker image:
```bash
docker build -t attendance-backend .
```

2. Run the container:
```bash
docker run -p 8000:8000 attendance-backend
```

Or use docker-compose:
```bash
docker-compose up --build
```

## Development

### Adding New Models

1. Create model in `app/models/models.py`
2. Run database migrations:
```bash
python scripts/setup_db.py
```

### Creating New Services

1. Add new service file in `app/services/`
2. Import and use in relevant route handlers

## Testing

Run tests using pytest:
```bash
pytest
```

## Common Issues

1. Database Connection Issues:
   - Verify PostgreSQL is running
   - Check database credentials in .env
   - Ensure database exists

2. Migration Issues:
   - Delete existing tables if needed
   - Run setup_db.py again

3. Environment Variables:
   - Ensure all required variables are set
   - Check variable types match expected values

## Security Notes

- Always use HTTPS in production
- Keep SECRET_KEY secure and unique
- Implement rate limiting for production
- Regular security updates
- Proper input validation

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License

## Support

For support, please create an issue in the repository or contact the development team.

