import React from 'react'
import './InteractionForm.css'
import HcpSelect from '../HcpSelect'
import { Save, EventNote } from '@mui/icons-material'
import { useDispatch, useSelector } from "react-redux";
import { setFormField } from '../../Store/InteractionSlice';
import { createInteraction } from '../../Service/api';

const InteractionForm = () => {
  const dispatch = useDispatch();

  const form = useSelector((state) => state.interaction.form);

  const handleChange = (event) => {
    const { name, value } = event.target;

    dispatch(
      setFormField({
        field: name,
        value: value
      })
    );
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    if (
      !form.hcp_id ||
      !form.interaction_type ||
      !form.interaction_date
    ) {
      alert("Please fill all required fields");
      return;
    }

    try {
      const response = await createInteraction(form);

      alert("Interaction saved successfully");

      console.log(response.data);

    } catch (error) {
      console.error(error);

      alert(
        error.response?.data?.detail ||
        "Failed to save interaction"
      );
    }
  };

  return (
    <div className='form'>
      <h3>
        <span><EventNote /></span>
        Log HCP Interaction
      </h3>

      <form
        className="form_content"
        onSubmit={handleSubmit}
      >
        <HcpSelect />

        <h5>Interaction</h5>
        <select
          name="interaction_type"
          value={form.interaction_type}
          onChange={handleChange}
          className='customcolor'
          required
        >
          <option value="">Select Type</option>
          <option value="Meeting">Meeting</option>
          <option value="Call">Call</option>
          <option value="Email">Email</option>
          <option value="Conference">Conference</option>
        </select>

        <h5>Date</h5>
        <input
          type='date'
          name="interaction_date"
          value={form.interaction_date}
          onChange={handleChange}
          required
        />

        <h5>Time</h5>
        <input
          type='time'
          name="interaction_time"
          value={form.interaction_time}
          onChange={handleChange}
        />

        <h5>Attendees</h5>
        <input
          type='text'
          name="attendees"
          value={form.attendees}
          onChange={handleChange}
          placeholder='Attendees'
        />

        <h5>Topic Discussed</h5>
        <textarea
          name="topics_discussed"
          value={form.topics_discussed}
          onChange={handleChange}
        />

        <h5>Material Shared</h5>
        <input
          type='text'
          name="materials_shared"
          value={form.materials_shared}
          onChange={handleChange}
          placeholder='Material'
        />

        <h5>Samples Distributed</h5>
        <input
          type='text'
          name="samples_distributed"
          value={form.samples_distributed}
          onChange={handleChange}
          placeholder='Samples'
        />

        <h5>Sentiment</h5>
        <select
          name="sentiment"
          value={form.sentiment}
          onChange={handleChange}
          className='customcolor'
        >
          <option value="">Select Sentiment</option>
          <option value="Positive">Positive</option>
          <option value="Neutral">Neutral</option>
          <option value="Negative">Negative</option>
        </select>

        <h5>Outcome</h5>
        <textarea
          name="outcomes"
          value={form.outcomes}
          onChange={handleChange}
        />

        <h5>Follow-up</h5>
        <textarea
          name="follow_up_actions"
          value={form.follow_up_actions}
          onChange={handleChange}
        />

        <h5>Summary</h5>
        <textarea
          name="summary"
          value={form.summary}
          onChange={handleChange}
        />

        <br />

        <button type="submit">
          <span><Save /></span>
          Save Interaction
        </button>
      </form>
    </div>
  )
}

export default InteractionForm