# Touch Capacitive Sensor - mdBook Documentation

Esta carpeta contiene la documentación técnica completa del **Touch Capacitive Sensor** construida con [mdBook](https://rust-lang.github.io/mdBook/).

## 📁 Estructura del Proyecto

```
software/book/
├── book.toml          # Configuración de mdBook
├── src/               # Archivos fuente de la documentación
│   ├── SUMMARY.md     # Índice y estructura de navegación
│   ├── introduction.md # Página de introducción
│   ├── hardware/      # Documentación de hardware
│   ├── software/      # Ejemplos de código y APIs
│   ├── applications/  # Casos de uso y aplicaciones
│   └── resources/     # Recursos adicionales
├── theme/             # Tema personalizado de UNIT Electronics
└── book/              # Salida generada (ignorada en git)
```

## 🚀 Desarrollo Local

### Instalación de mdBook

**Opción 1: Script automático**
```bash
# Desde la raíz del proyecto
./setup-mdbook.sh
```

**Opción 2: Instalación manual**
```bash
# Con Cargo (Rust)
cargo install mdbook

# Con Homebrew (macOS)
brew install mdbook

# Ubuntu/Debian
curl -sSL https://github.com/rust-lang/mdBook/releases/download/v0.4.40/mdbook-v0.4.40-x86_64-unknown-linux-gnu.tar.gz | tar -xz
sudo mv mdbook /usr/local/bin/
```

### Comandos de Desarrollo

```bash
cd software/book

# Servidor de desarrollo con hot-reload
mdbook serve --open

# Construir documentación estática
mdbook build

# Limpiar archivos generados
mdbook clean

# Verificar la documentación
mdbook test
```

## 🌐 Despliegue Automático

La documentación se despliega automáticamente en GitHub Pages cuando:
- Se hace push a `main` o `develop`
- Se modifican archivos en `software/book/`

El workflow de GitHub Actions:
1. Instala mdBook
2. Construye la documentación
3. Copia recursos adicionales (imágenes, PDFs, ejemplos)
4. Despliega en GitHub Pages

## ✅ Flujo de Trabajo

1. **Editar contenido**: Modifica archivos en `src/`
2. **Probar localmente**: `mdbook serve` para vista previa
3. **Commit y push**: Los cambios se despliegan automáticamente
4. **Verificar despliegue**: Revisar en GitHub Pages

## 📝 Convenciones

- **Imágenes**: Usar rutas relativas desde `src/`
- **Enlaces**: Preferir enlaces relativos cuando sea posible
- **Código**: Usar bloques de código con sintaxis específica
- **Recursos**: Hardware resources se copian automáticamente desde `hardware/`

## 🎨 Personalización

El tema se encuentra en `theme/` y incluye:
- `custom.css`: Estilos de UNIT Electronics
- `custom.js`: Funcionalidades adicionales (botones de copia, etc.)

## 📖 Recursos

- [mdBook Documentation](https://rust-lang.github.io/mdBook/)
- [Markdown Guide](https://www.markdownguide.org/)
- [GitHub Pages](https://pages.github.com/)

## 🔧 Mantenimiento

- **Actualizar mdBook**: `cargo install --force mdbook`
- **Verificar enlaces**: `mdbook test`
- **Optimizar imágenes**: Comprimir imágenes grandes antes de agregar

---

**UNIT Electronics** - Documentación técnica profesional
