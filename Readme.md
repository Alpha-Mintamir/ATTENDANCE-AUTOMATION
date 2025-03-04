# University Attendance System - Mobile App

Created by Alpha Lencho ([@Alpha-Mintamir](https://github.com/Alpha-Mintamir))

Contact: Alphalencho4@gmail.com

A modern, secure, and automated attendance tracking system using QR codes, geofencing, and WiFi verification. This system prevents proxy attendance and provides real-time tracking for educational institutions.

## 🌟 Features

### Core Features
- QR Code-based attendance marking
- Geofencing verification
- WiFi network validation
- Real-time attendance tracking
- Automated reporting system
- Cross-platform mobile app (iOS & Android)

### Security Features
- Location-based verification
- Device binding
- Network validation
- Anti-proxy measures

## 🏗 System Architecture

```
university-attendance-system/
├── backend/                 # FastAPI Backend
│   ├── app/
│   ├── scripts/
│   └── requirements.txt
│
└── mobile-app/             # React Native Mobile App
    ├── src/
    ├── assets/
    └── package.json
```

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Node.js 14+
- PostgreSQL 13+
- Expo CLI
- Mobile device or emulator

### Backend Setup

1. Set up Python environment:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

2. Configure database:
```bash
# Create PostgreSQL database
createdb attendance_db

# Initialize database
python scripts/setup_db.py
```

3. Start the server:
```bash
uvicorn app.main:app --reload
```

### Mobile App Setup

1. Install dependencies:
```bash
cd mobile-app
npm install
```

2. Start the app:
```bash
npm start
```

## 📱 Mobile App Features

- QR code scanning
- Real-time location tracking
- WiFi network verification
- Offline support
- Push notifications
- Attendance history

## 🖥 Backend Features

- QR code generation
- Geofence validation
- Attendance tracking
- Report generation
- API documentation
- JWT authentication

## 💻 Technologies Used

### Backend
- FastAPI
- PostgreSQL
- SQLAlchemy
- Python QR Code

### Mobile App
- React Native
- Expo
- React Navigation
- NetInfo

## 📊 System Flow

1. Lecturer generates QR code
2. Students scan QR code
3. System verifies:
   - Location (Geofencing)
   - WiFi network
   - Device binding
4. Attendance is recorded
5. Reports are generated

## 🔒 Security Measures

- Geofencing validation
- WiFi network verification
- Device binding
- JWT authentication
- Rate limiting
- Input validation

## 📋 Documentation

### API Documentation
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### Mobile App
- Component documentation
- Screen navigation
- API integration

## 🛠 Development

### Backend Development
```bash
cd backend
uvicorn app.main:app --reload
```

### Mobile Development
```bash
cd mobile-app
npm start
```

## 🧪 Testing

### Backend Tests
```bash
cd backend
pytest
```

### Mobile App Tests
```bash
cd mobile-app
npm test
```

## 📦 Deployment

### Backend Deployment
```bash
docker-compose up --build
```

### Mobile App Deployment
```bash
# iOS
expo build:ios

# Android
expo build:android
```

## 🔧 Troubleshooting

### Common Issues

1. Database Connection
   - Check PostgreSQL service
   - Verify credentials
   - Check database existence

2. Mobile App
   - Camera permissions
   - Location services
   - Network connectivity

3. QR Code Scanning
   - Lighting conditions
   - Camera focus
   - QR code validity

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Submit Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 💡 Future Improvements

- Face recognition integration
- LMS integration
- Automated notifications
- Analytics dashboard
- Attendance patterns analysis

## 📞 Support

For support:
- Create GitHub issue
- Email: Alphalencho4@gmail.com
- Documentation: `/docs`
- GitHub: [@Alpha-Mintamir](https://github.com/Alpha-Mintamir)

## 🙏 Acknowledgments

- University IT Department
- Contributing developers
- Testing team
- User feedback

## 📈 Version History

- v1.0.0: Initial release
- v1.1.0: Added geofencing
- v1.2.0: Enhanced reporting
- v1.3.0: WiFi verification

## 🌐 Links

- [Backend Documentation](/backend/README.md)
- [Mobile App Documentation](/mobile-app/README.md)
- [API Documentation](http://localhost:8000/docs)
- [Deployment Guide](/docs/deployment.md)