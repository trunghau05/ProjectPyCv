import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CvBasic } from './cv-basic';

describe('CvBasic', () => {
  let component: CvBasic;
  let fixture: ComponentFixture<CvBasic>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CvBasic]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CvBasic);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
