import { Injectable } from '@angular/core';
import { HttpClient, HttpEvent, HttpRequest } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ResumeService {
  private uploadUrl = 'http://localhost:8000/resume/upload/';
  private detailUrl = 'http://localhost:8000/resume/';

  constructor(private http: HttpClient) {}

  uploadResume(file: File): Observable<HttpEvent<any>> {
    const formData = new FormData();
    formData.append('file', file);

    const req = new HttpRequest('POST', this.uploadUrl, formData, {
      reportProgress: true,
      withCredentials: true
    });

    return this.http.request(req);
  }

  getResumeDetail(id: string): Observable<any> {
    return this.http.get<any>(`http://localhost:8000/resume/${id}/`);
  }
  
}
