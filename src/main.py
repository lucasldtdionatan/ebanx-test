from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from .router import router

app = FastAPI()
app.include_router(router)


@app.exception_handler(HTTPException)
def http_exception_handler(request, exc):
    if exc.status_code == status.HTTP_404_NOT_FOUND:
        return JSONResponse(content=0, status_code=status.HTTP_404_NOT_FOUND)

    return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})
