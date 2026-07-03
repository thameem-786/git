import { Link } from 'react-router-dom'
import './Sidebar.css'

function Sidebar() {
  return (
    <aside className="sidebar">
      <div className="sidebar-header">
        <h2>EdgeGuardian</h2>
      </div>
      <nav className="sidebar-nav">
        <Link to="/" className="nav-item">
          Dashboard
        </Link>
        <Link to="/sensors" className="nav-item">
          Sensors
        </Link>
        <Link to="/obd" className="nav-item">
          OBD Diagnostics
        </Link>
        <Link to="/prediction" className="nav-item">
          AI Predictions
        </Link>
        <Link to="/maintenance" className="nav-item">
          Maintenance
        </Link>
        <Link to="/reports" className="nav-item">
          Reports
        </Link>
        <Link to="/settings" className="nav-item">
          Settings
        </Link>
      </nav>
    </aside>
  )
}

export default Sidebar
