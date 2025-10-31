# 🍽️ Restaurante Sky Lounge

Um sistema completo de **gerenciamento de reservas para restaurante**, desenvolvido com **Django**, **HTML5**, **CSS**, **JavaScript** e o pacote **Django Widget Tweaks**.  
O objetivo do projeto é permitir que clientes realizem reservas online e que o administrador do restaurante gerencie as reservas através de um painel administrativo seguro e intuitivo.

---

## 🚀 Funcionalidades

### 👥 Público (Clientes)
- Fazer reserva online de forma simples.
- Consultar o status das reservas enviando nome e e-mail.
- Interface responsiva e moderna.

### 🧑‍💼 Administrador (Staff)
- Login protegido (acesso exclusivo para staff).
- Listagem de todas as reservas.
- Atualização de status: **Confirmada**, **Pendente**, **Cancelada**.
- Edição e exclusão de reservas diretamente no painel.
- Visualização das reservas futuras de forma organizada.

---

## 🛠️ Tecnologias Utilizadas

| Camada | Tecnologia |
|--------|-------------|
| Backend | 🐍 Django (Python 3.x) |
| Frontend | 🌐 HTML5, CSS3, JavaScript |
| Estilização | 🎨 Bootstrap 5 |
| Template Engine | 🧩 Django Templates |
| Extensões | ⚙️ Django Widget Tweaks |
| Banco de Dados | 💾 SQLite (padrão) |

---

## 📁 Estrutura de Pastas

projeto_restaurante/
│
├── app/
│ ├── migrations/
│ ├── static/
│ │ ├── css/
│ │ ├── js/
│ │ └── img/
│ ├── templates/
│ │ └── app/
│ │ ├── base.html
│ │ ├── login.html
│ │ ├── lista_reserva.html
│ │ ├── fazer_reserva.html
│ │ ├── minhas_reservas.html
│ │ └── editar_reserva.html
│ ├── forms.py
│ ├── models.py
│ ├── urls.py
│ └── views.py
│
├── projeto_restaurante/
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│ └── asgi.py
│
├── manage.py
└── README.md

# Projeto_restaurante
Projeto Final utilizando o fremwork CRUD!   

---


--- 


👨‍💻 Autor

Cleyton Durans
📧 cleytondurans.n@gmail.com

💼 Projeto desenvolvido para estudos e prática com Django e Front-End moderno.


## ⚙️ Instalação e Configuração

### 1️⃣ Clonar o repositório



git clone https://github.com/seuusuario/projeto-restaurante.git
cd projeto-restaurante
