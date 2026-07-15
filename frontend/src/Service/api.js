import axios from "axios";

const api = axios.create({
    baseURL: "http://127.0.0.1:8000",
    headers: {
        "Content-Type": "application/json"
    }
});


export const getHcps = () => {
    return api.get("/hcps");
};


export const createInteraction = (data) => {
    return api.post("/interactions", data);
};


export const getInteractions = () => {
    return api.get("/interactions");
};


export const updateInteraction = (id, data) => {
    return api.put(`/interactions/${id}`, data);
};


export const sendAgentMessage = (message) => {
    return api.post("/agent/chat", {
        message: message
    });
};


export default api;