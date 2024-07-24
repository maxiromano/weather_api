# Weather API Service with Redis Caching

## Descripción

Este proyecto proporciona un servicio de API para consultar información meteorológica usando una API externa. Utiliza Redis para el almacenamiento en caché de los datos del clima para mejorar el rendimiento y reducir las solicitudes repetidas a la API externa.

## Tecnologías Utilizadas

- **FastAPI:** Framework para construir APIs web rápidas y eficientes.
- **Redis:** Base de datos en memoria para almacenamiento en caché.
- **Requests:** Biblioteca para realizar solicitudes HTTP a la API externa de clima.
- **Pydantic:** Para la validación de datos y la creación de modelos.

## Requisitos

- Python 3.8 o superior
- Redis

## Instalación

1. **Clonar el repositorio:**

    ```bash
    git clone https://github.com/tu-usuario/tu-repositorio.git
    cd tu-repositorio
    ```

2. **Crear y activar un entorno virtual:**

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # Para Windows: .venv\Scripts\activate
    ```

3. **Instalar las dependencias:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configurar las variables de entorno:**

    Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:

    ```plaintext
    API_KEY=tu_clave_de_api
    WEATHER_API_URL=https://api.visualcrossing.com
    REDIS_URL=redis://localhost:6379
    ```

    Asegúrate de reemplazar `tu_clave_de_api` con tu clave de API para la API de clima.

5. **Iniciar Redis:**

    Asegúrate de que Redis esté en funcionamiento en tu máquina local o en el servidor al que te conectas.

## Uso

Para iniciar el servicio, ejecuta el siguiente comando:

```bash
uvicorn main:app --reload
