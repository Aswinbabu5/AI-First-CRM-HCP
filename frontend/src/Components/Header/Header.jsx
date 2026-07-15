import React from 'react'
import './Header.css'
import { LocalHospital } from '@mui/icons-material'

const Header = () => {
  return (
    <div className='header'>
      <div className='top_header'>
        <section className='left_content'>
          <LocalHospital />
        </section>
        <section className='right_content'>
          <h3>AI-First CRM</h3>
          <h4>HCP Interaction Management</h4>
        </section>
      </div>
      <section className='top_right_logo'>
        <h4>AI</h4>
      </section>
    </div>
  )
}

export default Header