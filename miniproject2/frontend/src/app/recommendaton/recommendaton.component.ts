import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { JobService } from './recomend.service';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule } from '@angular/forms';


interface JobRecommendation {
  job: {
    id: number;
    title: string;
    company: string;
    required_skills: string;
    required_experience: string;
    location: string;
    is_remote: boolean;
  };
  score: number;
}

@Component({
  selector: 'app-recommendaton',
  imports: [ReactiveFormsModule, CommonModule],
  templateUrl: './recommendaton.component.html',
  styleUrl: './recommendaton.component.css'
})
export class RecommendatonComponent {
  recommendations: JobRecommendation[] = [];
  loading = true;
  error: string | null = null;
  resumeId!: string;

  constructor(
    private route: ActivatedRoute,
    private jobService: JobService
  ) { }

  ngOnInit(): void {
    this.route.paramMap.subscribe(params => {
      this.resumeId = params.get('resume_id') || '';
      if (this.resumeId) {
        this.loadRecommendations();
      }
    });
  }

  loadRecommendations(): void {
    this.jobService.getRecommendations(this.resumeId)
      .subscribe({
        next: (data) => {
          this.recommendations = data;
          this.loading = false;
        },
        error: (err) => {
          this.error = 'Failed to load recommendations';
          this.loading = false;
          console.error(err);
        }
      });
  }
}
