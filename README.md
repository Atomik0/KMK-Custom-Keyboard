# KMK Firmware – Teclado Custom (Raspberry Pi Pico) – Matriz 6×14

Firmware basado en **KMK (CircuitPython)** para un teclado custom con **matriz 6 filas × 14 columnas**, diodos en orientación **COL2ROW**, tecla ISO **< >** y **AltGr real** (Right Alt) forzado con `ModifierKey(64)`.

---

## ✅ Características

* **Placa:** Raspberry Pi Pico (RP2040)
* **Matriz:** 6 filas × 14 columnas
* **Diodos:** `COL2ROW`
* **LED onboard:** se enciende al iniciar (verificación de carga)
* **Layout base:** QWERTY + fila F + fila números
* **Tecla ISO (< >):** definida con `KeyboardKey(100)`
* **AltGr funcional:** definido como `ModifierKey(64)` para compatibilidad completa (ej: `AltGr + ...`)
* **Tecla Fn:** habilita capa 1 (por ahora vacía)

---

## 🔌 Pines usados

### Filas (Rows) – 6

```python
keyboard.row_pins = (GP6, GP7, GP8, GP9, GP10, GP11)
```

### Columnas (Cols) – 14

```python
keyboard.col_pins = (
  GP18, GP17, GP16, GP15, GP14, GP13, GP12,
  GP5,  GP4,  GP3,  GP2,  GP1,  GP0,  GP19
)
```

### Orientación de diodos

```python
keyboard.diode_orientation = DiodeOrientation.COL2ROW
```

| | |
|---|---|
| ![](https://datablack.cl/github/KMK-Custom-Keyboard/conexion1.jpeg) | ![](https://datablack.cl/github/KMK-Custom-Keyboard/conexion2.jpeg) |

![](https://datablack.cl/github/KMK-Custom-Keyboard/diagrama.jpeg)

---

## 🧠 Notas importantes (AltGr y tecla ISO)

### ✅ AltGr (Alt derecho) “real”

En algunas versiones/instalaciones de KMK, `KC.ALGR` puede no ser reconocido como modificador real (aparece como `Key` en debug).
Para asegurar compatibilidad, se fuerza Right Alt como modificador HID:

```python
RALT = ModifierKey(64)  # 0x40 = Right Alt (AltGr)
```

Esto permite que el sistema operativo interprete correctamente combinaciones tipo **AltGr + tecla** según el layout del sistema.

### ✅ Tecla ISO `< >` (Non-US Backslash)

La tecla física ISO se define con:

```python
ISO_LTGT = KeyboardKey(100)
```

---

## 🛠️ Cómo usar / instalar (resumen)

1. Instala **CircuitPython** en la Raspberry Pi Pico.
2. Copia KMK a la unidad del dispositivo (carpeta `kmk/`).
3. Guarda este script como `code.py` (o `main.py`) en la raíz.
4. Reconecta el teclado.

Al iniciar:

* El LED onboard debe quedar encendido ✅

---

## 🧪 Debug / Diagnóstico

Para ver eventos por serial:

```python
keyboard.debug_enabled = True
```

Esto permite verificar:

* `key_number` al presionar teclas
* si un modificador sale como `ModifierKey(...)`
* si una tecla mal definida aparece solo como `Key`

Ejemplo esperado para AltGr correcto:

* debe verse como **ModifierKey**, no como **Key**

---

## ✏️ Personalización rápida

### Agregar funciones en capa Fn

Edita la **capa 1** y reemplaza `KC.NO` por acciones (ej: flechas, multimedia, macros).

Ejemplos útiles:

* `KC.VOLU`, `KC.VOLD`, `KC.MPLY`
* `KC.LEFT`, `KC.RIGHT`, `KC.UP`, `KC.DOWN`
* `KC.HOME`, `KC.END`, `KC.PGUP`, `KC.PGDN`

---

## 📌 Archivo principal

El firmware está contenido en el script `code.py` y finaliza con:

```python
if __name__ == "__main__":
    keyboard.go()
```

---

## ✅ Estado

Firmware estable y funcional (matriz alineada + AltGr operativo + ISO key OK).
La capa Fn está lista para configurarse según necesidades.
