from fastapi import FastAPI, Depends, Body, Query, HTTPException
from typing import Annotated
from sqlalchemy.orm import Session
from datetime import datetime
from db import Base, SessionLocal, Link, engine
from urllib.parse import urlparse

# create table
Base.metadata.create_all(bind=engine)

app = FastAPI()


# send db-session object to function
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
def return_domains(
        from_time: Annotated[int, Query(alias="from")] = 0,
        to_time: Annotated[int, Query(alias="to")] = float('inf'),
        db: Session = Depends(get_db)):
    links = db.query(Link).all()
    result = {"domains": []}
    for i in links:
        if from_time > to_time:
            raise HTTPException(status_code=400, detail="date error")
        if from_time <= i.time <= to_time:
            url = urlparse(i.domains).netloc
            if url in result["domains"]:
                continue
            else:
                result["domains"].append(url)
    return result, {"status": "ok"}


@app.post("/visited_links")
def accept_links(data=Body(), db: Session = Depends(get_db)):
    for link in data['links']:
        links = Link()
        links.domains = link
        links.time = int(datetime.now().timestamp())
        db.add(links)
    db.commit()
    return {"status": "ok"}
