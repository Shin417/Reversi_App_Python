import axios from "axios";
import { useState, useEffect } from "react";
import Piece from "./Piece";

export default function Cell(props) {
  const [color, setColor] = useState();
  const x = props.x;
  const y = props.y;

  const getInfo = async () => {
    const response = await axios.get("http://localhost:8080/");
    setColor(response.data);
  };

  useEffect(() => {
    getInfo();
  });
  
  return (
    <div className="cell" x={props} y={props} onClick={getInfo}>
      <Piece color={color} />
    </div>
  );
}
