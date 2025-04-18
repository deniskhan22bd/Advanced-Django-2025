import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Job {
  id: number;
  company: string;
  title: string;
  description: string;
  required_skills: string[];
  required_experience: number;
  location: string;
  is_remote: boolean;
  created_at: string;
}

@Injectable({ providedIn: 'root' })
export class JobService {
  private apiUrl = 'http://localhost:8000/jobs/api/'

  constructor(private http: HttpClient) { }

  getJobs(): Observable<Job[]> {
    return this.http.get<Job[]>(this.apiUrl, { withCredentials: true });
  }
}
