# 📢 Fala, Povo!

**Fala, Povo!** é uma plataforma web que permite à população registrar denúncias e solicitações relacionadas a problemas urbanos em sua cidade, como iluminação pública defeituosa, buracos nas ruas, acúmulo de lixo, entre outros.

Este projeto foi desenvolvido como parte da Atividade Extensionista II do curso de Análise e Desenvolvimento de Sistemas — UNINTER.

---

## 🔎 Funcionalidades

- ✅ Envio de denúncias com formulário completo
- ✅ Opção de denúncia anônima
- ✅ Upload de anexos (imagens, vídeos e arquivos)
- ✅ Visualização de denúncias registradas (com privacidade)
- ✅ Layout responsivo e visual leve com CSS puro

---

## 🚀 Acesse o projeto

🔗 [Clique aqui para acessar a versão online](https://fala-povo-hw2s.onrender.com)

---

## 🛠 Tecnologias utilizadas

- Python 3.12
- Flask (microframework web)
- HTML5 + CSS3 personalizados (sem frameworks externos)
- JSON (como banco de dados leve)
- Hospedagem via Render

---

## 📁 Estrutura do projeto

```
fala-povo/
│
├── static/            # Arquivos estáticos
├── templates/         # Páginas HTML
├── uploads/           # Anexos enviados pelos usuários
├── app.py             # Lógica principal da aplicação Flask
├── denuncias.json     # Armazena todas as denúncias
├── README.md          # Este arquivo
└── requirements.txt   # Dependências do projeto
```

---

## 🧾 Como rodar o projeto localmente

1. Clone o repositório:

   ```bash
   git clone https://github.com/annalu1z4/fala-povo.git
   cd fala-povo
   ```

2. Crie um ambiente virtual (opcional, mas recomendado):

   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Inicie o servidor:

   ```bash
   python app.py
   ```

5. Acesse no navegador:
   ```
   http://localhost:5000
   ```

---

## 📎 Observações

- Os arquivos enviados pelos usuários ficam na pasta `/uploads` e podem ser baixados diretamente via link na tela de denúncias.
- A visualização pública **oculta dados pessoais** por padrão.
- A aplicação aceita arquivos `.jpg`, `.jpeg`, `.png`, `.mp4` com limite de 10MB.

---

## 👩‍💻 Autoria

Projeto desenvolvido por **Anna Luiza**  
Curso de **Análise e Desenvolvimento de Sistemas — UNINTER**  
Atividade Extensionista II — 2025

---

## 💬 Licença

Este projeto é acadêmico e não possui licença comercial. Uso livre com fins educacionais.
