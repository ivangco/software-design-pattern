# Software Design Pattern 

Un proyecto para utilizar varios patrones de diseño con ejemplos de uso de cada caso en python.

Los patrones de diseño en programación son soluciones reutilizables para problemas comunes que se presentan en el desarrollo de software. Estos patrones proporcionan un enfoque probado y estructurado para resolver problemas específicos, y permiten que los desarrolladores eviten reinventar la rueda cada vez que se encuentran con el mismo problema.

Existen diferentes tipos de patrones de diseño, por ejemplo los patrones creacionales que se utilizan para crear objetos y clases de manera eficiente, los patrones estructurales que se utilizan para organizar y relacionar los elementos del software, y los patrones de comportamiento que se utilizan para controlar el comportamiento y la interacción entre los objetos.

>nota:El uso de patrones de diseño en programación permite mejorar la calidad, la eficiencia, la reusabilidad y la escalabilidad del software.

## Los patrones de diseño de software se agrupan en tres categorías principales:

- Patrones de creación: estos patrones se centran en la forma en que se crean los objetos y se les da un estado inicial. Ejemplos incluyen el patrón de fábrica, el patrón abstracto de fábrica y el patrón de constructor.

- Patrones estructurales: estos patrones se centran en la composición de clases y objetos. Ejemplos incluyen el patrón de adaptador, el patrón de decorador y el patrón de fachada.

- Patrones de comportamiento: estos patrones se centran en la comunicación entre objetos y cómo se manejan los algoritmos. Ejemplos incluyen el patrón de comando, el patrón de observador y el patrón de estrategia.

>nota: Hay muchos patrones de diseño dentro de cada una de estas categorías, y cada uno puede ser aplicado en diferentes situaciones para resolver problemas específicos en el diseño de software.

## Cada categoria de patron de diseño contiene varios patrones de diseño con su propia definicion y aplicacion

### - Patrones creacionales:

- Patrón Singleton: este patrón asegura que solo haya una instancia de una clase y proporciona un punto de acceso global a esa instancia.

- Patrón de fábrica: este patrón se utiliza para crear objetos sin exponer la lógica de creación al cliente y permite a una clase delegar la creación de objetos a sus subclases.

- Patrón de fábrica abstracto: este patrón se utiliza para crear familias de objetos relacionados, sin especificar las clases concretas.

- Patrón del constructor: este patrón separa la construcción de objetos complejos de su representación, permitiendo diferentes representaciones del objeto construido.

- Patrón de objeto prototipo: este patrón se utiliza para crear nuevos objetos a partir de un prototipo existente, evitando la creación de objetos desde cero.

Estos patrones de diseño creacionales se utilizan para manejar la creación y la inicialización de objetos en un sistema de software. Al utilizar estos patrones, los desarrolladores de software pueden crear un código más modular, flexible y escalable.

### - Patrones estructurales:

- Patrón de adaptador: este patrón se utiliza para permitir que una clase existente se adapte a una interfaz diferente sin cambiar la funcionalidad de dicha clase.

- Patrón de puente: este patrón separa la abstracción y la implementación de una clase en dos jerarquías diferentes, lo que permite que ambas evolucionen de forma independiente.

- Patrón de composición: este patrón permite crear estructuras compuestas de objetos en árboles jerárquicos, lo que permite tratar a los objetos individuales y las composiciones de la misma manera.

- Patrón de decorador: este patrón permite agregar funcionalidad a un objeto existente de forma dinámica sin modificar su estructura utilizando clases adicionales.

- Patrón de fachada: este patrón proporciona una interfaz simplificada para un conjunto de subsistemas complejos, lo que hace que sea más fácil de usar y entender.

- Patrón de volante: este patrón se utiliza para reducir el número de objetos que se crean mediante el uso de objetos compartidos para representar componentes comunes en un sistema.

- Patrón de proxy: este patrón se utiliza para proporcionar un objeto de reemplazo para otro objeto, que brinda el mismo nivel de funcionalidad pero con un rendimiento mejorado.

Estos patrones de diseño estructurales se utilizan para organizar y relacionar diferentes componentes de un sistema de software de manera efectiva y eficiente. Al utilizar estos patrones, los desarrolladores pueden crear un código más fácil de entender, mantener y ampliar.


### - Patrones por comportamiento:

- Patrón de cadena de responsabilidad: este patrón se utiliza para establecer una cadena de objetos, donde cada objeto en la cadena tiene la oportunidad de manejar una solicitud o pasarla al siguiente objeto de la cadena.

- Patrón de comandos: este patrón encapsula una solicitud como un objeto, permitiendo que se configure, se encole y se deshaga en un momento posterior.

- Patrón de iterador: este patrón se utiliza para proporcionar una manera de acceder a los elementos de una colección de objetos de manera secuencial sin conocer su implementación subyacente.

- Patrón de intérprete: Este patrón se utiliza para definir una gramática para un idioma, así como proporcionar una forma de evaluar las oraciones en ese idioma.

- Patrón de mediador: este patrón proporciona una forma de reducir las dependencias entre objetos mediante la introducción de un objeto mediador que coordina las interacciones entre los objetos que implementan diferentes comportamientos.

- Patrón de observador: este patrón establece una relación uno a muchos entre objetos, de modo que cuando cambia el estado de uno de ellos, todos los demás objetos son notificados y actualizados automáticamente.

- Patrón visitante: este patrón permite definir una nueva operación sobre los objetos de una clase sin cambiar dicha clase, proporcionando una forma de separar la lógica de las operaciones de los objetos en una clase separada.

- Patrón de estrategia: este patrón permite que los algoritmos se seleccionen dinámicamente y cambien en tiempo de ejecución en base a una interfaz común.

- Patrón de plantilla de método: este patrón define los pasos básicos de un algoritmo en un método, lo que permite que los submétodos se definan por separado por las subclases.

Estos patrones de diseño por comportamiento se utilizan para definir la colaboración entre objetos en un sistema de software y para definir cómo se controlarán y coordinarán dichos objetos en tiempo de ejecución. En resumen, al utilizar estos patrones, los desarrolladores pueden crear sistemas de software más flexibles y fáciles de mantener.

### Los patrones de diseño conocidos actualmente son:

- Patrón de diseño de fábrica (Factory Design Pattern)
- Patrón de diseño Singleton (Singleton Design Pattern)
- Patrón de diseño de constructor (Builder Design Pattern)
- Patrón de diseño Prototipo (Prototype Design Pattern)
- Patrón de diseño adaptador (Adapter Design Pattern)
- Patrón de diseño Puente (Bridge Design Pattern)
- Patrón de diseño Compuesto (Composite Design Pattern)
- Patrón de diseño Decorador (Decorator Design Pattern)
- Patrón de diseño Fachada (Facade Design Pattern)
- Patrón de diseño Volcado (Flyweight Design Pattern)
- Patrón de diseño Proxy (Proxy Design Pattern)
- Patrón de diseño Cadena de responsabilidad (Chain of Responsibility Design Pattern)
- Patrón de diseño Comandos (Command Design Pattern) 
- Patrón de diseño Iterador (Iterator Design Pattern)
- Patrón de diseño Intérprete (Interpreter Design Pattern)
- Patrón de diseño Mediador (Mediator Design Pattern)
- Patrón de diseño Observador (Observer Design Pattern)
- Patrón de diseño Visitante (Visitor Design Pattern)
- Patrón de diseño Estrategia (Strategy Design Pattern)
- Patrón de diseño Plantilla de método (Template Method Design Pattern)
- Patrón de diseño Estado (State Design Pattern)
- Patrón de diseño Memento (Memento Design Pattern)

La secuencia de aprendizaje de los patrones de diseño puede variar dependiendo de la experiencia y habilidades previas que tengas. Sin embargo, aquí te muestro una posible secuencia en la que podrías aprender los patrones de diseño:

- Aprende los conceptos básicos de programación orientada a objetos (POO), como clases, objetos, herencia, polimorfismo, etc. Será más fácil entender los patrones de diseño después de conocer estos conceptos.

- Aprende patrones de diseño creacionales, como Singleton, Factory, Abstract Factory, etc. Estos patrones tratan cómo crear objetos de manera más flexible y mantenible.

- Aprende patrones de diseño estructurales, como Adapter, Bridge, Decorator, etc. Estos patrones se centran en la composición de objetos y cómo se agrupan para formar estructuras más grandes pero flexibles.

- Aprende patrones de diseño de comportamiento, como Observer, Strategy, Template Method, etc. Estos patrones describen cómo los objetos interactúan entre sí y cómo se comunican para lograr objetivos.

- Aprende patrones de diseño arquitectónico, como Microservicios, Monolith-to-Microservices, Event-driven, etc. Estos patrones se centran en cómo se modela y organiza una aplicación completa.

Es importante tener en cuenta que la comprensión de los patrones de diseño no significa que siempre debas aplicarlos. La decisión de aplicar patrones de diseño debe tomarse cuidadosamente en función de los requisitos y el contexto del proyecto.