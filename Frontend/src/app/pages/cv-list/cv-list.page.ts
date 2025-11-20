import { Component, OnInit } from '@angular/core';
import { CvService } from '../../services/cv.service';
import { Router } from '@angular/router';
import { CvCardComponent } from '../../components/cv-card/cv-card.component';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  imports: [CvCardComponent, CommonModule, FormsModule],
  selector: 'app-cv-list',
  templateUrl: './cv-list.page.html',
  styleUrls: ['./cv-list.page.css']
})
export class CvListPage implements OnInit {
  cvs: any[] = [];
  userId = '691f48f387c2866156590f47';

  constructor(private cvService: CvService, private router: Router) {}

  ngOnInit(): void { this.loadCVs(); }

  loadCVs() {
    this.cvService.getCVsByUser(this.userId).subscribe(res => {
      if (res.status === 'success') this.cvs = res.cvs;
      console.log(this.cvs);
      
    });
  }

  viewCV(cv_id: string) { this.router.navigate(['/cv-detail', cv_id]); }
  createCV() { this.router.navigate(['/cv-create']); }
  deleteCV(cv_id: string) {
    if (confirm('Xóa CV này?')) this.cvService.deleteCV(cv_id).subscribe(()=>this.loadCVs());
  }
}
