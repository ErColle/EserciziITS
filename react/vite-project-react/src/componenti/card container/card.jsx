import React, {useState} from 'react';

const Card = () => {

const [textColor, setTextColor] = useState('#000000');
const [themeColor, setThemeColor] = useState('#ffffff');

const changeColor = () => {
  if (textColor === '#000000') {
    setTextColor('#ff0000');
  } else {
    setTextColor('#000000');
  }
};

const changeTheme = () => {
  if (themeColor === '#ffffff') {
    setThemeColor('#5e5e5eff');
  } else {
    setThemeColor('#ffffff');
  }
};




  return (
    <div onClick={changeTheme}
      style={{
        display: "flex",
        flexDirection: "column",
        margin: 10,
        width: 300,
        height: 400,
        borderRadius: 16,
        border: "1px solid #e5e7eb",
        backgroundColor: themeColor,
      }}
    >
      <div
        style={{
          height: 180,
          whidth:362,
          backgroundColor: "#f3f4f6",
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
        }}>
        362x180
      </div>

      <div style={{ padding: 20, flex: 1, textAlign:"left" }}>
        <h3>Card title</h3>
        <p style={ { color: textColor }}>
          Testo descrittivo della card
        </p>
      </div>
      </div>  
  );
};

export default Card;
