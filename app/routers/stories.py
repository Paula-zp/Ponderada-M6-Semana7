# Arquivo responsável por definir as rotas relacionadas as histórias
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import schemas, crud, database, dependencies

router = APIRouter(prefix="/stories", tags=["stories"])

# Dependência para obter a sessão do banco de dados
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rota para listar todas as histórias
@router.get("/", response_model=List[schemas.Story])
def read_stories(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    stories = crud.get_stories(db, skip=skip, limit=limit)
    return stories

# Rota para adicionar uma nova história
@router.post("/", response_model=schemas.Story)
def create_story(story: schemas.StoryCreate, user_id: int, db: Session = Depends(get_db)):
    return crud.create_story(db=db, story=story, user_id=user_id)

# Rota para obter uma história pelo ID
@router.get("/{story_id}", response_model=schemas.Story)
def read_story(story_id: int, db: Session = Depends(get_db)):
    db_story = crud.get_story(db, story_id=story_id)
    if db_story is None:
        raise HTTPException(status_code=404, detail="Story not found")
    return db_story

# Rota para atualizar uma história
@router.put("/{story_id}", response_model=schemas.Story)
def update_story(story_id: int, story: schemas.StoryUpdate, db: Session = Depends(get_db)):
    db_story = crud.get_story(db, story_id=story_id)
    if db_story is None:
        raise HTTPException(status_code=404, detail="Story not found")
    return crud.update_story(db=db, story_id=story_id, story_update=story)

# Rota para deletar uma história
@router.delete("/{story_id}", response_model=schemas.Story)
def delete_story(story_id: int, db: Session = Depends(get_db)):
    db_story = crud.get_story(db, story_id=story_id)
    if db_story is None:
        raise HTTPException(status_code=404, detail="Story not found")
    return crud.delete_story(db=db, story_id=story_id)

# Rota para gerar conteúdo para uma história
@router.post("/{story_id}/generate-content", response_model=schemas.Story)
def generate_story_content(story_id: int, prompt: str, db: Session = Depends(get_db)):
    db_story = crud.get_story(db, story_id=story_id)
    if db_story is None:
        raise HTTPException(status_code=404, detail="Story not found")
    
    content = dependencies.generate_story_content(prompt)
    db_story.content = db_story.content + "\n" + content if db_story.content else content
    
    db.commit()
    db.refresh(db_story)
    return db_story
