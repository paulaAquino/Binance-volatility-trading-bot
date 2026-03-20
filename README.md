# Binance Volitility Trading Bot

## Description
Este bot de trading para Binance analisa as variações de preço de todas as moedas na Binance e realiza operações nas mais voláteis.
Além disso, o algoritmo mantém o controle de todas as moedas compradas e as vende conforme o Stop Loss e Take Profit definidos por você.

O bot monitora as mudanças de preço em todas as moedas da Binance. Por padrão, apenas pares USDT são utilizados, excluindo pares de margem (como BTCDOWNUSDT) e pares Fiat.

> As informações abaixo são exemplos e totalmente configuráveis

- O bot verifica se alguma moeda subiu mais de 3% nos últimos 5 minutos
- O bot compra 100 USDT das moedas mais voláteis da Binance
- O bot vende ao atingir 6% de lucro ou 3% de stop loss

Você pode seguir o [guia do bot de volatilidade Binance](https://www.cryptomaton.org/2021/05/08/how-to-code-a-binance-trading-bot-that-detects-the-most-volatile-coins-on-binance/) para um passo a passo do desenvolvimento do bot (em inglês).

## LEIA ANTES DE USAR
1. Se você usar `TEST_MODE: False` no seu config, estará operando com DINHEIRO REAL.
2. Para evitar isso, SEMPRE confira o item `TEST_MODE` no arquivo config.yml.
3. Este é um framework para ser adaptado à sua estratégia, não uma solução pronta.
4. Dependendo do mercado, a configuração padrão pode não operar muito, adapte para sua estratégia.

## Uso
Consulte nossas páginas wiki (em inglês):

- [Guia de Instalação](https://github.com/CyberPunkMetalHead/Binance-volatility-trading-bot/wiki/Setup-Guide)
- [Guia de Estratégia do Bot](https://github.com/CyberPunkMetalHead/Binance-volatility-trading-bot/wiki/Bot-Strategy-Guide)
- [Guia de Configuração](https://github.com/CyberPunkMetalHead/Binance-volatility-trading-bot/wiki/Configuration)

## Rodando
- Iniciar env
''source .venv/bin/activate
- Rodar python3 detectedMooning.py
- Rodar testes unitários python3 -m unittest test_detectMoonings.py

## Solução de Problemas

1. Leia o [FAQ](FAQ.md)
2. Abra uma issue ou acesse o canal `#troubleshooting` no [Discord](https://discord.gg/buD27Dmvu3) 🚀
    - Não faça spam, não seja rude, este é um projeto open source, não um trabalho em tempo integral.

## 💥 Aviso Legal
Todas as estratégias de investimento envolvem risco de perda.
**Nada neste programa, scripts, código ou repositório deve ser interpretado como conselho de investimento.**
Qualquer referência a desempenho passado ou potencial não é, e não deve ser interpretada como, recomendação ou garantia de qualquer resultado ou lucro específico.
Ao usar este programa, você aceita toda a responsabilidade e não poderá fazer reivindicações contra os desenvolvedores ou outros envolvidos no projeto.