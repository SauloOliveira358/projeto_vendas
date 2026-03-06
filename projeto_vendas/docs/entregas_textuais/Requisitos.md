# 1. Descrição dos Problemas da Empresa

Atualmente, a empresa utiliza planilhas eletrônicas como principal ferramenta para geração de relatórios gerenciais. Esse modelo apresenta diversas limitações, pois os gestores não possuem uma visão consolidada e integrada dos dados corporativos.

As informações encontram-se descentralizadas, não padronizadas e sem disponibilidade em tempo real, o que dificulta a análise das informações e compromete a tomada de decisões estratégicas.

Além disso, não existem mecanismos adequados de autenticação ou controle de acesso, o que pode comprometer a segurança e a confiabilidade das informações.

Outro problema relevante é a baixa escalabilidade desse modelo. À medida que o volume de dados aumenta, surgem dificuldades relacionadas a:

- perda de desempenho das planilhas  
- maior risco de inconsistência de dados  
- dificuldade de manutenção e controle das informações  

Diante desse cenário, torna-se necessária a implementação de um sistema centralizado de visualização e gestão de dados, que permita maior segurança, integração e eficiência no acesso às informações corporativas.

---

# 2. Requisitos Funcionais

## 2.1 Controle de Acesso
O sistema deverá possuir controle de acesso baseado em perfis de usuário, garantindo diferentes níveis de permissão de acordo com a função desempenhada dentro da organização.

## 2.2 Visualização de Dashboards via Web
O sistema deverá permitir a visualização de dashboards por meio de uma aplicação web, possibilitando acesso remoto aos dados de forma segura, sem a necessidade de instalação de softwares adicionais.

## 2.3 Apresentação Clara e Intuitiva dos Dados
Os dashboards deverão apresentar os dados de forma clara, objetiva e intuitiva, utilizando gráficos, indicadores e visualizações que facilitem a análise das informações e apoiem a tomada de decisão gerencial.

## 2.4 Exportação de Dados e Relatórios
O sistema deverá permitir a exportação de dados e relatórios, possibilitando sua utilização em outros sistemas ou para fins de análise externa, auditoria e compartilhamento em formatos amplamente utilizados.

## 2.5 Integração com o Banco de Dados Corporativo
O sistema deverá ser integrado ao banco de dados da empresa, garantindo atualização automática das informações, consistência dos dados e acesso em tempo real ou próximo do tempo real.

---

# 3. Requisitos Não Funcionais

## 3.1 Disponibilidade
O sistema deverá apresentar disponibilidade mínima de 99% do tempo, garantindo acesso contínuo aos usuários, exceto em períodos previamente programados para manutenção.

## 3.2 Escalabilidade
O sistema deverá ser capaz de suportar o crescimento do volume de dados e do número de usuários simultâneos, sem degradação significativa de desempenho.

## 3.3 Desempenho
O sistema deverá responder às requisições dos usuários em até 2 segundos, considerando condições normais de operação.

## 3.4 Segurança e Autenticação
O sistema deverá implementar mecanismos seguros de autenticação e controle de acesso, garantindo proteção das informações e prevenção de acessos não autorizados.

## 3.5 Usabilidade
O sistema deverá possuir interface intuitiva e de fácil utilização, permitindo que usuários com diferentes níveis de conhecimento técnico utilizem suas funcionalidades com mínima necessidade de treinamento.

## 3.6 Compatibilidade
O sistema deverá ser compatível com os principais navegadores web, garantindo funcionamento consistente em diferentes ambientes e plataformas.

---

# 4. Delimitação de Escopo

Neste primeiro momento, não fazem parte do escopo do projeto:

- Criação ou definição de novos indicadores de desempenho, sendo utilizados apenas os indicadores já existentes.
- Realização de treinamentos contínuos ou recorrentes para os usuários do sistema.
- Implementação de funcionalidades avançadas de análise de dados, como:
  - análises preditivas
  - mineração de dados
  - uso de técnicas de inteligência artificial

---

# 5. Justificativa dos Requisitos

## 5.1 Controle de Acesso
O controle de acesso é necessário para garantir que cada usuário tenha acesso apenas às informações e funcionalidades compatíveis com seu nível de permissão, preservando a segurança e a confidencialidade dos dados.

## 5.2 Visualização de Dashboards via Web
A visualização de dashboards via aplicação web permite que gestores e usuários autorizados acesssem informações estratégicas de forma rápida e remota, facilitando a análise dos dados e apoiando o processo de tomada de decisão.