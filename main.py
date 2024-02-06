from fastapi import FastAPI, Depends, Body
from sqlalchemy.orm import Session
from datetime import datetime
from db import Base, SessionLocal, Link, engine

# create table
Base.metadata.create_all(bind=engine)

app = FastAPI()


# passing db-session object to function
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close


@app.get("/")
def read_root():
    return "Welcome to a test task from SBER!"


@app.get("/visited_domains")
def return_domains(from_time: int = None, to_time: int = None, db: Session = Depends(get_db)):
    if from_time and to_time:
        links = db.query(Link).filter(from_time < Link.time < to_time)
        return links, {"status": "ok"}
    else:
        links = db.query(Link).all()
        result = {"domains": []}
        for i in links:
            result["domains"].append(i.domains)
        return result, {"status": "ok"}


@app.post("/visited_links")
def accept_links(data=Body(), db: Session = Depends(get_db)):
    for link in data['links']:
        links = Link()
        links.domains = link
        links.time = int(datetime.now().timestamp())
        db.add(links)
    db.commit()
    # db.refresh(links)
    return {"status": "ok"}
