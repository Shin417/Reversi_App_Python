import { useState, useEffect } from "react";
import "./App.css";
import Header from "./components/Header.jsx";
import axios from "axios";
import Side from './components/Side.jsx'
import Cell from "./components/Cell.jsx";

function App() {
  const [hello, setHello] = useState();

  const fetchAPI = async () => {
    const response = await axios.get("http://127.0.0.1:8080/");
    setHello(response.data);
  };

  useEffect(() => {
    fetchAPI();
  }, []);

  return (
    <>
      <Header/>
      <Side/>
      <div className="board">
        {Array.apply(null, {length: 64}).map((e, i) => {
          <Cell/>
        })}
      </div>
    </>
  );
}

export default App;
