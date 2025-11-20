import { CommonModule } from '@angular/common';
import { Component, Input } from '@angular/core';

@Component({
  imports: [CommonModule],
  selector: 'app-cv-projects',
  template: `<div class="projects"><h4>Projects</h4><ul><li *ngFor="let p of projects">{{p.title || p}} ({{p.role || ''}}) - {{p.technologies?.join(', ') || ''}}</li></ul></div>`,
  styles:[`.projects ul { padding-left:20px; } .projects li { margin:5px 0; }`]
})
export class CvProjectsComponent { @Input() projects: any[] = []; }
