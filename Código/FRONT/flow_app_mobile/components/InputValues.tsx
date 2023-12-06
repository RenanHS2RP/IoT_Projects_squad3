import { StyleSheet, Text, View, TextInput, ImageStyle, TouchableWithoutFeedback, Keyboard } from 'react-native'
import React from 'react'
import CustomImage from './Image'

interface InputValuesProp{
  
    text: string,
    imagePath: string,
    style?: ImageStyle,
    onChange: (value:number) => void
}

  const handleDismissKeyboard = () => {
    Keyboard.dismiss();
  };


export default function InputValues({text, imagePath, style}: InputValuesProp) {
  

  return (
    <View style={styles.wrapper}>
      <Text style={styles.text}>{text}</Text>
      <View style={styles.container}>
        <CustomImage imagePath={imagePath} style={style}/>

          <TouchableWithoutFeedback onPress={handleDismissKeyboard}>
            <View style={styles.container}>
              <TextInput
                keyboardType='numeric'
                style={styles.input}
                returnKeyType='done'
              />
            </View>
          </TouchableWithoutFeedback>
        </View>
    </View>
  )
}

const styles = StyleSheet.create({
  wrapper: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center'
  },
  container: {
      textAlign:"center",
      flexDirection: 'column',
      justifyContent: 'center',
      alignSelf: 'center',
  },
  text: {
      color: '#000',
      fontSize: 22,
      textAlign: 'center',
      display: 'flex',
      flexDirection:'row',
      paddingLeft:5,
      paddingRight: 5,
      margin:0,
      paddingBottom:0,
      paddingTop:0
  },
  input: {
    textAlign: 'center',
    textAlignVertical: 'center',
    width: 180,
    height: 100,
    borderRadius: 15,
    fontSize: 30,
    fontWeight: '700',
    backgroundColor: '#fff'
  },
  image: {
    width: 17,
    height: 30
  },

})