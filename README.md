# 🧬 SymbiOSis: Mi Parke de Diversiones 🎢🌌

> "Un Soñador con Poca RAM, pero con una visión que no cabe en 64GB." 👨🏻‍💻

Este proyecto no es solo un conjunto de salvapantallas; es mi **rincón de experimentación visual y filosófica**. Aquí es donde el hardware de mi Mac, el código y mis creencias convergen para crear algo más que píxeles: una experiencia de simbiosis.

## 🧠 La Filosofía SymbiOSis
Para mí, la tecnología no debe ser un monólogo de la máquina, sino un diálogo. Este ecosistema nace bajo la idea del **Sistema Operativo del Criterio**: un modelo donde la IA y el ser humano no compiten, sino que colaboran bajo la "fricción deliberada" del juicio humano.

## 🚀 ¿Qué hay en esta sinfonía?

### 1. HÉCTOR: Orbital Symphony (v3.9) 📉🌡️
Mi monitor diario. No solo me dice cuánta RAM me queda (que suele ser poca), sino que visualiza el pulso térmico y la carga de mi sistema con una estética inspirada en *Tron Legacy*. Es el hardware cobrando vida propia.

### 2. Faith: Verdades Eternas 📖✨
Porque no solo de pan (ni de bytes) vive el hombre. He creado un espacio minimalista para reflexionar sobre verdades bíblicas y pensamientos de gigantes como **Spurgeon, Sproul, San Agustín e Ireneo de Lyon**. Es el recordatorio de lo que realmente importa cuando la pantalla se apaga.

### 3. El Reveal Épico 🛡️🎬
Un diseño cinemático basado en mi logo real. Representa la evolución: desde la construcción básica hasta la red neuronal que alimenta el proyecto pedagógico **SymbiOSis**.

## 🛠️ Bajo el Capó (Las Tripas del Parke) 🎡

Aquí es donde ocurre la magia técnica, ¡pero con luces de neón! 🌈✨

*   **🐍 Motor de Datos (Backend)**: Un script en `python3` que actúa como el operario del Parke, extrayendo telemetría real (`top`, `sysctl`, `df`) para que los juegos tengan vida.
*   **🎨 Pinceles Digitales (Frontend)**: Nada de frameworks aburridos. Aquí usamos **HTML5 puro**, **Vanilla CSS** (con mucho glow) y **JS nativo**. 🍭
*   **🔌 Conexión Maestra**: Todo se comunica vía una API JSON local que corre en el puerto `8080`.
*   **🎢 El Vagón**: Diseñado para correr sobre el cargador **WebViewScreenSaver** en macOS.

## 🚀 ¿Cómo hacerlo latir?
1. Despliega los archivos en `~/Library/Application Support/HectorSaver/`.
2. Lanza el motor de datos: `python3 server.py`.
3. Configura tu cargador de salvapantallas para apuntar a `http://localhost:8080/index.html`.

---
**SymbiOSis** es un proyecto vivo. Es mi bitácora de vuelo en este viaje de aprendizaje constante.

🔗 [Mi Repositorio de Ideas](https://github.com/HecAguilaV/ParkeDiversiones)

*Hecho con fe, café y muchas horas de debug.*  
**Héctor Águila - 2026**
