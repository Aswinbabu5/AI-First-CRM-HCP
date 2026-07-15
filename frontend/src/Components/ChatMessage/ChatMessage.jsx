import React from "react";
import "./ChatMessage.css";

const ChatMessage = ({ role, message }) => {
  return (
    <div className={`chat_message ${role}`}>
      <div className="message_bubble">
        {message}
      </div>
    </div>
  );
};

export default ChatMessage;