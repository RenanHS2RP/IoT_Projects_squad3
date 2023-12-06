import { ViewStyle, TextStyle, ImageStyle, Image } from 'react-native';
import React from 'react';

interface ImageProps {
  imagePath: string; 
  style?: ImageStyle;
}

export default function CustomImage({ imagePath, style }: ImageProps){
  return <Image source={{uri: imagePath}} style={style} />;
};


