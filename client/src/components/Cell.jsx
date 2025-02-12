import axios from "axios";
import { useState } from "react";

export default function Cell(props) {
  const [side, setSide] = useState();

  const getInfo = async () => {
    const response = await axios.get("http://127.0.0.1:8080/");
    setSide(response.data);
  };

  return (
    <div className="cell" onClick={getInfo}>
      <img src="" alt="" />
    </div>
  );
}
