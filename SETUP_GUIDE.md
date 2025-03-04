# Setup Guide for University Attendance System

## Prerequisites Installation

1. Install Python (3.9+):
```bash
# Check Python version
python --version

# If not installed, download from https://www.python.org/downloads/
```

2. Install Node.js (14+):
```bash
# Check Node.js version
node --version

# If not installed, download from https://nodejs.org/
```

3. Install PostgreSQL (13+):
```bash
# For Ubuntu
sudo apt-get install postgresql postgresql-contrib

# For macOS using Homebrew
brew install postgresql

# For Windows, download from https://www.postgresql.org/download/windows/
```

4. Install Expo CLI:
```bash
npm install -g expo-cli
```

## Backend Setup

1. Clone the repository and navigate to backend:
```bash
git clone https://github.com/Alpha-Mintamir/university-attendance-system.git
cd university-attendance-system/backend
```

2. Create and activate virtual environment:
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# For Windows:
venv\Scripts\activate
# For macOS/Linux:
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up PostgreSQL database:
```bash
# Access PostgreSQL
psql -U postgres

# Create database
CREATE DATABASE attendance_db;

# Exit PostgreSQL
\q
```

5. Configure environment variables:
```bash
# Copy example env file
cp .env.example .env

# Edit .env file with your database credentials and other configurations
# Use any text editor to modify the .env file
```

6. Initialize the database:
```bash
python scripts/setup_db.py
```

7. Run the backend server:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Mobile App Setup

1. Navigate to mobile-app directory:
```bash
cd ../mobile-app
```

2. Install dependencies:
```bash
npm install
```

3. Configure environment:
```bash
# Copy example env file
cp .env.example .env

# Edit .env file - set your backend URL
# API_URL should point to your backend server
# Example: API_URL=http://192.168.1.100:8000
```

4. Start the mobile app:
```bash
npm start
```

## Testing the System

1. Backend Testing:
```bash
# In backend directory
pytest
```

2. Mobile App Testing:
```bash
# In mobile-app directory
npm test
```

## Verifying the Setup

1. Backend Verification:
- Open browser and visit: http://localhost:8000/docs
- You should see the Swagger UI documentation

2. Mobile App Verification:
- Scan the QR code with Expo Go app
- Or run on simulator:
  ```bash
  # For iOS
  npm run ios
  
  # For Android
  npm run android
  ```

## Common Issues and Solutions

1. Database Connection Issues:
```bash
# Check PostgreSQL service status
# For Ubuntu/macOS:
sudo service postgresql status
# For Windows:
net start postgresql

# Verify database exists
psql -U postgres -l
```

2. Mobile App Network Issues:
- Ensure backend URL in .env is correct
- Check if backend server is running
- Verify network connectivity

3. Permission Issues:
```bash
# For camera access issues
# Check app permissions in device settings

# For location services
# Enable location services in device settings
```

## Running in Development Mode

1. Backend Development:
```bash
# Run with auto-reload
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

2. Mobile App Development:
```bash
# Run with development server
npm start

# In separate terminal for iOS
npm run ios

# Or for Android
npm run android
```

## Additional Notes

- Keep both backend server and Expo development server running
- Use real device for testing geofencing features
- Ensure proper WiFi connection for network verification
- Check camera permissions for QR scanning

For any issues, contact:
- Email: Alphalencho4@gmail.com
- GitHub: [@Alpha-Mintamir](https://github.com/Alpha-Mintamir) 