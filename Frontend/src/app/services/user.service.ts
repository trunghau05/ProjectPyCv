import axios from 'axios';
import { User } from '../interfaces/user.interface';

const API_URL = 'http://localhost:8000/users/';

export const UserService = {
  getAll: async (): Promise<User[]> => {
    const res = await axios.get(API_URL);
    return res.data;
  },

  getById: async (id: string): Promise<User> => {
    const res = await axios.get(`${API_URL}${id}/`);
    return res.data;
  },

  create: async (user: User): Promise<User> => {
    const res = await axios.post(API_URL, user);
    return res.data;
  },

  update: async (id: string, user: User): Promise<User> => {
    const res = await axios.put(`${API_URL}${id}/`, user);
    return res.data;
  },

  delete: async (id: string): Promise<void> => {
    await axios.delete(`${API_URL}${id}/`);
  }
};
