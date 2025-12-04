import axios from 'axios';
import { environment } from '../../enviroment/enviroment';
import { User, Skill, Language, Education, Experience, Project } from '../interfaces/user.interface';

const API_URL = `${environment.apiUrl}/cvs/`;

export interface Cv {
  _id?: string;
  user_id: string;
  title: string;
  skills?: Skill[];
  languages?: Language[];
  educations?: Education[];
  experiences?: Experience[];
  projects?: Project[];
  created_at?: string;
}

export const CvService = {
  getAll: async (): Promise<Cv[]> => {
    const res = await axios.get(API_URL);
    return res.data;
  },

  getById: async (id: string): Promise<Cv> => {
    const res = await axios.get(`${API_URL}${id}/`);
    return res.data;
  },

  create: async (cv: Cv): Promise<Cv> => {
    const res = await axios.post(API_URL, cv);
    return res.data;
  },

  update: async (id: string, cv: Cv): Promise<Cv> => {
    const res = await axios.put(`${API_URL}${id}/`, cv);
    return res.data;
  },

  delete: async (id: string): Promise<void> => {
    await axios.delete(`${API_URL}${id}/`);
  }
};
