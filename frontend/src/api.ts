import axios from "axios"

const runtimeApiUrl = window.RUNTIME_CONFIG?.VITE_API_BASE_URL
const baseURL = import.meta.env.VITE_API_BASE_URL || runtimeApiUrl || window.location.origin

export const api = axios.create({
  baseURL,
})

