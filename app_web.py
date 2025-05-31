from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from src.controller.web_controlador import WebControlador
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

if __name__ == "__main__":
    app = FastAPI()
    web_controlador = WebControlador()
    
    # Configurar CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins="*",
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Montar archivos estáticos
    app.mount("/static", StaticFiles(directory="src/view/web"), name="static")
    
    # Ruta para el index.html
    @app.get("/")
    async def read_root():
        return FileResponse("src/view/web/index.html")
    
    # Incluir el router del controlador
    app.include_router(web_controlador.router)
    
    # Iniciar el servidor
    uvicorn.run(app=app, host="127.0.0.1", port=8000)
