import { useState, useEffect } from "react";
import "./App.css";
import Header from "./components/Header.jsx";
import axios from "axios";
import Cell from "./components/Cell.jsx";

function App() {

 const tempArray = Array(8).fill().map(() => Array(8).fill(0));
 
 
  return (
    <>
      <Header/>
      <section className="main-section">
        <div className="board">
          {tempArray.map((row, i) => (
            row.map((element, j) => (
              <Cell  key={" " + i + j} x={j} y={i}></Cell>
            ))
          ))}
        </div>
      </section>
    </>
  );
}

export default App;
