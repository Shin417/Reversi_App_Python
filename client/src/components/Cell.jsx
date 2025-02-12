import axios from "axios";
import { useState, useEffect} from "react";
import Piece from './Piece';

export default function Cell(props) {
  const [color, setColor] = useState();



  const getInfo = async () => {
    const response = await axios.get("http://localhost:8080/");
    setColor(response.data)
  };

  useEffect(() => {
    getInfo();
  })

  return (
    <div className="cell" onClick={getInfo}>
      <Piece color={color}/>
    </div>
  );
}
