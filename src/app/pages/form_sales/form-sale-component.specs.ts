import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FormCardsComponent } from './form-cards.component';

describe('FormCardsComponent', () => {
  let component: FormCardsComponent;
  let fixture: ComponentFixture<FormCardsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [FormCardsComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(FormCardsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
