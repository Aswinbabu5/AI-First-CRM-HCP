import React, { useState } from "react";
import "./ChatForm.css";

import { Send } from "@mui/icons-material";
import { useDispatch, useSelector } from "react-redux";

import {
  addMessage,
  setFormData,
  setError
} from "../../Store/InteractionSlice";

import { sendAgentMessage } from "../../Service/api";

const ChatForm = () => {
  const dispatch = useDispatch();

  const [input, setInput] = useState("");
  const [chatLoading, setChatLoading] = useState(false);

  const messages = useSelector(
    (state) => state.interaction.messages
  );

  const handleSend = async () => {
    const message = input.trim();

    if (!message || chatLoading) {
      return;
    }

    dispatch(
      addMessage({
        role: "user",
        message: message
      })
    );

    setInput("");
    setChatLoading(true);

    try {
      dispatch(setError(null));

      const response = await sendAgentMessage(message);

      const responseData = response.data;

      dispatch(
        addMessage({
          role: "assistant",
          message: responseData.message
        })
      );

      if (
        responseData.tool_used === "log_interaction" &&
        responseData.data &&
        responseData.data.success
      ) {
        dispatch(
          setFormData({
            hcp_id: responseData.data.hcp_id ?? "",
            interaction_type:
              responseData.data.interaction_type ?? "",
            interaction_date:
              responseData.data.interaction_date ?? "",
            interaction_time:
              responseData.data.interaction_time ?? "",
            attendees:
              responseData.data.attendees ?? "",
            topics_discussed:
              responseData.data.topics_discussed ?? "",
            materials_shared:
              responseData.data.materials_shared ?? "",
            samples_distributed:
              responseData.data.samples_distributed ?? "",
            sentiment:
              responseData.data.sentiment ?? "",
            outcomes:
              responseData.data.outcomes ?? "",
            follow_up_actions:
              responseData.data.follow_up_actions ?? "",
            summary:
              responseData.data.summary ?? ""
          })
        );
      }

    } catch (error) {
      console.error(error);

      const errorMessage =
        error.response?.data?.detail ||
        "Failed to communicate with AI assistant";

      dispatch(setError(errorMessage));

      dispatch(
        addMessage({
          role: "assistant",
          message: errorMessage
        })
      );

    } finally {
      setChatLoading(false);
    }
  };

  const handleKeyDown = (event) => {
    if (
      event.key === "Enter" &&
      !event.shiftKey
    ) {
      event.preventDefault();
      handleSend();
    }
  };

  return (
    <div className="chat_panel">

      <div className="chat_header">
        <h3>AI Assistant</h3>

        <p>
          Log, edit and manage HCP interactions using natural language.
        </p>
      </div>

      <div className="chat_messages">

        {messages.length === 0 && (
          <div className="assistant_message">
            Hi! Tell me about your HCP interaction and I can help you log it.
          </div>
        )}

        {messages.map((item, index) => (
          <div
            key={index}
            className={
              item.role === "user"
                ? "user_message"
                : "assistant_message"
            }
          >
            {item.message}
          </div>
        ))}

        {chatLoading && (
          <div className="assistant_message">
            Thinking...
          </div>
        )}

      </div>

      <div className="chat_input_container">

        <textarea
          value={input}
          onChange={(event) =>
            setInput(event.target.value)
          }
          onKeyDown={handleKeyDown}
          placeholder="Type your message..."
        />

        <button
          type="button"
          onClick={handleSend}
          disabled={
            chatLoading ||
            !input.trim()
          }
        >
          <Send />
        </button>

      </div>

    </div>
  );
};

export default ChatForm;