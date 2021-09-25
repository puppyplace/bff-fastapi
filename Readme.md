# Bff FastApi


### Python
Versão 3.8


### Para desenvolvimento

1. Criação do venv

```
python -m venv .venv
```

2. Ativar o venv local

```
source .venv/bin/activate
```

3. Instalar as dependencias

```
pip install -r requirements.txt
```

4. Iniciar o app

```
uvicorn main:app --reload
```

### Como iniciar docker

Comando docker

```
sudo docker run -p 8000:80 -it bff-fastapi
```
