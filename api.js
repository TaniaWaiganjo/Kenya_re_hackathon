import axios from 'axios';

//Change to whatever the server ip address is
const api = axios.create({
    baseURL: "http://localhost:8000"
});

// Export the Axios instance
export default api;