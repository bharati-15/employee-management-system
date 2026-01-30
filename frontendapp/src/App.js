import logo from './logo.svg';
import './App.css';

import Home from './components/home';
import About from './components/About';
import Create from './components/Create';
import { Route, Routes } from 'react-router-dom';

function App() {
  return (
    <div className="App">
     <Routes>

          <Route path= "" element={<Home/>} />
          <Route path= "/aboutpage" element={<About/>} />
          <Route path="/createrecord" element={<Create/>} />
      </ Routes>
    </div>
  );
}

export default App;
