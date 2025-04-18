import { Component } from '@angular/core';
import { Job, JobService } from './job.service';
import { ReactiveFormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-jobs',
  imports: [ReactiveFormsModule, CommonModule],
  templateUrl: './jobs.component.html',
  styleUrl: './jobs.component.css'
})
export class JobsComponent {
  jobs: Job[] = [];

  constructor(private jobService: JobService) { }

  ngOnInit(): void {
    this.jobService.getJobs()
      .subscribe({
        next: data => this.jobs = data,
        error: err => console.error('Failed to load jobs', err)
      });
  }
}
