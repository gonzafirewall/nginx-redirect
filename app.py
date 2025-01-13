from fastapi import FastAPI
from fastapi import Response
# import redirect response
from fastapi.responses import RedirectResponse
from fastapi.responses import HTMLResponse

app = FastAPI()

dominios = {
    "agencia-1": "viejo",
    "agencia-2": "nuevo"
}

@app.get("/{dominio}")
def read_root(dominio: str):
    tipo = dominios[dominio]
    if tipo == "nuevo":
        # Implementar redirect para usuario final
    return HTMLResponse("Aplication Python FastAPI <a href='/set-theme'>Set cookie</a>")


@app.get("/")
def read_root():
    if ""
    return HTMLResponse("Aplication Python FastAPI <a href='/set-theme'>Set cookie</a>")

@app.get("/set-theme")
def set_theme():
    # Set cookie to user to redirect to dark theme
    response = RedirectResponse(url="/")
    response.set_cookie("old-theme", "dark")
    return response


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)