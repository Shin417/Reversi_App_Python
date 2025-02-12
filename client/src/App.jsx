import { useState, useEffect } from "react";
import "./App.css";
import Header from "./components/Header.jsx";
import axios from "axios";
import Side from './components/Side.jsx'

function App() {
  const fetchAPI = async () => {
    const response = await axios.get("http://127.0.0.1:8080/");
  };

  useEffect(() => {}, []);

  return (
    <>
      <Header/>
      <Side/>
    </>
  );
}

export default App;
