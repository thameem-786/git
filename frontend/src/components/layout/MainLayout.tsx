import { Outlet } from 'react-router-dom'
import Sidebar from './Sidebar'
import TopNav from './TopNav'
import './MainLayout.css'

interface MainLayoutProps {
  onLogout: () => void
}

function MainLayout({ onLogout }: MainLayoutProps) {
  return (
    <div className="main-layout">
      <Sidebar />
      <div className="layout-content">
        <TopNav onLogout={onLogout} />
        <main className="layout-main">
          <Outlet />
        </main>
      </div>
    </div>
  )
}

export default MainLayout
