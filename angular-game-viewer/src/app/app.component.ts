import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClient, HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, HttpClientModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  grid: string[][] = [];
  width = 0;
  height = 0;

  constructor(private http: HttpClient) {}

  ngOnInit() {
    this.http.get<any>('http://localhost:5000/state').subscribe(data => {
      this.grid = data.grid;
      this.width = data.width;
      this.height = data.height;
    });

    if(typeof window !== 'undefined') {
      window.addEventListener('keydown', this.handleKey.bind(this));
    }
  }

  move(direction: string) {
    this.http.post<any>('http://localhost:5000/move', { direction }).subscribe(data => {
      this.grid = data.grid;
      
      // Now the enemy AI makes a move...
      this.http.post<any>('http://localhost:5000/ai', { }).subscribe(data => {
        this.grid = data.grid;
      });
    });
  }

  moveAI() {
    this.http.post<any>('http://localhost:5000/ai', { }).subscribe(data => {
      this.grid = data.grid;
    });
  }

  resetGame() {
    this.http.post<any>('http://localhost:5000/reset', { }).subscribe(data => {
      this.grid = data.grid;
    });
  }

  handleKey(event: KeyboardEvent) {
    const key = event.key.toLowerCase();
    const moveKeys = ['w','a','s','d'];//, 'arrowup', 'arrowdown', 'arrowleft', 'arrowright'];

    if (moveKeys.includes(key)) {
      //let direction = '';
      this.move(key);
    }
  }
}
