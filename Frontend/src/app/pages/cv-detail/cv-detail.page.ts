import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { CvService } from '../../services/cv.service';
import { CvProfileComponent } from '../../components/cv-profile/cv-profile.component';
import { CvSkillsComponent } from '../../components/cv-skills.component';
import { CvLanguagesComponent } from '../../components/cv-languages.component';
import { CvEducationsComponent } from '../../components/cv-educations.component';
import { CvExperiencesComponent } from '../../components/cv-experiences.component';
import { CvProjectsComponent } from '../../components/cv-projects.component';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  imports: [CvProfileComponent, CvSkillsComponent, CvLanguagesComponent, CvEducationsComponent, CvEducationsComponent, CvExperiencesComponent, CvLanguagesComponent, CvProjectsComponent, FormsModule, CommonModule],
  selector: 'app-cv-detail',
  templateUrl: './cv-detail.page.html',
  styleUrls: ['./cv-detail.page.css']
})
export class CvDetailPage implements OnInit {
  cv: any = null;
  cvId = '';

  constructor(private route: ActivatedRoute, private cvService: CvService) {}

  ngOnInit(): void {
    this.cvId = this.route.snapshot.paramMap.get('cv_id')!;
    console.log(this.cvId);
    
    this.loadCV();
  }

  loadCV() { this.cvService.getCVDetail(this.cvId).subscribe(res => { if(res.status==='success') this.cv=res.cv; }); }
}
