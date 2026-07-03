import { useState, useEffect } from 'react'
import axios from 'axios'
import { DashboardData } from '../types'
import './DashboardPage.css'

function DashboardPage() {
  const [dashboard, setDashboard] = useState<DashboardData | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')

  useEffect(() => {
    const fetchDashboard = async () => {
      try {
        const token = localStorage.getItem('token')
        const response = await axios.get(
          'http://localhost:5000/api/dashboard',
          {
            headers: { Authorization: `Bearer ${token}` },
          }
        )
        setDashboard(response.data)
      } catch (err: any) {
        setError('Failed to load dashboard')
        console.error(err)
      } finally {
        setLoading(false)
      }
    }

    fetchDashboard()
    const interval = setInterval(fetchDashboard, 5000)
    return () => clearInterval(interval)
  }, [])

  if (loading) return <div className="dashboard-loading">Loading...</div>
  if (error) return <div className="dashboard-error">{error}</div>
  if (!dashboard) return <div>No data available</div>

  return (
    <div className="dashboard-container">
      <div className="dashboard-header">
        <h1>Vehicle Dashboard</h1>
        <p>{dashboard.vehicle.make} {dashboard.vehicle.model} ({dashboard.vehicle.year})</p>
      </div>

      <div className="dashboard-grid">
        <div className="card health-card">
          <h3>Health Score</h3>
          <div className="health-score">{dashboard.health_score}%</div>
          <p>Vehicle is operating normally</p>
        </div>

        <div className="card system-card">
          <h3>Engine</h3>
          <p className="status-{dashboard.system_status.engine}">
            {dashboard.system_status.engine}
          </p>
        </div>

        <div className="card system-card">
          <h3>Battery</h3>
          <p className="status-{dashboard.system_status.battery}">
            {dashboard.system_status.battery}
          </p>
        </div>

        <div className="card system-card">
          <h3>Brakes</h3>
          <p className="status-{dashboard.system_status.brakes}">
            {dashboard.system_status.brakes}
          </p>
        </div>

        <div className="card system-card">
          <h3>Tyres</h3>
          <p className="status-{dashboard.system_status.tyres}">
            {dashboard.system_status.tyres}
          </p>
        </div>
      </div>

      <div className="alerts-section">
        <h2>Recent Alerts</h2>
        {dashboard.recent_alerts.length > 0 ? (
          <div className="alerts-list">
            {dashboard.recent_alerts.map((alert) => (
              <div key={alert.id} className={`alert alert-${alert.severity}`}>
                <p>{alert.message}</p>
                <small>{new Date(alert.timestamp).toLocaleString()}</small>
              </div>
            ))}
          </div>
        ) : (
          <p>No alerts</p>
        )}
      </div>
    </div>
  )
}

export default DashboardPage
