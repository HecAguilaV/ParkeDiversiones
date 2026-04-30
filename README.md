# 🧬 SymbiOSis: HÉCTOR Orbital Symphony 🌌

Un ecosistema de protectores de pantalla dinámicos de alta fidelidad basados en HTML/JS para macOS, diseñados para fusionar arte digital, monitoreo de hardware y visualización de audio en tiempo real.

## 🚀 La Joya de la Corona: HÉCTOR Orbital Symphony
El diseño principal (**v3.8 Nerd Edition**) es un híbrido sofisticado que combina:
- **Telemetría de Hardware en Tiempo Real**: 
  - **CPU**: Carga del sistema con **Thermal Engine** integrado (estimación de temperatura dinámica con alertas de color).
  - **RAM**: Monitoreo detallado (Usada / Total).
  - **SWAP**: Indicador de memoria de intercambio para Power Users.
  - **SSD**: Estado de almacenamiento del disco principal.
- **Visualizador de Audio 3D**: Espectro circular reactivo que pulsa y brilla con la música (requiere acceso al micrófono).
- **Estética Tron Legacy/Ares**: 
  - Fondo con rejilla 3D y perspectiva infinita.
  - **Grid Runners**: Corredores de luz que recorren la pista siguiendo la geometría 3D.
  - **Digital Rain**: Lluvia de bits cósmica que reacciona al bajo de la música.
  - **Brillo Aditivo**: Iluminación neón de alta fidelidad (Electric Cyan & Ares Red).

## 🛠 Estructura del Proyecto
- `index.html`: Controlador maestro. Configurado por defecto para cargar la *Sinfonía Orbital*.
- `server.py`: El "Cerebro" del sistema. Provee una API JSON en `/stats` con toda la telemetría del Mac (CPU, RAM, SWAP, SSD, TEMP).
- `designs/`: Galería de diseños adicionales (Matrix, SIGA Architecture, Zen, etc.).

## 🚀 Instalación y Uso
1. **Requisito Maestro**: Este proyecto es una aplicación web independiente, pero para usarlo como salvapantallas en macOS necesitas un cargador. Se recomienda el uso de **[WebViewScreenSaver](https://github.com/liquid-metal/WebViewScreenSaver)** (Licencia Apache 2.0).
2. **Despliegue**: Copia los archivos de este repositorio a `~/Library/Application Support/HectorSaver/`.
3. **Servidor**: Ejecuta `python3 server.py`. El servidor debe estar corriendo para que la telemetría (CPU, RAM, TEMP) funcione.
4. **Configuración**: En los ajustes de tu salvapantallas web, apunta a la URL local:
   `http://localhost:8080/index.html`

## 🧠 Telemetría Avanzada
El sistema utiliza comandos nativos de macOS (`top`, `sysctl`, `df`) para extraer datos precisos sin necesidad de instalar herramientas de terceros, superando las restricciones de sandbox de macOS Sequoia.

## ⚖️ Licencia
Este proyecto está bajo la Licencia **MIT**. Consulta el archivo `LICENSE` para más detalles.

---
*Diseñado con pasión por la tecnología y el arte digital.*  
**> Un Soñador con Poca RAM 👨🏻‍💻**
