# Desafio: Abstração de Dispositivos Climáticos

Projeto desenvolvido para praticar conceitos fundamentais de programação e modelagem computacional utilizando abstração.

O objetivo é criar:

- ventilador
- ar-condicionado
- aquecedor

seguindo etapas de análise, modelagem lógica e implementação.

---

# Etapas do Projeto

Para resolver o desafio, o desenvolvimento seguirá as etapas abaixo:

1. Abstração
2. Modelagem (fluxograma)
3. Lógica (pseudocódigo)
4. Código
5. Organização do projeto

---

# 1. Ventilador / Soprador

## 1.1 Definição

O ventilador é um dispositivo que recebe energia elétrica e a converte em energia mecânica de rotação.

O motor aciona o eixo, que transmite o movimento para as hélices, promovendo o fluxo de ar.

O comportamento do ventilador depende da quantidade de energia recebida:

- maior energia
- maior rotação
- maior fluxo de ar
- maior consumo energético

---

## 1.2 Reformulação Computacional

No ventilador:

- o motor recebe energia elétrica;
- a energia é convertida em movimento de rotação;
- o eixo transmite o movimento para a hélice;
- o sistema entra no estado `ligado`;
- o ventilador inicia na velocidade mínima.

Seu comportamento pode ser alterado através do aumento ou redução da passagem de energia.

A alteração da energia modifica:

- velocidade
- rotação
- fluxo de ar
- consumo energético

O ventilador permanece funcionando até que o comando de desligamento seja acionado.

---

# 1.3 Modelagem Geral

```text
INÍCIO
↓
receber energia
↓
acionar motor
↓
mover eixo
↓
girar hélices
↓
estado = ligado
↓
velocidade = mínima
↓
consumo = mínimo
↓
usuário altera velocidade?

├─ SIM
│   ↓
│ aumentar potência
│ aumentar rotação
│ aumentar fluxo de ar
│ aumentar consumo
│
└─ NÃO

↓
usuário desligou?

├─ NÃO → continuar funcionamento
│
└─ SIM
    ↓
 interromper energia
 estado = desligado

FIM
```

---

# 1.4 Estrutura do Sistema

## 1.4.1 Componentes

- motor
- eixo
- hélice
- fonte de energia

---

## 1.4.2 Comportamentos

- ligar
- desligar
- aumentar velocidade
- reduzir velocidade

---

## 1.4.3 Atributos

- velocidade
- consumo
- potência
- estado (ligado/desligado)

---

# 1.5 Variáveis do Sistema

| Variável   | Tipo      | Função                    |
|------------|-----------|----------------------------|
| estado     | booleano  | ligado / desligado         |
| velocidade | inteiro   | nível atual                |
| consumo    | real      | gasto energético           |
| potencia   | real      | força do motor             |

---

# 1.6 Tabela de Estados

| Velocidade | Fluxo de Ar | Consumo |
|------------|-------------|----------|
| 0          | desligado   | 0 kw     |
| 1          | baixo       | 10 kw    |
| 2          | médio       | 20 kw    |
| 3          | alto        | 30 kw    |

---

# Próximas Etapas

- [ ] Criar fluxograma visual
- [ ] Desenvolver pseudocódigo
- [ ] Implementar em Python
- [ ] Criar versão orientada a objetos
- [ ] Adicionar ar-condicionado
- [ ] Adicionar aquecedor
- [ ] Melhorar organização do projeto

---

# Objetivo de Estudo

Este projeto foi criado para praticar:

- abstração
- lógica de programação
- modelagem computacional
- algoritmos
- organização de projetos
- programação em Python
- orientação a objetos
