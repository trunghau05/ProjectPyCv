import { CommonModule } from '@angular/common';
import { Component, Input } from '@angular/core';

@Component({
  imports: [CommonModule],
  selector: 'app-cv-skills',
  template: `<div class="skills"><span class="chip" *ngFor="let s of skills">{{s.name || s}}</span></div>`,
  styles:[`.skills { display:flex; flex-wrap:wrap; gap:5px; } .chip { background:#1976d2; color:#fff; padding:5px 10px; border-radius:20px; }`]
})
export class CvSkillsComponent { @Input() skills: any[] = []; }
