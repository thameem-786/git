import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import axios from 'axios'
import './LoginPage.css'

interface LoginPageProps {
  onLogin: () => void
}

function LoginPage({ onLogin }: LoginPageProps) {
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')
  const navigate = useNavigate()

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault()
    setLoading(true)
    setError('')

    try {
      const response = await axios.post('http://localhost:5000/api/auth/login', {
        username,
        password,
      })

      localStorage.setItem('token', response.data.token)
      onLogin()
      navigate('/')
    } catch (err: any) {
      setError(err.response?.data?.message || 'Login failed')
    } finally {
      setLoading(false)
    }
  }

  const handleDemoLogin = (demoUsername: string, demoPassword: string) => {
    setUsername(demoUsername)
    setPassword(demoPassword)
  }

  return (
    <div className="login-container">
      <div className="login-box">
        <div className="login-header">
          <h1>EdgeGuardian AI</h1>
          <p>Vehicle Health Monitoring & Predictive Maintenance</p>
        </div>

        <form onSubmit={handleLogin} className="login-form">
          <div className="form-group">
            <label htmlFor="username">Username</label>
            <input
              id="username"
              type="text"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              placeholder="Enter your username"
              required
            />
          </div>

          <div className="form-group">
            <label htmlFor="password">Password</label>
            <input
              id="password"
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeholder="Enter your password"
              required
            />
          </div>

          {error && <div className="error-message">{error}</div>}

          <button type="submit" disabled={loading} className="btn-login">
            {loading ? 'Signing in...' : 'Sign In'}
          </button>
        </form>

        <div className="demo-section">
          <p>Demo Credentials:</p>
          <div className="demo-buttons">
            <button
              onClick={() => handleDemoLogin('admin', 'admin123')}
              className="demo-btn"
            >
              Admin
            </button>
            <button
              onClick={() => handleDemoLogin('engineer', 'eng123')}
              className="demo-btn"
            >
              Engineer
            </button>
            <button
              onClick={() => handleDemoLogin('viewer', 'view123')}
              className="demo-btn"
            >
              Viewer
            </button>
          </div>
        </div>
      </div>
    </div>
  )
}

export default LoginPage
