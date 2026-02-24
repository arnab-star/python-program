import Homepage from "./Pages/Homepage";
import { Routes, Route } from "react-router-dom";
// import LoginPage from "./login";

function App() {
  return (
    <Routes>
      <Route path="/" element={<Homepage />} />
      {/* <Route path="/login" element={<LoginPage />} /> */}
    </Routes>
  );
}

export default App;