# PT - Síndrome Gripal em Sergipe (2021-2024) 🏥📊
Este repositório contém um pipeline de dados baseado na arquitetura medalhão para o processamento e análise de casos de síndrome gripal no estado de Sergipe, utilizando dados públicos do Gov.br.

🔗 Fonte dos Dados

Os dados utilizados neste projeto foram obtidos a partir do portal dados.gov.br, nos seguintes links:

- [Notificações de Síndrome Gripal 2021](https://dados.gov.br/dados/conjuntos-dados/notificacoes-de-sindrome-gripal-leve-2021)  
- [Notificações de Síndrome Gripal 2022](https://dados.gov.br/dados/conjuntos-dados/notificacoes-de-sindrome-gripal-leve-2022)  
- [Notificações de Síndrome Gripal 2023](https://dados.gov.br/dados/conjuntos-dados/notificacoes-de-sindrome-gripal-leve-2023)  
- [Notificações de Síndrome Gripal 2024](https://dados.gov.br/dados/conjuntos-dados/notificacoes-de-sindrome-gripal-leve-2024)

📂 Armazenamento e Processamento
- Armazenamento: Os dados são armazenados no Azure Data Lake Gen2.
- Transformação: O processamento ocorre no Databricks, utilizando PySpark para a transformação e enriquecimento dos dados.
- Segurança: A Access Key utilizada para acessar os dados está armazenada de forma segura no Azure Key Vault.

🏅 Arquitetura Medalhão

O pipeline segue a arquitetura medalhão e cada camada está armazenada em uma pasta diferente no Data Lake:  
- Bronze: Armazena os dados brutos exatamente como foram extraídos da fonte.  
- Silver: Realiza a limpeza, padronização e filtragem dos dados.  
- Gold: Contém os dados prontos para análise e geração de insights.

⚙️ Workflow no Databricks

O Workflow possui três tasks diferentes, uma para escrita em cada camada:
- casos-bronze : Realiza leitura da camada raw e escrita na bronze a partir do notebook bronze.dbc
- casos-silver : Realiza leitura da camada bronze e escrita na silver a partir do notebook silver.dbc
- casos-gold: Realiza leitura da camada silver e escrita na gold a partir do notebook gold.dbc

![workflow](https://github.com/user-attachments/assets/e982c0c9-83b7-4ea7-917e-5ac1618c7cf6)


📌 Diagrama da Solução
  
![casos_sindrome_gripal (2)](https://github.com/user-attachments/assets/3314a285-b502-4d00-9ee9-5c37d051dff5)


# EN - Flu Syndrome in Sergipe (2021-2024) 🏥📊
This repository contains a data pipeline based on the medallion architecture for processing and analyzing flu syndrome cases in the state of Sergipe, using public data from Gov.br.

🔗 Data Sources

The data used in this project was obtained from the dados.gov.br portal at the following links:

- [Notificações de Síndrome Gripal 2021](https://dados.gov.br/dados/conjuntos-dados/notificacoes-de-sindrome-gripal-leve-2021)  
- [Notificações de Síndrome Gripal 2022](https://dados.gov.br/dados/conjuntos-dados/notificacoes-de-sindrome-gripal-leve-2022)  
- [Notificações de Síndrome Gripal 2023](https://dados.gov.br/dados/conjuntos-dados/notificacoes-de-sindrome-gripal-leve-2023)  
- [Notificações de Síndrome Gripal 2024](https://dados.gov.br/dados/conjuntos-dados/notificacoes-de-sindrome-gripal-leve-2024)

📂 Storage and Processing
- Storage: Data is stored in Azure Data Lake Gen2.
- Transformation: Processing is done in Databricks, using PySpark and SQL for data transformation and enrichment.
- Security: The Access Key used to access the data is securely stored in Azure Key Vault.

🏅 Medallion Architecture

The pipeline follows the medallion architecture, with each layer stored in a different folder in the Data Lake:
- Bronze: Stores raw data exactly as extracted from the source.
- Silver: Cleans, standardizes, and filters the data.
- Gold: Contains data ready for analysis and insights.

⚙️ Databricks Worfklow

The workflow consists of three different tasks, one for writing in each layer:
- casos-bronze: Reads from the raw layer and writes to bronze using the bronze.dbc notebook.
- casos-silver: Reads from the bronze layer and writes to silver using the silver.dbc notebook.
- casos-gold: Reads from the silver layer and writes to gold using the gold.dbc notebook.

![workflow](https://github.com/user-attachments/assets/e982c0c9-83b7-4ea7-917e-5ac1618c7cf6)


📌 Solution Diagram
  
![casos_sindrome_gripal (2)](https://github.com/user-attachments/assets/3314a285-b502-4d00-9ee9-5c37d051dff5)




