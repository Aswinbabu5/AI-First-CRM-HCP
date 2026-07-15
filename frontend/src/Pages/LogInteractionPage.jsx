import React from 'react'
import './LogInteractionPage.css'
import Header from '../Components/Header/Header'
import InteractionForm from '../Components/InteractionForm/InteractionForm'
import ChatForm from '../Components/ChatForm/ChatForm'

const LogInteractionPage = () => {
  return (
    <div>
      <Header />
      <main className='two_box'>
        <section className='left_box'>
          <InteractionForm />
        </section>
        <section className='right_box'>
          <ChatForm />
        </section>
      </main>
    </div>
  )
}

export default LogInteractionPage