# app_diagnostico_defeitos_ar_cond

# Diagnóstico Automático de Falhas em Ar-Condicionado

#### Descrição do Projeto
Este projeto tem como objetivo desenvolver uma aplicação web que permita aos usuários diagnosticar falhas em sistemas de ar-condicionado. A aplicação utiliza um banco de dados SQLite contendo informações sobre problemas comuns, possíveis causas e testes sugeridos. Os usuários podem descrever um problema, e a aplicação fornece respostas baseadas em correspondências exatas ou aproximadas utilizando técnicas de processamento de linguagem natural.

#### Tecnologias usadas
* Streamlit: Framework utilizado para construir a interface da aplicação web.
* SQLite: Sistema de gerenciamento de banco de dados utilizado para armazenar informações sobre diagnósticos.
* FuzzyWuzzy: Biblioteca utilizada para realizar comparações de similaridade entre strings.
* NLTK: Biblioteca de processamento de linguagem natural que fornece funcionalidades para remoção de stopwords.
* Unidecode: Biblioteca para remoção de acentos e normalização de texto.

Estrutura do Banco de Dados
O banco de dados contém uma tabela chamada diagnosticos com a seguinte estrutura:

Coluna	             Tipo	    Descrição
problema	        TEXT	    Descrição do problema do ar-condicionado
possiveis_causas	TEXT	    Causas potenciais do problema
teste	            TEXT	    Testes recomendados para diagnóstico

#### Funcionamento da Aplicação
* Entrada do Usuário: O usuário descreve o problema do ar-condicionado em um campo de texto.
* Processamento do Texto: A entrada do usuário é normalizada (removendo acentos e convertendo para minúsculas) e as stopwords são removidas.
* Busca no Banco de Dados:
Primeiro, a aplicação tenta encontrar correspondências exatas no banco de dados.
Se não houver correspondências exatas, a aplicação realiza uma busca fuzzy para encontrar correspondências aproximadas.
* Resultados: A aplicação exibe as possíveis causas e testes sugeridos ao usuário, categorizados como correspondências exatas ou aproximadas.

#### Código
O código principal da aplicação é organizado da seguinte forma:

* Importações: Bibliotecas necessárias são importadas.

Funções:
* preprocessar_texto(texto): Normaliza e limpa o texto.
* conectar_banco(): Estabelece conexão com o banco de dados SQLite.
* buscar_diagnostico(problema): Busca causas e testes com base no problema informado.
* Interface com o Usuário: A interface é construída utilizando Streamlit, permitindo interatividade e exibição de resultados.

#### Considerações Finais
Este projeto pode ser expandido para incluir mais funcionalidades, como:

* Uma interface administrativa para adicionar ou editar diagnósticos no banco de dados.
* Integração com APIs para obter informações adicionais sobre os problemas.
* Melhorias no processamento de texto para lidar com sinônimos e variações de termos.

#### Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

