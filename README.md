# Estrutura do Projeto

* **`data/`**: Armazena os dados do projeto.
  * **`raw/`**: dataset original
  * **`processed/`**: dados após limpeza e transformações
* **`notebooks/`**: Ambiente de experimentação. Contém análise exploratória (EDA), visualizações e testes iniciais de modelos antes da implementação final no código modular.
* **`src/`**: Núcleo do sistema de Machine Learning. Contém toda a lógica de:
  * Carregamento de dados
  * Pré-processamento
  * Treinamento
  * Avaliação
  * Salvamento do modelo
  É onde o pipeline de treino é executado.
* **`models/`**: Armazena os artefatos treinados. Inclui o modelo final (`.pkl`) e objetos auxiliares como scaler ou encoder.
* **`api/`**: Serviço de inferência. Contém a API responsável por:
  * Carregar o modelo treinado
  * Receber requisições
  * Retornar previsões em tempo real
* **`monitoring/`**: Módulos de monitoramento do modelo em produção. Inclui:
  * Registro de previsões
  * Monitoramento de métricas
  * Detecção de data drift
* **`tests/`**: Testes automatizados para garantir estabilidade do código e confiabilidade do pipeline.

* **Arquivos raiz**:
  * `requirements.txt` → dependências do projeto
  * `Dockerfile` → containerização da API
