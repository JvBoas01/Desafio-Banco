Desáfio DIO


# 🏦 Banco V2.1 — Sistema Bancário em Python

Um sistema bancário de terminal desenvolvido em **Python**, com suporte a criação de contas, clientes, depósitos, saques e extratos.  
Este projeto foi desenvolvido com base em **Programação Orientada a Objetos (POO)**, utilizando **classes, herança, abstração e encapsulamento**.

---

## 📋 Funcionalidades

- 👤 **Cadastro de clientes (Pessoa Física)**
- 💳 **Criação de contas correntes**
- 💰 **Depósitos**
- 💸 **Saques (com limite diário e de valor)**
- 📄 **Visualização de extrato**
- 📜 **Listagem de contas cadastradas**
- ⚙️ **Controle de transações com limite diário**
- 🧩 **Histórico detalhado de transações**
- 🧠 **Uso de classes abstratas e decoradores para log**

---

## 🧱 Estrutura do Projeto

```
BancoV2.1.py
```

O código é composto por diversas classes:

### 🔹 Classe `Cliente`
Representa um cliente genérico. Armazena endereço e lista de contas associadas.

### 🔹 Classe `PessoaFisica`
Herda de `Cliente`. Adiciona CPF, nome e data de nascimento.

### 🔹 Classe `Conta`
Modelo base para contas bancárias. Possui saldo, número, agência e histórico de transações.

### 🔹 Classe `ContaCorrente`
Especialização de `Conta`. Define limites de saque e quantidade máxima de saques.

### 🔹 Classe `Historico`
Registra todas as transações (saques e depósitos) realizadas na conta.

### 🔹 Classes `Transacao`, `Saque` e `Deposito`
Usam abstração para representar transações genéricas e suas subclasses específicas.

### 🔹 Decorador `@log_transacao`
Registra automaticamente logs de data e hora para cada operação executada.

---

## 🖥️ Menu Principal

Ao executar o programa, o usuário verá o seguinte menu interativo no terminal:

```
======== BOSS BANK ========
[1] Depositar
[2] Sacar
[3] Extrato
[4] Nova conta
[5] Listar contas
[6] Novo usuário
[0] Sair
```

---

## 🚀 Como Executar

### Pré-requisitos
- Python 3.8 ou superior instalado.

### Passos
1. Clone ou baixe o projeto:
   ```bash
   git clone https://github.com/JvBoas01/BancoV2.0.git
   cd BancoV2.0
   ```

2. Execute o script:
   ```bash
   python BancoV2.0.py
   ```

3. Interaja pelo menu no terminal.

---

## ⚙️ Exemplo de Uso

```
======== BOSS BANK ========
[6] Novo usuário
Informe o CPF (somente número): 12345678900
Informe o nome completo: João Victor
Informe a data de nascimento (dd-mm-aaaa): 01-01-2000
Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): Rua X, 123 - Centro - São Paulo/SP

=== Cliente criado com sucesso! ===
```

---

## 📈 Regras de Negócio

- Cada cliente pode ter **várias contas**.
- O limite de **saques diários** é **3**.
- O valor máximo de **saque por transação** é **R$ 1.500,00**.
- Cada conta possui um **histórico de transações** com data e hora.
- Cada cliente pode realizar **até 2 transações por dia** (para simular limites operacionais).

---

## 🧩 Conceitos Utilizados

- **Programação Orientada a Objetos (POO)**
  - Abstração (`class Transacao`)
  - Herança (`PessoaFisica` herda de `Cliente`)
  - Encapsulamento (atributos privados com `@property`)
  - Polimorfismo (`Saque` e `Deposito`)
- **Iteradores personalizados**
- **Decoradores**
- **Geradores e filtros**
- **Tratamento de erros e validações**

---

## 🧑‍💻 Autor

**João Victor**  
📧 Email: joaoboas@proton.me
💼 GitHub: github.com/JvBoas01

---

## 🪪 Licença

Este projeto é de uso livre para fins educacionais e de estudo.  
Sinta-se à vontade para modificar e expandir.
