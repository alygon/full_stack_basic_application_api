from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote
from sqlalchemy.exc import IntegrityError
from model import Session, Usuario, Comentario
from logger import logger
from schemas import *
from flask_cors import CORS

info = Info(title="BackEnd_API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
usuario_tag = Tag(name="Usuario", description="Adição, visualização e remoção de usuários à base")
comentario_tag = Tag(name="Comentario", description="Adição e visualização de comentários à base")

@app.get('/', tags=[home_tag])
def home():
    return redirect('/openapi')

@app.post('/usuario', tags=[usuario_tag],
          responses={"200": UsuarioViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_usuario(form: UsuarioSchema):
 
    usuario = Usuario(
        login=form.login,
        nome=form.nome)
    logger.debug(f"Adicionando usuário de login: '{usuario.login}'")
    try:
        # Criando conexão com a base
        session = Session()
        # Adicionando usuário
        session.add(usuario)
        # Efetivando o camando de adição de novo usuário na tabela
        session.commit()
        logger.debug(f"Adicionado usuário de login: '{usuario.login}'")
        return apresenta_usuario(usuario), 200

    except IntegrityError as e:
        error_msg = "Login de usuário já cadastrado!"
        logger.warning(f"Erro ao adicionar usuário! '{usuario.login}', {error_msg}")
        return {"mensagem": error_msg}, 409

    except Exception as e:
        error_msg = "Não foi possível cadastrar usuário!"
        logger.warning(f"Erro ao adicionar usuário '{usuario.login}', {error_msg}")
        return {"mensagem": error_msg}, 400


@app.get('/usuarios', tags=[usuario_tag],
         responses={"200": ListagemUsuariosSchema, "404": ErrorSchema})
def get_usuarios():
 
    logger.debug(f"Buscando usuários...")
    # Criando conexão com a base
    session = Session()
    # Fazendo a busca
    usuarios = session.query(Usuario).all()

    if not usuarios:
        # Se não há usuários cadastrados
        return {"usuarios": []}, 200
    else:
        logger.debug(f"%d Usuários encontrados" % len(usuarios))
        return apresenta_usuarios(usuarios), 200


@app.get('/usuario', tags=[usuario_tag],
         responses={"200": UsuarioViewSchema, "404": ErrorSchema})
def get_usuario(query: UsuarioBuscaSchema):
   
    login = query.login
    logger.debug(f"Buscando usuário... #{login}")
    # Criando conexão com a base
    session = Session()
    # Fazendo a busca
    usuario = session.query(Usuario).filter(Usuario.login == login).first()

    if not usuario:
        error_msg = "Usuário não encontrado na base!"
        logger.warning(f"Erro ao buscar usuário '{login}', {error_msg}")
        return {"mensagem": error_msg}, 404
    else:
        logger.debug(f"Usuário encontrado: '{usuario.login}'")
        return apresenta_usuario(usuario), 200


@app.delete('/usuario', tags=[usuario_tag],
            responses={"200": UsuarioDelSchema, "404": ErrorSchema})
def del_usuario(query: UsuarioBuscaSchema):

    usuario_login = unquote(unquote(query.login))
    logger.debug(f"Apagando dados do usuário #{usuario_login}")
    # Criando conexão com a base
    session = Session()
    countComentario = session.query(Comentario).filter(Comentario.usuario == usuario_login).delete()
    session.commit()
    count = session.query(Usuario).filter(Usuario.login == usuario_login).delete()
    session.commit()

    if count:
        logger.debug(f"Usuário apagado: #{usuario_login}")
        return {"mensagem": "Usuário removido", "login": usuario_login}
    else:
        error_msg = "Usuário não encontrado na base!"
        logger.warning(f"Erro ao apagar usuário #'{usuario_login}', {error_msg}")
        return {"mensagem": error_msg}, 404


@app.post('/comentario', tags=[comentario_tag],
          responses={"200": UsuarioViewSchema, "404": ErrorSchema})
def add_comentario(form: ComentarioSchema):
    
    login  = form.login
    logger.debug(f"Adicionando comentário do usuário #{login}")
    # Criando conexão com a base
    session = Session()

    usuario = session.query(Usuario).filter(Usuario.login == login).first()

    if not usuario:
        error_msg = "Usuário não encontrado na base!"
        logger.warning(f"Erro ao adicionar comentário do usuário '{login}', {error_msg}")
        return {"mensagem": error_msg}, 404

    # Criando o comentário
    descricao = form.descricao
    comentario = Comentario(descricao)

    # Adicionando o comentário pelo usuário
    usuario.adiciona_comentario(comentario)
    session.commit()

    logger.debug(f"Adicionado comentário do usuário #{login}")

    # Retorna a representação de produto
    return apresenta_usuario(usuario), 200