import { CommonModule } from '@angular/common';
import { Component, Input } from '@angular/core';

@Component({
  imports: [CommonModule],
  selector: 'app-cv-educations',
  template: `<div class="education"><h4>Education</h4><ul><li *ngFor="let e of educations">{{e.degree || e}} - {{e.school || ''}} ({{e.start_year || ''}} - {{e.end_year || ''}})</li></ul></div>`,
  styles:[`.education ul { padding-left:20px; } .education li { margin:5px 0; }`]
})
export class CvEducationsComponent { @Input() educations: any[] = []; }
