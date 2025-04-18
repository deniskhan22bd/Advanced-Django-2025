import { Component } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { ResumeService } from './resume.service';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

@Component({
  selector: 'app-resume-detail',
  imports: [ReactiveFormsModule, CommonModule, FormsModule],
  templateUrl: './resume-detail.component.html',
  styleUrl: './resume-detail.component.css'
})
export class ResumeDetailComponent {
  resume: any;

  constructor(
    private route: ActivatedRoute,
    private resumeService: ResumeService,
    private router: Router
  ) {}

  ngOnInit(): void {
    const id = this.route.snapshot.paramMap.get('id');
    if (id) {
      this.resumeService.getResumeDetail(id).subscribe({
        next: (data) => this.resume = data,
        error: () => alert("Resume not found")
      });
    }
  }
  chunkArray(arr: any[], chunkSize: number): any[][] {
    const chunks = [];
    for (let i = 0; i < arr.length; i += chunkSize) {
      chunks.push(arr.slice(i, i + chunkSize));
    }
    return chunks;
  }
  
  redirectToUpload(): void {
    this.router.navigate(['/upload']);
  }
}

