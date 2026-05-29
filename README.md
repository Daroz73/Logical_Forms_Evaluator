# 🧮 Logic Formula Evaluator

Un evaluador de fórmulas de lógica proposicional interactivo desarrollado en **Python**. El proyecto procesa expresiones lógicas complejas, genera sus respectivas tablas de verdad de forma automática y determina si la expresión es una **tautología**, **contradicción** o **contingencia**.

El motor del proyecto está construido desde cero bajo la arquitectura clásica de un intérprete/compilador: **Lexer ➔ Parser (AST) ➔ Evaluator**, utilizando **Flet** para ofrecer una interfaz de usuario limpia y moderna.

---

## 🚀 Características

* **Análisis Sintáctico Robusto:** Soporta variables proposicionales en minúsculas y constantes numéricas (`0` para Falso, `1` para Verdadero).
* **Manejo de Precedencia:** El parser respeta jerárquicamente la prioridad de los operadores lógicos y el uso de paréntesis `()`.
* **Generador de Tablas de Verdad:** Evalúa de forma exhaustiva (por backtracking) todas las interpretaciones posibles de las variables.
* **Interfaz Gráfica (GUI):** Un entorno responsivo y minimalista creado con Flet que actúa como un editor de código táctico.

---

## 🎛️ Operadores Soportados

El sistema reconoce los siguientes símbolos lógicos (ordenados de mayor a menor precedencia):

| Operador | Símbolo | Ejemplo | Significado |
| :--- | :---: | :---: | :--- |
| **Negación** | `!` | `!p` | No p |
| **Conjunción** | `&` | `p & q` | p y q |
| **Disyunción** | `\|` | `p \| q` | p o q |
| **Implicación** | `=>` | `p => q` | Si p entonces q |
| **Equivalencia / Bicondicional** | `<=>` | `p <=> q` | p si y solo si q |

---

## 🏗️ Arquitectura del Proyecto

El código fuente está modularizado siguiendo patrones de diseño limpios:

* **`lexer.py`**: Analizador léxico. Convierte la cadena de texto de entrada en un flujo de tokens (`VARIABLE`, `OPERATOR`, `PAREN`, etc.).
* **`parser.py`**: Analizador sintáctico por descenso recursivo. Se encarga de validar la gramática de la fórmula y de construir el **AST** (Árbol de Sintaxis Abstracta).
* **Nodos del AST (`*_node.py`)**: Implementación del patrón *Composite* donde cada operador lógico (`Conjuntion`, `Disyuntion`, `Negation`, `Implies`, `IFF`) sabe cómo evaluarse a sí mismo recursivamente.
* **`evaluator.py`**: Explora el espacio de estados lógicos mediante recursión para construir la tabla de verdad fila por fila.
* **`UI.py`**: La interfaz gráfica que conecta el motor lógico con el usuario mediante un área de texto inteligente y controles de ejecución.

---

## 📦 Instalación y Requisitos

### Prerrequisitos
Asegúrate de tener instalado Python 3.9 o superior.
Asegurate de tener instalado Flet.

### Pasos para iniciar

1. **Clona este repositorio:**
   ```bash
   git clone [https://github.com/TU_USUARIO/TU_REPOSITORIO.git](https://github.com/TU_USUARIO/TU_REPOSITORIO.git)
   cd TU_REPOSITORIO
