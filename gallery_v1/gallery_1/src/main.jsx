import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import Home from './components/screens/home/Home'
import './assets/styles/global.css'
// import styles from './main.module.css'


createRoot(document.getElementById('root')).render(
  <StrictMode>
    
      <Home />
     
    
    
  </StrictMode>,
)
