import { Component } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';

@Component({
  selector: 'app-resume-upload',
  imports: [ReactiveFormsModule, CommonModule, FormsModule],
  templateUrl: './resume-upload.component.html',
  styleUrl: './resume-upload.component.css'
})
export class ResumeUploadComponent {
  selectedFile: File | null = null;
  uploadError: string | null = null;
  isUploading = false;

  constructor(
    private http: HttpClient,
    private router: Router
  ) { }

  onFileSelected(event: Event): void {
    const input = event.target as HTMLInputElement;
    if (input.files && input.files.length > 0) {
      this.selectedFile = input.files[0];
      this.uploadError = null;
    }
  }

  onSubmit(): void {
    if (!this.selectedFile) {
      this.uploadError = 'Please select a file first!';
      return;
    }

    this.isUploading = true;
    const formData = new FormData();
    formData.append('file', this.selectedFile);

    // Get CSRF token from cookie
    const csrfToken = this.getCookie('csrftoken');

    const headers = new HttpHeaders({
      'X-Requested-With': 'XMLHttpRequest',
      'X-CSRFToken': csrfToken || ''  // Add CSRF token header
    });

    this.http.post<{ id: number }>('http://localhost:8000/resume/upload/', formData, {
      headers,
      withCredentials: true
    }).subscribe({
      next: (response) => {
        this.router.navigate(['resume/', response.id]);
      },
      error: (error) => {
        console.error('Upload failed:', error);
        this.isUploading = false;
        this.uploadError = error.error?.message || 'Upload failed. Please try again.';
      },
      complete: () => {
        this.isUploading = false;
      }
    });
  }

  private getCookie(name: string): string | null {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop()?.split(';').shift() || null;
    return null;
  }
}
