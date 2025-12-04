import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { MatIconModule } from '@angular/material/icon';
import { CvBasic } from '../../components/cv-basic/cv-basic';
import { UserService } from '../../services/user.service';
import { User } from '../../interfaces/user.interface';

@Component({
  selector: 'app-home',
  imports: [CommonModule, FormsModule, MatIconModule, CvBasic],
  templateUrl: './home.html',
  styleUrl: './home.scss',
})
export class Home implements OnInit {
  users: User[] = [];
  user = {} as User

  downloadPDF() {
    window.print();
  }

  async ngOnInit() {
    this.load();
  }

  async load() {
    const usId = '693162f564652b56afa5d29c';
    sessionStorage.setItem('us_id', usId);
    
    this.user = await UserService.getById(usId);
    console.log(this.user);
  }

  async update() {
    try {
      const response = await UserService.update(this.user._id || '', this.user);
      alert("Cập nhật thành công!")
      this.load();
    } catch (error) {
      console.error(error);
    }
  }

  addSkill() {
    this.user.skills?.push({ name: '', level: 0 });
  }

  removeSkill(index: number) {
    this.user.skills?.splice(index, 1);
  }

  addLanguage() {
    this.user.languages?.push({ name: '', level: '' });
  }

  removeLanguage(index: number) {
    this.user.languages?.splice(index, 1);
  }

  // ===== EDUCATIONS =====
  addEducation() {
    this.user.educations?.push({ school: '', branch: '', start_year: 0, end_year: 0 });
  }

  removeEducation(index: number) {
    this.user.educations?.splice(index, 1);
  }

  // ===== EXPERIENCES =====
  addExperience() {
    this.user.experiences?.push({ company: '', position: '', start_date: '', end_date: '', description: '' });
  }

  removeExperience(index: number) {
    this.user.experiences?.splice(index, 1);
  }

  // ===== PROJECTS =====
  addProject() {
    this.user.projects?.push({ title: '', role: '', description: '' });
  }

  removeProject(index: number) {
    this.user.projects?.splice(index, 1);
  }
}
