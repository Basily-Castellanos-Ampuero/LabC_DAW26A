import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PalabraService } from '../palabra.service';

@Component({
  selector: 'app-juego',
  imports: [CommonModule],
  templateUrl: './juego.html',
  styleUrl: './juego.css',
})
export class Juego {
  palabra = '';
  letrasAdivinadas: string[] = [];
  letrasErradas: string[] = [];
  maxErrores = 6;
  abecedario = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('');

  constructor(private palabraService: PalabraService) {
    this.nuevoJuego();
  }

  // reinicio el juego con una palabra nueva
  nuevoJuego(): void {
    this.palabra = this.palabraService.obtenerPalabraAleatoria();
    this.letrasAdivinadas = [];
    this.letrasErradas = [];
  }

  // armo la palabra mostrando solo las letras ya acertadas
  get palabraMostrada(): string[] {
    return this.palabra
      .split('')
      .map((letra) => (this.letrasAdivinadas.includes(letra) ? letra : '_'));
  }

  get errores(): number {
    return this.letrasErradas.length;
  }

  get gano(): boolean {
    return this.palabra
      .split('')
      .every((letra) => this.letrasAdivinadas.includes(letra));
  }

  get perdio(): boolean {
    return this.errores >= this.maxErrores;
  }

  get juegoTerminado(): boolean {
    return this.gano || this.perdio;
  }

  // verifico si la letra ya fue usada para no repetirla
  letraUsada(letra: string): boolean {
    return (
      this.letrasAdivinadas.includes(letra) ||
      this.letrasErradas.includes(letra)
    );
  }

  // proceso el intento del usuario al elegir una letra
  intentar(letra: string): void {
    if (this.juegoTerminado || this.letraUsada(letra)) {
      return;
    }
    if (this.palabra.includes(letra)) {
      this.letrasAdivinadas.push(letra);
    } else {
      this.letrasErradas.push(letra);
    }
  }
}
