# 📦 Consulta de Ordens de Compra – Sênior

## 📄 Descrição

Este projeto realiza o consumo da **API nativa de Ordens de Compra da Sênior**, com o objetivo de facilitar, padronizar e automatizar a consulta e o processamento dos dados de compras.

A aplicação foi desenvolvida para atuar como um **serviço backend**, responsável por buscar informações diretamente da API da Sênior, tratar os dados conforme as regras de negócio e disponibilizá-los para uso interno ou integração com outros sistemas.

---

## 🏗️ Arquitetura do Projeto

O projeto foi desenvolvido em **Python**, seguindo uma arquitetura modular e organizada, baseada em boas práticas de separação de responsabilidades.

Estrutura de diretórios:

* **app** – Inicialização da aplicação
* **api** – Definição das rotas e endpoints
* **config** – Configurações gerais da aplicação
* **core** – Componentes centrais e regras base
* **database** – Configuração e acesso ao banco de dados
* **dto** – Data Transfer Objects
* **helpers** – Funções auxiliares
* **mappers** – Conversão e mapeamento de dados
* **repository** – Acesso e persistência de dados
* **services** – Regras de negócio e integrações
* **usecase** – Casos de uso da aplicação
* **utils** – Utilitários gerais

Essa abordagem facilita a manutenção, testes, escalabilidade e evolução do projeto.

---

## ⚙️ Orquestração e Execução

Todo o fluxo da aplicação é **orquestrado pelo FastAPI**, que atua como o motor principal do serviço.

O sistema foi projetado para ser executado de forma **automática e recorrente**, com execução **diária**, garantindo que os dados de ordens de compra estejam sempre atualizados.

---

## 🛠️ Tecnologias Utilizadas

* **Python**
* **FastAPI**
* **HTTP Clients / Requests**
* **Arquitetura em camadas**
* **Integração com API REST (Sênior)**

---

## 🎯 Objetivo

* Facilitar a consulta de Ordens de Compra
* Centralizar o consumo da API da Sênior
* Padronizar o tratamento dos dados
* Automatizar o processo de atualização diária

---

## 📌 Observações

Este projeto foi desenvolvido com foco em **robustez**, **clareza estrutural** e **facilidade de manutenção**, podendo ser expandido para novos endpoints ou regras de negócio conforme a necessidade.

---

📌 *Projeto em constante evolução.*
