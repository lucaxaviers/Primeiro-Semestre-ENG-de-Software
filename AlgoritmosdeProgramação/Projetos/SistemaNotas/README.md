<div align="center">

# 📝 Sistema de Gerenciamento de Notas em Python

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Dom%C3%ADnio-Gest%C3%A3o%20Acad%C3%AAmica-blue?style=for-the-badge" alt="Domínio" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License" />
</p>

<p align="center">
  Sistema acadêmico em Python para processamento de avaliações teóricas e práticas, médias ponderadas e emissão de situação final.
</p>

---

</div>

## 📐 Fórmulas Matemáticas

1. **Média Teórica ($MT$):**
   $$MT = 0.4 \times T_1 + 0.6 \times T_2$$
2. **Média Prática ($MP$):**
   $$MP = \frac{P_1 + P_2}{2}$$
3. **Média Final ($MF$):**
   - Se $MT > 5.0$ e $MP > 5.0$:
     $$MF = 0.3 \times MP + 0.7 \times MT$$
   - Caso contrário:
     $$MF = \min(MT, MP)$$

---

## 🚀 Como Executar

```bash
# Clonar o repositório
git clone https://github.com/lucaxaviers/sistema-notas-python.git

# Acessar o diretório
cd sistema-notas-python

# Executar
python SistemaNota.py
```

---

<div align="center">
  <sub>Desenvolvido no contexto de Engenharia de Software</sub>
</div>
