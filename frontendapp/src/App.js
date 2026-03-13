import logo from './logo.svg';
import './App.css';

import Home from './components/home';
import About from './components/About';
import Create from './components/Create';
import { Route, Routes } from 'react-router-dom';
import Services from './components/Services';
import Login from './components/login.js';
import Register from "./components/register.js"

import Navi from './components/Navbar.tsx'
import react from 'react';

function App() {
  return (
    <div className="App">
      
     <Navi/>
     <Routes>

          <Route path= "" element={<Home/>} />
          <Route path= "/aboutpage" element={<About/>} />
          <Route path="/createrecord" element={<Create/>} />
          <Route path="/services" element={<Services/>} />
          <Route path="/login" element={<Login/>} />
          <Route path="/register" element={<Register />} />
      </ Routes>
    </div>
  );
}

export default App;
