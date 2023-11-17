# Biblioteca-App

Una biblioteca necesita un software que le permita registrar los datos de los libros que posee y de sus préstamos. De cada libro conoce como mínimo su código, título, precio de reposición (para el caso de extravíos o daños) y estado (disponible, prestado o extraviado).

Por otro lado, cada vez que un libro es prestado se registra el socio que lo solicita y la cantidad de días pactados para su devolución. Cuando un libro es devuelto debe calcularse si fue devuelto en fecha o con demora, registrando si corresponde la cantidad de días de retraso.

Todo libro prestado y que posea más de 30 días de demora en su devolución se considera extraviado, por lo tanto el software debe poder listar aquellos que se encuentren en tal condición para ofrecer al usuario el cambio de estado.

Cuando un socio solicite un libro, el software debe verificar que el socio no posea más de tres libros prestados (aunque todavía se encuentre dentro del plazo del préstamo) y que no posea ningún libro con demora en su devolución.

La biblioteca requiere que el software ofrezca como mínimo las funcionalidades de:
1. **Administración de socios**
2. **Administración de libros**
3. **Registración de préstamos y devoluciones**
4. **Registración de libros extraviados**
5. **Reportes:**
   1. Cantidad de libros en cada estado (tres totales)
   2. Sumatoria del precio de reposición de todos los libros extraviados
   3. Nombre de todos los solicitantes de un libro en particular identificado por su título
   4. Listado de préstamos de un socio identificado por su número de socio
   5. Listado de préstamos demorados

Para correr el programa ejecute los siguientes comandos:
```bash
   cd src
   python bibliotecaApp.py
