import { CommonModule } from '@angular/common';
import { Component, Input } from '@angular/core';

@Component({
  imports: [CommonModule],
  selector: 'app-cv-experiences',
  template: `<div class="experience"><h4>Experience</h4><ul><li *ngFor="let ex of experiences">{{ex.position || ex}} @ {{ex.company || ''}} ({{ex.start_date || ''}} - {{ex.end_date || ''}})</li></ul></div>`,
  styles:[`.experience ul { padding-left:20px; } .experience li { margin:5px 0; }`]
})
export class CvExperiencesComponent { @Input() experiences: any[] = []; }
