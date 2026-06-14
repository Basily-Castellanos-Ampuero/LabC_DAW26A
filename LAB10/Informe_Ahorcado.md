# Informe - Laboratorio 10: Juego del Ahorcado en Angular

## Introduccion

Para el ejercicio propuesto del laboratorio se decidio implementar el juego del
ahorcado usando Angular. La idea es tener un arreglo con varias palabras, elegir
una al azar y dejar que el usuario vaya adivinando letra por letra hasta
completar la palabra o quedarse sin intentos. La interfaz se armo de forma
sencilla para centrarse en que la logica funcionara bien.

## Herramientas usadas

- Angular CLI 20
- Node 22
- TypeScript
- HTML y CSS

## Estructura del proyecto

Se trabajo sobre un proyecto creado con `ng new ahorcado`. Los archivos
relevantes son:

```
ahorcado/src/app/
  app.ts                -> componente raiz, solo muestra el juego
  app.html              -> contiene <app-juego></app-juego>
  palabra.service.ts    -> servicio con el arreglo de palabras
  juego/
    juego.ts            -> logica del juego
    juego.html          -> interfaz
    juego.css           -> estilos
```

Se separo la parte de las palabras en un servicio porque se considero mas
ordenado tener los datos en un lugar aparte y dejar el componente solo con la
logica del juego.

## El servicio de palabras

En `palabra.service.ts` se guardo un arreglo de palabras y un metodo que
devuelve una al azar. Se marco como `providedIn: 'root'` para inyectarlo
directamente en el componente sin necesidad de registrarlo en otro lado.

```ts
obtenerPalabraAleatoria(): string {
  const indice = Math.floor(Math.random() * this.palabras.length);
  return this.palabras[indice];
}
```

## La logica del juego

En el componente `juego.ts` se manejan dos arreglos: uno con las letras que el
usuario acerto y otro con las que fallo. Con esos dos arreglos se calcula casi
todo lo demas usando getters:

- `palabraMostrada`: recorre la palabra y muestra la letra si ya se acerto, o
  un guion bajo si todavia no.
- `errores`: es simplemente la cantidad de letras erradas.
- `gano`: es verdadero cuando todas las letras de la palabra ya estan
  adivinadas.
- `perdio`: es verdadero cuando los errores llegan al maximo (6).

El metodo `intentar(letra)` revisa si la letra esta en la palabra y la agrega al
arreglo que corresponde. Se valida que el juego no haya terminado y que la
letra no se haya usado antes, para evitar repeticiones.

## La interfaz

Para la interfaz se usaron las directivas que pedia el laboratorio:

- `*ngFor` para dibujar el teclado con las 26 letras y para mostrar la palabra
  oculta.
- `*ngIf` para mostrar las partes del muneco segun la cantidad de errores y para
  los mensajes de victoria o derrota.

El ahorcado se dibujo con un `<svg>`. La horca siempre se ve, y cada parte del
muneco (cabeza, cuerpo, brazos y piernas) va apareciendo con un `*ngIf` que
depende del numero de errores. Cuando se llega a 6 errores el dibujo queda
completo y el juego termina.

Los botones del teclado se deshabilitan cuando la letra ya se uso o cuando el
juego termino, usando un binding a la propiedad `disabled`. Tambien hay un boton
de "Reiniciar" que llama a `nuevoJuego()` para empezar de nuevo con otra palabra.

## Cumplimiento de los requisitos

- Seleccionar una palabra aleatoria: lo hace el servicio.
- Mostrar letras ocultas: con el getter `palabraMostrada`.
- Permitir ingreso de letras: con el teclado en pantalla.
- Validar aciertos y errores: en el metodo `intentar`.
- Dibujar progresivamente el ahorcado: con el SVG y los `*ngIf`.
- Mostrar mensajes de victoria o derrota: con los getters `gano` y `perdio`.
- Permitir reiniciar el juego: con el boton de reinicio.

## Como ejecutarlo

Desde la carpeta `ahorcado` se ejecuta:

```
npm install
ng serve
```

Y se abre el navegador en `http://localhost:4200`.

## Conclusion

Con este ejercicio se repasaron los conceptos principales de Angular: componentes,
servicios, inyeccion de dependencias, data binding, eventos y directivas. Sirvio
para ver como separar los datos de la logica y como mantener la interfaz simple
pero funcional.
