from fastapi import FastAPI

from routes import auth,about_services,comforts,comments,order,partners,services,users

from db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Shablon",
    responses={200: {'description': 'Ok'}, 201: {'description': 'Created'}, 400: {'description': 'Bad Request'},
               401: {'desription': 'Unauthorized'}}
)

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def home():
    return {"message": "Welcome"}


app.include_router(
    auth.login_router,
    prefix='/auth',
    tags=['User auth section'])

app.include_router(
    users.router_user,
    prefix='/user',
    tags=['Users section']

)

app.include_router(
    services.router_servic,
    prefix='/services',
    tags=['Services section']

)

app.include_router(
    about_services.router_about_servic,
    prefix='/about_services',
    tags=['About_services section']

)

app.include_router(
    partners.router_partner,
    prefix='/partners',
    tags=['Partners section']

)

app.include_router(
    order.router_order,
    prefix='/order',
    tags=['Orders section']

)

app.include_router(
    comments.router_comment,
    prefix='/comments',
    tags=['Comments section']

)

app.include_router(
    comforts.router_comfort,
    prefix='/comforts',
    tags=['Comforts section']

)
