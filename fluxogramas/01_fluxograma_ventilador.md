# Ventilador

## Objetivo
Simular funcionamento do ventilador assoprador.

## Fluxograma
```flowchart TB

    A["inicio"] --> B("recebe energia")
    B --> C("aciona motor")
    C --> D("mover eixo")
    D --> E("girar hélice")
    E --> F("estado = ligado = velocidade minima")
    
    F --> G{"alterar velocidade?"}
    G -- sim --> H("aumentar passagem de energia")
    H --> I("aumentar rotacao")
    I --> J("aumentar fluxo de ar")
    J --> K("aumentar consumo KW")
    
    G -- nao --> L{"usuario desligou?"}
    K --> L
    L -- sim --> M("interromper energia")
    M --> N("estado = desligado")
    N --> O["fim"]
    L -- nao --> P("continuar funcionando")
    P --> G

    style F fill:#C8E6C9
    style G fill:#FFF9C4
    style H fill:#FFF9C4
    style I fill:#FFF9C4
    style J fill:#FFF9C4
    style K fill:#FFF9C4
    style L fill:#FFCDD2
    style P fill:#C8E6C9
```

## Pseudocódigo
```text
INICIO

Ligar ventilador

Enquanto o ventilador estiver ligado:
    motor será acionado
    eixo irá se mover
    hélice irá girar, na velocidade minima

    Se o usuario alterar a velocidade:
        energia irá aumentar
        rotacao irá aumentar
        fluxo de ar irá aumentar

    Se nao:
        interrompe a energia
        desliga o ventilador
    
FIM

```