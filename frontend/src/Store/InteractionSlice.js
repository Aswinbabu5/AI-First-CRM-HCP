import { createSlice } from "@reduxjs/toolkit";

const initialState = {
    form: {
        hcp_id: "",
        interaction_type: "",
        interaction_date: "",
        interaction_time: "",
        attendees: "",
        topics_discussed: "",
        materials_shared: "",
        samples_distributed: "",
        sentiment: "",
        outcomes: "",
        follow_up_actions: "",
        summary: ""
    },

    hcps: [],

    messages: [],

    loading: false,

    error: null
};


const interactionSlice = createSlice({
    name: "interaction",

    initialState,

    reducers: {

        setFormField: (state, action) => {
            const { field, value } = action.payload;

            state.form[field] = value;
        },


        setFormData: (state, action) => {
            state.form = {
                ...state.form,
                ...action.payload
            };
        },


        setHcps: (state, action) => {
            state.hcps = action.payload;
        },


        addMessage: (state, action) => {
            state.messages.push(action.payload);
        },


        setLoading: (state, action) => {
            state.loading = action.payload;
        },


        setError: (state, action) => {
            state.error = action.payload;
        },


        resetForm: (state) => {
            state.form = {
                hcp_id: "",
                interaction_type: "",
                interaction_date: "",
                interaction_time: "",
                attendees: "",
                topics_discussed: "",
                materials_shared: "",
                samples_distributed: "",
                sentiment: "",
                outcomes: "",
                follow_up_actions: "",
                summary: ""
            };
        }
    }
});


export const {
    setFormField,
    setFormData,
    setHcps,
    addMessage,
    setLoading,
    setError,
    resetForm
} = interactionSlice.actions;


export default interactionSlice.reducer;