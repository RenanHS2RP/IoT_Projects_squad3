import React from "react";
import { Tabs } from "expo-router";
import Colors from "../../constants/Colors";
import { MaterialIcons } from "@expo/vector-icons";
import { useNavigation } from "@react-navigation/native";

export default function TabLayout() {
  const navigation = useNavigation();

  return (
    <Tabs
      screenOptions={{
        tabBarActiveTintColor: Colors.light.tint,
      }}
    >
      <Tabs.Screen
        name="index"
        options={{
          title: "Sensor",
          tabBarIcon: ({ color }) => (
            <MaterialIcons name="wifi-tethering" size={24} color="black" />
          ),
          headerTitle: "Verifica Combustível",
        }}
      />
      <Tabs.Screen
        name="dashboard"
        options={{
          title: "Dashboard",
          tabBarIcon: ({ color }) => (
            <MaterialIcons name="dashboard" size={24} color="black" />
          ),
          headerTitle: "Verifica Combustível",
        }}
      />
    </Tabs>
  );
}
