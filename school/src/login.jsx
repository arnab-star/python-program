import './Login.css'; // Assuming your CSS is in Login.css

function LoginPage() {
  return (
    <div className="login-page">
      <div className="login-container">
        <h1>Login</h1>
        <input type="email" placeholder="Email address" />
        <input type="password" placeholder="Enter your password" />
        <button className="btn-primary">Continue</button>
        <div className="signup-text">
          Don't have an account? <a href="/signup">Sign up</a>
        </div>
        <div className="separator">
          <span></span>
          <span>or</span>
          <span></span>
        </div>
        <button className="btn-google">Continue with Google</button>
      </div>
    </div>
  );
}
export default LoginPage;
