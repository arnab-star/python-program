import React from "react";
// import SchoolPortal from "./school-portal";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import LoginPage from "./login";

function App() {
  return (
    // <Router>
    //   <Routes>
    //     {/* <Route path="/" element={<SchoolPortal />} /> */}
    //     <LoginPage />
    //   </Routes>
    // </Router>
    <LoginPage />
    
  );
}

export default App;
    