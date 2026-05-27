# desafio: criar um ventilador, um ar condicionado e um aquecedor usando o conceito de abstração

Para resoluçao deve seguir os passos a baixo:

a. abstração
b. modelagem (fluxograma)
c. logica (pseudocódigo)
d. código
e. organizacao

# 1. DEFINIÇAO: ventilador-soprador

Dispositivo que recebe 'energia eletrica' e converte em 'energia mecanica' de rotacao. 

O eixo é o meio de transformacao, e controle do fluxo de recebimento de energia, que resulta no  controle da velocidade das hélices para mover o ar.

Há uma relacao diretamente proporcional, no aumento de energia e no aumento da pressao do ar.

O que será traduzido em velocidades do ventilador, quanto maior a velocidade, maior também o consumo em kw.

--- REFORMULAÇAO

No ventilador

o motor recebe energia eletrica, que converterá em energia mecanica, promovendo o movimento de rotacao do motor que acionará a hélice, entrando no estado de ligado, na velocidade minima. 

Seu comportamento (velocidade) será alterado se houver alteracao (aumento ou diminuicao) na passagem de energia.

Tal comportamento alterará a rotacao e o fluxo de ar, resultando na quantidade de consumo.

O ventilador só para quando desligar for acionado.

## Modelagem geral
```fluxogram TD
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
 ├─ SIM → aumentar potência
 │        → aumentar rotação
 │        → aumentar fluxo de ar
 │        → aumentar consumo
 │
 └─ NÃO
↓
usuário desligou?
 ├─ NÃO → continuar funcionamento
 └─ SIM → interromper energia
          → estado = desligado
FIM
```


## 1.2 ESTRUTURA
### 1.2.1. Componentes
* motor
* eixo
* hélice
* fonte de energia

### 1.2.2. Comportamentos
* ligar
* desligar
* aumentar velocidade
* reduzir velocidade

### 1.2.3. Atributos
* velocidade
* consumo
* potencia
* estado ligado / desligado

## 1.3. VARIAVEIS
|-----------|-----------|--------|
| VARIAVEL  |    TIPO   | FUNÇAO |
|-----------|-----------|--------|
| estado | booleano | ligado / desligado |
| velocidade| inteiro | nivel atual |
| consumo | real | gasto energetico |
| potencia | real | força do motor |
|--------|----------|--------------|


## 1.4. TABELA ESTADOS
|-----------|-------------|------|
|VELOCIDADE | FLUXO DE AR | CONSUMO KW |
|-----------|-------------|------|
| 0 | desligado | 0 kw |
| 1 | baixo | 10 kw |
| 2 | médio | 20 kw |
| 3 | alto | 30 kw |
|-----------|-------------|------|

