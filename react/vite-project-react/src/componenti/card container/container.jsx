import React from 'react';
import Card from './card';

const Container = () => {
  return (
    <div style={{display: "flex"}}>
        <Card></Card>
        <Card></Card>
        <Card></Card>
    </div>
  );
};

export default Container;