## API Evolution

A API Evolution disponibiliza endpoints para integração com o projeto.

### Como rodar

```bash
uvicorn api_evolution:app --reload
```

### Endpoints disponíveis

- `/evolution/status` – Verifica o status da API.

### Como consumir

Exemplo usando `requests` em Python:

```python
import requests

response = requests.get("http://localhost:8000/evolution/status")
print(response.json())
```
