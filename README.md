# BST-SO: Árboles y Sistemas Operativos

## Integrantes

- Rodrigo Rivera
- James Sipac

## Propósito

Este proyecto simula y compara el comportamiento de tres estructuras de árbol de búsqueda
(BST, Splay Tree y Red-Black Tree) en el contexto de la gestión de procesos de un sistema
operativo, específicamente inspirado en el Completely Fair Scheduler (CFS) de Linux.

Se analizan tres escenarios:
- **Escenario A**: Inserción de 1000 procesos con vruntime aleatorio
- **Escenario B**: Inserción secuencial (peor caso para el BST)
- **Escenario C**: Acceso frecuente al mismo proceso (ventaja del Splay Tree)

## Estructura del Proyecto
BST-SO/
├── src/
│   ├── main.py               # Script principal que corre los 3 escenarios
│   ├── trees/
│   │   ├── node.py           # Clase base Node
│   │   ├── bst.py            # Árbol Binario de Búsqueda
│   │   ├── splay.py          # Splay Tree
│   │   └── red_black.py      # Red-Black Tree
│   └── utils/
│       ├── generator.py      # Generadores de datos (aleatorio y secuencial)
│       ├── metrics.py        # Funciones de cálculo (promedio, min, max)
│       └── visualization.py  # Gráficas con matplotlib y Graphviz
├── results/                  # Imágenes generadas automáticamente
├── requirements.txt
└── README.md

## Cómo ejecutar

1. Instalar dependencias:

```bash
pip install -r requirements.txt
```

> También necesitas tener instalado Graphviz en tu sistema:
> - Windows: https://graphviz.org/download/
> - Linux: `sudo apt install graphviz`
> - Mac: `brew install graphviz`

2. Correr el proyecto:

```bash
cd src
python main.py
```

3. Las gráficas y visualizaciones se guardan automáticamente en la carpeta `results/`.
