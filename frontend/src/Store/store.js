import { configureStore } from "@reduxjs/toolkit";

import interactionReducer from "./InteractionSlice";


export const store = configureStore({
    reducer: {
        interaction: interactionReducer
    }
});