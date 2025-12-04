import { CommonModule } from '@angular/common';
import { Component, Input, OnInit, OnChanges, SimpleChanges } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { MatIconModule } from '@angular/material/icon';
import { User } from '../../interfaces/user.interface';

@Component({
  selector: 'app-cv-basic',
  imports: [MatIconModule, CommonModule, FormsModule],
  templateUrl: './cv-basic.html',
  styleUrls: ['./cv-basic.scss'],
})
export class CvBasic implements OnInit, OnChanges {
  @Input() user!: User; 

  ngOnInit() {
    if (!this.user) {
      this.user = {} as User;
    }
  }

  ngOnChanges(changes: SimpleChanges) {
    if (changes['user']) {
      console.log('User updated in CvBasic:', this.user);
    }
  }
}
