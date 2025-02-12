import axios from "axios";
import { useState } from "react";
import blank from '../assets/blank.png';
import black from '../assets/black.png';
import white from '../assets/white.png';

export default function Cell(props) {
  const [side, setSide] = useState();
  const [color, setColor] = useState();

  const getInfo = async () => {
    const response = await axios.get("http://localhost:8080/");
    setSide(response.data)
  };

  const setImg = () => {
    if(side == 1){
        setColor(black);
    } else if(side == -1){
        setColor(white);
    } else {
        setColor(blank);
    }
  }

  return (
    <div className="cell" onClick={getInfo}>
      <h1>{side}</h1>
    </div>
  );
}
