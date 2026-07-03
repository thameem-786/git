import { useNavigate } from 'react-router-dom'
import './TopNav.css'

interface TopNavProps {
  onLogout: () => void
}

function TopNav({ onLogout }: TopNavProps) {
  const navigate = useNavigate()

  const handleLogout = () => {
    onLogout()
    navigate('/login')
  }

  return (
    <div className="top-nav">
      <div className="nav-left">
        <h1>Vehicle Monitoring System</h1>
      </div>
      <div className="nav-right">
        <button onClick={handleLogout} className="btn-logout">
          Logout
        </button>
      </div>
    </div>
  )
}

export default TopNav
