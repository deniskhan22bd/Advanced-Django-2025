import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RecommendatonComponent } from './recommendaton.component';

describe('RecommendatonComponent', () => {
  let component: RecommendatonComponent;
  let fixture: ComponentFixture<RecommendatonComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [RecommendatonComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(RecommendatonComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
