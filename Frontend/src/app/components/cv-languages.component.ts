import { CommonModule } from '@angular/common';
import { Component, Input } from '@angular/core';

@Component({
  imports: [CommonModule],
  selector: 'app-cv-languages',
  template: `<div class="languages"><span class="chip" *ngFor="let l of languages">{{l.name || l}}</span></div>`,
  styles:[`.languages { display:flex; flex-wrap:wrap; gap:5px; } .chip { background:#4caf50; color:#fff; padding:5px 10px; border-radius:20px; }`]
})
export class CvLanguagesComponent { @Input() languages: any[] = []; }
