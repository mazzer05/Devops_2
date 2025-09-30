from fastapi import APIRouter, FastAPI

app = FastAPI(title="My FastAPI Application")

@app.get("/")
def read_root():
    return {'message': 'Welcome to the FastAPI application!'}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='localhost', port=8000)