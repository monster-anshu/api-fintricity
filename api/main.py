from fastapi import FastAPI
from Router.Onboarding import main as Onboarding
app = FastAPI()


app.include_router(Onboarding.router)

@app.get('/')
def get_root():
    return { "info" : "Appilication runnig"}