import React, { useState, useEffect } from 'react';
import { StyleSheet, Text, View, Alert } from 'react-native';
import { Camera } from 'expo-camera';
import * as Location from 'expo-location';
import NetInfo from '@react-native-community/netinfo';
import { GeofenceCheck } from '../utils/GeofenceCheck';

export default function QRScanner() {
  const [hasPermission, setHasPermission] = useState(null);
  const [scanned, setScanned] = useState(false);

  useEffect(() => {
    (async () => {
      const { status } = await Camera.requestCameraPermissionsAsync();
      setHasPermission(status === 'granted');
    })();
  }, []);

  const checkGeofence = async (qrData, location) => {
    const { latitude, longitude } = location.coords;
    const { centerLat, centerLng, radius } = JSON.parse(qrData).geofence;
    
    return GeofenceCheck.isWithinGeofence(
      latitude,
      longitude,
      centerLat,
      centerLng,
      radius
    );
  };

  const handleBarCodeScanned = async ({ type, data }) => {
    setScanned(true);
    
    try {
      const location = await Location.getCurrentPositionAsync({});
      const netInfo = await NetInfo.fetch();
      
      // Check geofence
      const isInGeofence = await checkGeofence(data, location);
      if (!isInGeofence) {
        Alert.alert('Error', 'You must be inside the classroom to mark attendance');
        return;
      }
      
      // Verify attendance
      const response = await fetch('YOUR_API_URL/api/attendance/verify', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          qr_data: data,
          location: {
            latitude: location.coords.latitude,
            longitude: location.coords.longitude,
          },
          wifi_ssid: netInfo.details.ssid,
          timestamp: new Date().toISOString(),
        }),
      });

      const result = await response.json();
      Alert.alert('Success', 'Attendance marked successfully!');
    } catch (error) {
      Alert.alert('Error', error.message);
    }
  };

  if (hasPermission === null) {
    return <Text>Requesting camera permission...</Text>;
  }
  if (hasPermission === false) {
    return <Text>No access to camera</Text>;
  }

  return (
    <View style={styles.container}>
      <Camera
        style={styles.camera}
        onBarCodeScanned={scanned ? undefined : handleBarCodeScanned}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    flexDirection: 'column',
  },
  camera: {
    flex: 1,
  },
}); 