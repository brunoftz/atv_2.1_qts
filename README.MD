# Projeto TDD - testes unitarios, funcionais e e2e

---

## Instruções de Execução

### Requisitos

- Python 3.12+
- pip
- virtualenv (opcional)

### Instalação

**1. Clonar o repositório**
```bash
git clone <URL_DO_REPOSITORIO>
cd nome-do-projeto
```

**2. Criar ambiente virtual**
```bash
python -m venv venv
```

**3. Ativar ambiente virtual**

Windows:
```bash
venv\Scripts\activate
```

Linux/Mac:
```bash
source venv/bin/activate
```

**4. Instalar dependências**
```bash
pip install -r requirements.txt
```

### Execução da Aplicação

```bash
python run.py
```

A aplicação será executada em: `http://localhost:5000`


## Testes

Executar todos os testes:
```bash
pytest
```

---

## TDD

O projeto utiliza a abordagem **Test Driven Development**:

-  **RED** — criação de testes que inicialmente falham
-  **GREEN** — implementação mínima para passar nos testes
-  **REFACTOR** — melhoria do código mantendo os testes passando

Evidências podem ser encontradas nos commits e na evolução incremental das funcionalidades.


## Evidências do Test Driven Development

Prints em `/evidencia_tdd` e enviados na entrega da atividade, indicam:

- **img1:** teste executado retornando erro
- **img2:** função no momento do erro
- **img3:** função refatorada
- **img4:** teste com sucesso pós refatoração
