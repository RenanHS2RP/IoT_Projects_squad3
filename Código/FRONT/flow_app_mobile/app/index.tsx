import React, { useEffect } from 'react';
import { View, Text, Image, StyleSheet } from 'react-native';
import { router } from 'expo-router';

const IntroScreen: React.FC = () => {

  useEffect(() => {
    const timer = setTimeout(() => {
      router.replace('./(tabs)');
    
    }, 2000);

    // Limpar o timer ao desmontar o componente
    return () => clearTimeout(timer);
  }, []);

  return (
    <View style={styles.container}>
      {/* Adicione seu logo aqui */}
      <Image source={require('../assets/images/logo.png')} style={styles.logo} />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: "#f2f2f2"
  },
  logo: {
    width: 330,
    height: 330,
    marginBottom: 16,
  },
});

export default IntroScreen;


