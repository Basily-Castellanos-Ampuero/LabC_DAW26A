import { Injectable } from '@angular/core';

@Injectable({ providedIn: 'root' })
export class PalabraService {
  private palabras: string[] = [
    'ANGULAR',
    'COMPONENTE',
    'SERVICIO',
    'DIRECTIVA',
    'TYPESCRIPT',
    'PROGRAMACION',
    'NAVEGADOR',
    'VARIABLE',
    'PALABRA',
  ];

  // devuelvo una palabra al azar del arreglo
  obtenerPalabraAleatoria(): string {
    const indice = Math.floor(Math.random() * this.palabras.length);
    return this.palabras[indice];
  }
}
