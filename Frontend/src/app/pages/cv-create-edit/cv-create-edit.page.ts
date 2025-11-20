import { Component, OnInit } from '@angular/core';
import { CvService } from '../../services/cv.service';
import { Router, ActivatedRoute } from '@angular/router';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  imports: [CommonModule, FormsModule],
  selector: 'app-cv-create-edit',
  templateUrl: './cv-create-edit.page.html',
  styleUrls: ['./cv-create-edit.page.css']
})
export class CvCreateEditPage implements OnInit {
  cvId: string | null = null;

  cv: any = {
    title: '',
    template_id: '',
    profile: { headline: '', phone: '', address: '', birthday: '', about_me: '' },
    skills: [''],
    languages: [''],
    educations: [''],
    experiences: [''],
    projects: ['']
  };

  constructor(private cvService: CvService, private router: Router, private route: ActivatedRoute) {}

  ngOnInit(): void {
    this.cvId = this.route.snapshot.paramMap.get('cv_id');
    if(this.cvId){
      this.cvService.getCVDetail(this.cvId).subscribe(res => {
        if(res.status === 'success') this.cv = res.cv;
      });
    }
  }

  // ====== Skills ======
  addSkill() { this.cv.skills.push(''); }
  removeSkill(i: number) { this.cv.skills.splice(i, 1); }

  // ====== Languages ======
  addLanguage() { this.cv.languages.push(''); }
  removeLanguage(i: number) { this.cv.languages.splice(i, 1); }

  // ====== Educations ======
  addEducation() { this.cv.educations.push(''); }
  removeEducation(i: number) { this.cv.educations.splice(i, 1); }

  // ====== Experiences ======
  addExperience() { this.cv.experiences.push(''); }
  removeExperience(i: number) { this.cv.experiences.splice(i, 1); }

  // ====== Projects ======
  addProject() { this.cv.projects.push(''); }
  removeProject(i: number) { this.cv.projects.splice(i, 1); }

  // ====== Submit ======
  onSubmit() {
    if(this.cvId){
      this.cvService.updateCV(this.cvId, this.cv).subscribe(() => this.router.navigate(['/cv-list']));
    } else {
      this.cvService.createCV(this.cv).subscribe(() => this.router.navigate(['/cv-list']));
    }
  }
}
