export interface Skill {
  sk_id?: string;
  name: string;
  level: number;
}

export interface Language {
  lg_id?: string;
  name: string;
  level: string;
}

export interface Education {
  ed_id?: string;
  school: string;
  branch?: string;
  start_year?: number;
  end_year?: number;
}

export interface Experience {
  ex_id?: string;
  company: string;
  position: string;
  description?: string;
  start_date?: string;
  end_date?: string;
}

export interface Project {
  pj_id?: string;
  title: string;
  role?: string;
  description?: string;
  technologies?: string[];
}

export interface User {
  _id?: string;
  name: string;
  img?: string;
  role?: string;
  email: string;
  phone?: string;
  birth?: string;
  address?: string;
  about?: string;
  skills?: Skill[];
  languages?: Language[];
  educations?: Education[];
  experiences?: Experience[];
  projects?: Project[];
}
