# EdgeGuardian AI — Vehicle Health Monitoring & Predictive Maintenance

Real-Time Vehicle Health Monitoring & Predictive Maintenance using Edge AI.

## Overview

A production-ready automotive web application featuring a React 19 dashboard, Flask backend with WebSocket support, SQLite database, Raspberry Pi sensor integration, and TensorFlow Lite AI predictions — all working offline.

## Quick Start

### Prerequisites
- Node.js 18+
- Python 3.9+
- SQLite3
- pip

### Installation

```bash
# Frontend
cd frontend
npm install
npm run dev

# Backend (in another terminal)
cd backend
pip install -r requirements.txt
python run.py
```

### Demo Credentials
- **Admin**: `admin` / `admin123`
- **Engineer**: `engineer` / `eng123`
- **Viewer**: `viewer` / `view123`

## Technology Stack

| Layer | Technologies |
|-------|-------------|
| **Frontend** | React 19, Vite, TypeScript, Material UI, Tailwind CSS, Framer Motion, Chart.js |
| **Backend** | Python, Flask, Flask-RESTful, Flask-SocketIO, SQLAlchemy |
| **Database** | SQLite (dev) / MySQL (prod) |
| **Edge Device** | Raspberry Pi 4, GPIO, OBD-II (ELM327) |
| **AI** | TensorFlow Lite |
| **Communication** | WebSocket, REST API |

## Project Structure

```
edgeguardian-ai/
├── frontend/          # React 19 + Vite + TypeScript
├── backend/           # Flask REST API + SocketIO
├── raspberry_pi/      # Sensor reading scripts
├── ai_model/          # TensorFlow Lite model + training
├── database/          # SQLite DB + migrations
└── docs/              # Documentation
```

## Features

- ✅ Real-time sensor monitoring (temperature, voltage, vibration, etc.)
- ✅ OBD-II diagnostics (DTC codes, live parameters)
- ✅ AI-powered predictive maintenance
- ✅ WebSocket live updates
- ✅ Dark automotive theme
- ✅ Role-based access control (Admin, Engineer, Viewer)
- ✅ Offline capability
- ✅ PDF/CSV report generation
- ✅ Responsive design (desktop, tablet, mobile)

## API Documentation

See `docs/API.md` for complete REST API and WebSocket documentation.

## License

MIT
