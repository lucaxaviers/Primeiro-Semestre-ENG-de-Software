<div align="center">

# 🕵️ Jogo do Número Secreto em Python

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Tipo-Dedu%C3%A7%C3%A3o%20L%C3%B3gica-FF6F00?style=for-the-badge" alt="Tipo" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License" />
</p>

<p align="center">
  Jogo de dedução lógica e adivinhação onde os jogadores devem decifrar uma senha numérica de 4 dígitos com um sistema de dicas progressivas.
</p>

---

</div>

## 👥 Contribuidores do Projeto

<table align="center"> 
  <tr> 
    <td align="center" width="25%"> 
      <b>Arthur Grizone Silvestre de Oliveira</b>
    </td> 
    <td align="center" width="25%"> 
      <b>Lucas Rodrigues Xavier</b>
    </td>
    <td align="center" width="25%"> 
      <b>Mateus Oliveira Rafael</b>
    </td> 
    <td align="center" width="25%"> 
      <b>Wanderley Celestino Vieira Filho</b>
    </td> 
  </tr> 
</table>

---

## 🎮 Mecânica e Regras

1. **Número Secreto:** Gerado aleatoriamente entre `1000` e `9999`.
2. **Decomposição dos Dígitos:**
   - Milhar: `code // 1000`
   - Centena: `(code // 100) % 10`
   - Dezena: `(code // 10) % 10`
   - Unidade: `code % 10`
3. **Limite:** Até 10 tentativas por partida.
4. **Dicas Progressivas (a partir da 5ª tentativa):** Informa paridade (par/ímpar), dicas dimensionais (maior/menor) e posicionamento exato de dígitos acertados.

---

## 🚀 Como Executar

```bash
# Clonar o repositório
git clone https://github.com/lucaxaviers/jogo-secreto-python.git

# Acessar a pasta
cd jogo-secreto-python

# Executar
python JogoSecreto.py
```

---

<div align="center">
  <sub>Engenharia de Software — PUC-Campinas</sub>
</div>
