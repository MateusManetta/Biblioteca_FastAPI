# 1. Objetivo - Criar uma api que disponibiliza a consulta, criação edição e exclusão de livros
# 2. URL Base - localhost
# 3. Endpoints - 
    # - localhost/livros (GET)
    # - localhost/livros (POST)
    # - localhost/livros/id (GET)
    # - localhost/livros/id (PUT)
    # - localhost/livros/id (DELETE)

# 4. Quais recursos: Livros

from typing import Union

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Livro(BaseModel):
    id: int
    titulo: str
    autor: str



# Fonte de dados
livros = [
    Livro(id=1,
          titulo='O Senhor dos Anéis - A Sociedade do Anel',
          autor='J.R.R Tolkien'
          ),
    Livro(id=2,
          titulo='Harry Potter e a Pedra Filosofal',
          autor='J.K Howling'
          ),
    Livro(id=3,
          titulo='James Clear',
          autor='Hábitos Atômicos'
          ),
          ]


# Consultar (todos)
@app.get("/livros")
def obter_livros():
    return livros


# Consultar (id)
@app.get('/livros/{livro_id}')
def obter_livro_por_id(livro_id: int):
    for livro in livros:
        if livro.id == livro_id:
            return livro


# Criar
@app.post('/livros')
def incluir_novo_livro(livro: Livro):
    livros.append(livro)
    return livros


# Editar
@app.put('/livros/{livro_id}')
def editar_livro_por_id(livro_id: int, livro_editado : Livro):
    for livro in livros:
        if livro.id == livro_id:
            livro.autor = livro_editado.autor
            livro.titulo = livro_editado.titulo
            return livro
    raise HTTPException(status_code=404, detail="Livro não encontrado")


@app.delete('/livros/{livro_id}')
def excluir_livros(livro_id: int):
    for indice, livro in enumerate(livros):
        if livro.id == livro_id:
            del livros[indice]
            return livros
    raise HTTPException(status_code=404, detail="Livro não encontrado")
