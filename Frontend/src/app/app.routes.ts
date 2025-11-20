import { Routes } from '@angular/router';
import { CvListPage } from './pages/cv-list/cv-list.page';
import { CvCreateEditPage } from './pages/cv-create-edit/cv-create-edit.page';
import { CvDetailPage } from './pages/cv-detail/cv-detail.page';

export const routes: Routes = [
  { path: '', redirectTo: 'cv-list', pathMatch: 'full' },
  { path: 'cv-list', component: CvListPage },
  { path: 'cv-create', component: CvCreateEditPage },         
  { path: 'cv-edit/:cv_id', component: CvCreateEditPage },   
  { path: 'cv-detail/:cv_id', component: CvDetailPage }     
];
