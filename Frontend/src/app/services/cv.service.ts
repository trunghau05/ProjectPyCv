import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class CvService {
  private apiUrl = 'http://localhost:8000/cv';

  constructor(private http: HttpClient) {}

  createCV(data: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/create/`, data);
  }

  updateCV(cv_id: string, data: any): Observable<any> {
    return this.http.put(`${this.apiUrl}/update/${cv_id}/`, data);
  }

  deleteCV(cv_id: string): Observable<any> {
    return this.http.delete(`${this.apiUrl}/delete/${cv_id}/`);
  }

  getCVsByUser(user_id: string): Observable<any> {
    return this.http.get(`${this.apiUrl}/user/${user_id}/`);
  }

  getCVDetail(cv_id: string): Observable<any> {
    return this.http.get(`${this.apiUrl}/${cv_id}/`);
  }
}
