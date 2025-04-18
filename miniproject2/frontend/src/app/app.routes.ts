import { Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { JobsComponent } from './jobs/jobs.component';
import { ResumeUploadComponent } from './resume-upload/resume-upload.component';
import { ResumeDetailComponent } from './resume-detail/resume-detail.component';
import { RecommendatonComponent } from './recommendaton/recommendaton.component';

export const routes: Routes = [
    { path: 'login', component: LoginComponent },
    { path: 'register', component: RegisterComponent },
    { path: 'jobs', component: JobsComponent },
    { path: 'upload', component: ResumeUploadComponent },
    { path: 'resume/:id', component: ResumeDetailComponent },
    { path: '', redirectTo: '/upload', pathMatch: 'full' },
    { path: 'resume/:resume_id/recommends', component: RecommendatonComponent },
];
