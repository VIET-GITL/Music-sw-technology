import axios from 'axios';

const apiService = axios.create({
    baseURL: 'http://localhost:8000/auth/',
    headers: {
        'Content-Type': 'application/json',
        'X-Requested-With': 'XMLHttpRequest' 
    },
});

const authService = {
    register: async (username, email, password) => {
        try {
            const response = await apiService.post('register/', {
                username,
                email,
                password,
            });
            if (response.data.token) {
                localStorage.setItem('token', response.data.token);
            }
            return response.data;
        } catch (error) {
            console.error('Registration error:', error.response ? error.response.data : error.message);
            throw error;
        }
    },
    login: async ( email, password) => {
        try {
            const response = await apiService.post('login/', {
                email,
                password,
            });
            if (response.data.token) {
                localStorage.setItem('token', response.data.token);
            }
            return response.data;
        } catch (error) {
            console.error('Login error:', error.response ? error.response.data : error.message);
            throw error;
        }
    },
    logout: () => {
        localStorage.removeItem('token');
    },
    getToken: () => {
        return localStorage.getItem('token');
    }
};

export default authService;