import { useState, useEffect } from "react";
import "./App.css";
import Header from "./components/Header.jsx";
import axios from "axios";
import Side from './components/Side.jsx'
import Cell from "./components/Cell.jsx";

function App() {
  const [hello, setHello] = useState();


  return (
    <>
      <Header/>
      <Side/>
      <div className="board">
        <Cell></Cell>
      </div>
    </>
  );
}

export default App;
