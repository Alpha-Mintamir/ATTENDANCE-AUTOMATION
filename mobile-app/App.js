import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import QRScanner from './src/screens/QRScanner';
import Home from './src/screens/Home';

const Stack = createStackNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Home">
        <Stack.Screen name="Home" component={Home} />
        <Stack.Screen name="QRScanner" component={QRScanner} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
