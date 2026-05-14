# Sikuani Study

Editor de texto en terminal (TUI) construido con Python y `curses`. Proyecto de estudio para explorar arquitectura limpia con interfaces, presenters y modelos en aplicaciones de consola.

## Descripcion

Sikuani Study es una aplicacion de terminal que permite escribir y editar texto directamente en la consola usando una interfaz visual basada en colores y una barra de tareas. El objetivo principal es aprender y practicar el patron de diseño presenter/interface/model en Python puro.

## Arquitectura

```
src/
├── interfaces/          # Contratos abstractos (ABC)
│   ├── IDocumentHandling.py
│   └── IWindow.py
├── presenters/          # Implementaciones concretas
│   ├── DocumentHandling.py
│   └── Window.py
├── models/
│   └── services/        # Logica de negocio (en construccion)
└── views/               # Vistas (en construccion)
```

El proyecto sigue un patron **Interfaz → Presenter**:

- `IDocumentHandling` / `IWindow` definen los contratos
- `DocumentHandling` maneja la escritura, borrado, carga y guardado de documentos
- `Window` orquesta la UI: inicializa colores, barra de tareas y delega el input al handler

## Requisitos

- Python 3.x
- Terminal con soporte de colores

## Uso

```bash
python app.py
```

- Escribi texto normalmente (caracteres imprimibles ASCII)
- `Enter` para nueva linea
- `Backspace` para borrar
- `q` para salir

## Estado

Proyecto en desarrollo activo. Las capas `models/services` y `views` estan pendientes de implementacion.
