# Instruções Copilot para o Bot de Volatilidade Binance

## Visão Geral do Projeto
- Este bot monitora todas as moedas da Binance (padrão: pares USDT, excluindo margem/fiat) e opera nas mais voláteis.
- A lógica principal está em `detectMoonings.py`.
- Configuração via `config.yml` (estratégia, pares, risco) e `creds.yml` (chaves de API, veja `creds.example.yml`).
- Módulos auxiliares em `helpers/` fazem o parsing de config/creds.
- Sinais e estratégias customizadas podem ser adicionados via `signalsamplemod.py`, `custsignalmod.py` e o diretório `signals/`.
- Utilitários (ex: `utilities/sell-remaining-coins.py`) permitem gestão manual de trades.

## Padrões e Convenções-Chave
- Toda configuração/credencial é carregada em tempo de execução; nunca coloque segredos no código.
- Use `parse_args()` e `load_config()` de `helpers/parameters.py` para argumentos e configs.
- Chaves de API são acessadas via `helpers/handle_creds.py`.
- O log usa um wrapper customizado com timestamp e cores no console.
- A lógica de trading é orientada a eventos: polling de preços, checagem de volatilidade, gatilhos de compra/venda e acompanhamento de P&L da sessão.
- Sinais são lidos/escritos como arquivos em `signals/` (veja `signalsamplemod.py`).
- Exclusão de pares (ex: FIATS) e seleção de moedas são controladas no `config.yml`.

## Fluxos de Trabalho do Desenvolvedor
- **Rodar o bot principal:** `python3 Binance\ Detect\ Moonings.py` (garanta config/creds corretos)
- **Modo de teste:** Defina `TEST_MODE: True` no `config.yml` para evitar trades reais.
- **Vender todas as moedas:** `python3 utilities/sell-remaining-coins.py`
- **Adicionar novos sinais:** Implemente em `signals/` ou como novo arquivo `*_mod.py`.
- **Debug:** Use a flag `--debug` para log detalhado.
- **Soluções de problemas:** Veja `FAQ.md` para erros comuns.

## Integração & Dependências
- Depende dos pacotes Python `binance` e `tradingview_ta`.
- Todas as chaves de API externas devem ser válidas e testadas (veja `test_api_key()` em `helpers/handle_creds.py`).
- Módulos de análise de mercado (ex: `pausebotmod.py`) usam TradingView TA para checagem de mercado.

## Exemplos
- Para trocar os pares negociados, edite `PAIR_WITH` e `FIATS` em `config.yml`.
- Para adicionar novo sinal de compra/venda, crie um módulo em `signals/` seguindo o padrão de `signalsamplemod.py`.
- Para pausar operações conforme o mercado, use ou estenda `pausebotmod.py`.

## Cuidados
- **Nunca defina `TEST_MODE: False` a menos que queira operar com dinheiro real.**
- Sempre valide as chaves de API e config antes de rodar em produção.
- Este é um framework, não uma solução pronta—adapte a lógica para sua estratégia.

---
Para mais detalhes, veja `README.md`, `FAQ.md` e os links da wiki no README.
