# 📊 Sistema de Registro de Acionamentos

Sistema web desenvolvido para registro, armazenamento e visualização de acionamentos operacionais, substituindo o uso exclusivo de planilhas Excel por uma solução mais estável, centralizada e escalável.

O projeto integra Microsoft Forms, Power Automate e Microsoft Teams, utilizando FastAPI para receber os dados automaticamente, armazená-los em um banco de dados e exibir indicadores em um dashboard web.

---

🎯 Objetivo

Centralizar o registro de acionamentos operacionais, aumentar a confiabilidade dos dados e fornecer uma base sólida para análise e tomada de decisão.

---

## 🚀 Visão Geral

Atualmente, os acionamentos são registrados via Microsoft Forms, notificados no Microsoft Teams e armazenados em Excel para geração de indicadores.  
Este sistema centraliza os dados em um banco de dados relacional, reduzindo riscos de inconsistência e facilitando a análise das informações.

---

Microsoft Forms
↓
Power Automate
↓
FastAPI (API)
↓
Banco de Dados
↓
Dashboard Web
↓
Microsoft Teams

---

## 📌 Funcionalidades

- Recebimento automático de acionamentos via Microsoft Forms
- Integração com Power Automate
- Armazenamento em banco de dados relacional
- Dashboard web com indicadores operacionais
- Visualização de:
  - Total de acionamentos
  - Acionamentos urgentes e normais
  - Último acionamento registrado
  - Distribuição por segmento, motivo e turno
- Estrutura preparada para futuras evoluções

---

## 🛠️ Tecnologias Utilizadas

- Python
- FastAPI
- Pydantic
- SQLAlchemy
- Banco de Dados Relacional (PostgreSQL / MySQL)
- Microsoft Forms
- Power Automate
- Microsoft Teams
- HTML, CSS e JavaScript

---
