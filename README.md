# Iron Elite

Demo local de un sitio de seguridad privada. Usa Python y Flask para leer la configuración y servir el sitio. La interfaz usa HTML, CSS y JavaScript.

## Abrir en Windows

Desde PowerShell, en la carpeta del proyecto, con Python 3.10 o superior:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\iniciar-lan.cmd
```

En el equipo que ejecuta Flask, abre [http://127.0.0.1:5000](http://127.0.0.1:5000). En otro equipo de la misma red, usa la dirección IPv4 que imprime Flask con el puerto `5000`. Usa `ipconfig` para consultar la IP si cambia. Mantén abierta la ventana mientras presentes la demo y pulsa Ctrl+C para detenerla.

Si el otro equipo no conecta, comprueba que ambos estén en la misma red y que el firewall permita TCP 5000 en el perfil de red activo. En una red de confianza con perfil privado, puedes agregar esta regla desde PowerShell como administrador:

```powershell
New-NetFirewallRule -DisplayName "Iron Elite demo LAN" -Direction Inbound -Action Allow -Protocol TCP -LocalPort 5000 -RemoteAddress LocalSubnet -Profile Private
```

Las redes de invitados pueden aislar a los dispositivos entre sí.

## Subir el código a GitHub

Crea un repositorio vacío en GitHub. Con Git instalado, ejecuta desde la carpeta del proyecto y sustituye `TU_USUARIO` por tu usuario u organización:

```powershell
git init -b main
git add .
git status --short
git commit -m "Agregar demo de Iron Elite"
git remote add origin https://github.com/TU_USUARIO/iron-elite.git
git push -u origin main
```

GitHub guardará el código. Para publicar la aplicación en internet se requiere un servicio que ejecute Python y Flask.

## Personalizar

| Cambio | Archivo o carpeta |
| --- | --- |
| Marca, portada, servicios, datos y mensaje de WhatsApp | `content/sitio.json` |
| Estructura de las secciones y notas de la demo | `frontend/templates/index.html` |
| Colores, espaciado y diseño responsivo | `frontend/static/estilos.css` |
| Menú móvil | `frontend/static/menu.js` |
| Fotos y logotipo | `frontend/static/img/` |
| Ruta de inicio y armado del enlace de WhatsApp | `backend/app.py` |

Para cambiar la foto o agregar el logotipo oficial, coloca los archivos en `frontend/static/img/` y ajusta `portada.imagen` y `portada.logo` con rutas como `img/logo.png`. Recarga el navegador para ver cambios en el contenido.

Los servicios son ejemplos. Valida con el cliente el catálogo, la cobertura, el número de WhatsApp y los materiales visuales. Cambia `demo` a `false` cuando quieras retirar las notas de presentación.
