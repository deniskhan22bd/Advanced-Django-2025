import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class JobService {
  private apiUrl = 'http://localhost:8000/resume';

  constructor(private http: HttpClient) { }

  getRecommendations(resumeId: string): Observable<any> {
    return this.http.get(`${this.apiUrl}/${resumeId}/recommends`);
  }
}