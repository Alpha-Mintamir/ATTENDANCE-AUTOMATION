# University Attendance System - Mobile App

React Native mobile application for the University Attendance Automation System with QR code scanning, geofencing, and WiFi verification capabilities.

## Features

- QR Code scanning for attendance
- Geofencing validation
- WiFi network verification
- Real-time attendance marking
- Cross-platform (iOS & Android)
- Offline support
- Push notifications

## Prerequisites

- Node.js 14+
- npm or yarn
- Expo CLI
- iOS Simulator (for iOS development)
- Android Studio & SDK (for Android development)

## Installation

1. Install dependencies:
```bash
npm install
# or
yarn install
```

2. Configure environment:
```bash
# Copy the example env file
cp .env.example .env

# Edit .env with your configuration
```

3. Install Expo CLI globally:
```bash
npm install -g expo-cli
```

## Configuration

Create a `.env` file in the root directory with:

```ini
API_URL=http://your-backend-url:8000
WIFI_SSID=UNIVERSITY_WIFI
```

## Running the App

1. Start the development server:
```bash
npm start
# or
yarn start
```

2. Run on specific platform:
```bash
# For iOS
npm run ios
# or
yarn ios

# For Android
npm run android
# or
yarn android
```

## Project Structure

```
mobile-app/
├── src/
│   ├── components/
│   │   ├── QRScanner.js
│   │   └── GeofenceCheck.js
│   ├── screens/
│   │   ├── Home.js
│   │   ├── Login.js
│   │   └── AttendanceHistory.js
│   ├── services/
│   │   └── api.js
│   └── utils/
│       └── geofencing.js
├── assets/
├── App.js
├── package.json
└── .env
```

## Available Scripts

- `npm start` - Start the Expo development server
- `npm run ios` - Run on iOS simulator
- `npm run android` - Run on Android emulator
- `npm run web` - Run in web browser
- `npm run test` - Run tests
- `npm run eject` - Eject from Expo

## Features Documentation

### QR Code Scanner
- Uses device camera to scan QR codes
- Validates QR code format
- Real-time scanning feedback

### Geofencing
- Validates user location against class coordinates
- Configurable radius settings
- Background location updates

### WiFi Verification
- Checks connection to university network
- SSID validation
- Network strength monitoring

## Development Guide

### Adding New Screens

1. Create screen component in `src/screens/`
2. Add to navigation stack in `App.js`
3. Update navigation types if using TypeScript

### Styling Guidelines

- Use React Native's StyleSheet
- Follow component-based styling
- Maintain consistent theme variables

## Testing

```bash
# Run all tests
npm test

# Run with coverage
npm test -- --coverage
```

## Building for Production

### iOS Build
```bash
expo build:ios
```

### Android Build
```bash
expo build:android
```

## Troubleshooting

### Common Issues

1. QR Scanner Issues:
   - Check camera permissions
   - Verify adequate lighting
   - Update Expo Camera package

2. Location Services:
   - Enable device location
   - Grant app permissions
   - Check GPS accuracy

3. Network Issues:
   - Verify backend URL in .env
   - Check WiFi connection
   - Validate API endpoints

## Performance Optimization

- Enable Hermes Engine
- Implement proper memo-ization
- Optimize image assets
- Use proper list rendering

## Security Best Practices

- Secure storage for tokens
- Certificate pinning
- Input validation
- Regular dependency updates

## Contributing

1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create Pull Request

## Code Style

- Follow ESLint configuration
- Use Prettier for formatting
- Follow React Native best practices
- Document complex logic

## Dependencies

Core:
- react-native
- expo
- @react-navigation/native
- @react-native-community/netinfo

Development:
- typescript
- jest
- @testing-library/react-native