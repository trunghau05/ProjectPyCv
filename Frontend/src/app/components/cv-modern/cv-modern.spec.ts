import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CvModern } from './cv-modern';

describe('CvModern', () => {
  let component: CvModern;
  let fixture: ComponentFixture<CvModern>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CvModern]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CvModern);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
