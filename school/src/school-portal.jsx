import React from "react";
import "./school-portal.css";

const SchoolPortal = () => {
  return (
    <div className="school-portal">
      <div className="school-container">
        <h1 className="app-title">Welcome to School Portal</h1>

        <div className="button-submit">
          <Link to="/login" className="button-login">Login</Link>
        </div>

        <div className="button-submit">
          <Link to="/signup" className="button-login">Sign Up for Free</Link>
        </div>
      </div>
    </div>
  );
};

export default SchoolPortal;
