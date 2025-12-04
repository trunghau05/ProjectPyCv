import { Skill, Language, Education, Experience, Project } from './user.interface';

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