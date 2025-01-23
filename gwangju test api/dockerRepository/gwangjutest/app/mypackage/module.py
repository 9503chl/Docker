import sys,os,random,string,io
# FastAPI 관련 임포트
from fastapi import FastAPI,Form,File, UploadFile
from fastapi.responses import FileResponse
from fastapi.responses import StreamingResponse
from typing import List
from starlette.middleware.cors import CORSMiddleware
# SQLAlchemy 관련 임포트 
from sqlalchemy import (
    Column,
    Integer, 
    String,
    BLOB,
    create_engine
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import (
    sessionmaker,
    scoped_session
)

# Pydantic 관련 임포트
from pydantic import BaseModel

db_userName = "root"
db_userPassword = "ehdcns12!"
mariadb_container_name = "mariadb"
db_port = "3306"
db_tableName = "edudb"