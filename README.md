# Síndrome Gripal em Sergipe (2021-2024) 🏥📊
Este repositório contém um pipeline de dados baseado na arquitetura medalhão para o processamento e análise de casos de síndrome gripal no estado de Sergipe, utilizando dados públicos do Gov.br.

📂 Armazenamento e Processamento
- Armazenamento: Os dados são armazenados no Azure Data Lake Gen2.
- Transformação: O processamento ocorre no Databricks, utilizando PySpark para a transformação e enriquecimento dos dados.
- Segurança: A Access Key utilizada para acessar os dados está armazenada de forma segura no Azure Key Vault.

🏅 Arquitetura Medalhão
- O pipeline segue a arquitetura medalhão e cada camada está armazenada em uma pasta diferente no Data Lake:  
- Bronze: Armazena os dados brutos exatamente como foram extraídos da fonte.  
- Silver: Realiza a limpeza, padronização e filtragem dos dados.  
- Gold: Contém os dados prontos para análise e geração de insights.  

📌 Diagrama da Solução
  
![casos_sindrome_gripal (2)](https://github.com/user-attachments/assets/3314a285-b502-4d00-9ee9-5c37d051dff5)

