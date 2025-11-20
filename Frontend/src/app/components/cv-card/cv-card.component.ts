import { Component, Input, Output, EventEmitter, OnInit } from '@angular/core';

@Component({
  selector: 'app-cv-card',
  templateUrl: './cv-card.component.html',
  styleUrls: ['./cv-card.component.css']
})
export class CvCardComponent implements OnInit{
  @Input() cv: any;
  @Output() view = new EventEmitter<string>();
  @Output() delete = new EventEmitter<string>();
  
  ngOnInit(): void {
      console.log(this.cv);
  }
}
