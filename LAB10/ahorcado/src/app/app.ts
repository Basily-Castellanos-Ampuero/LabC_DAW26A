import { Component } from '@angular/core';
import { Juego } from './juego/juego';

@Component({
  selector: 'app-root',
  imports: [Juego],
  templateUrl: './app.html',
  styleUrl: './app.css',
})
export class App {
  protected title = 'ahorcado';
}
