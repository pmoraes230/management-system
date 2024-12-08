# Backlog - Gerenciador de VT e VA

## Funcionalidades Implementadas

### 1. **Estrutura Inicial do Projeto**
   - Criado a estrutura de pastas com organização para facilitar a manutenção.
   - Estrutura de diretórios definida para os módulos:
     - `app/`: Componentes, páginas e lógica do aplicativo.
     - `assets/`: Imagens, ícones e fontes.
     - `backend/`: Lógica de conexão com banco de dados e operações com dados.
     - Arquivo principal `main.py` configurado para iniciar o aplicativo.
   
### 2. **Implementação da HomePage**
   - Página inicial com saudação e descrição breve do sistema.
   - Adicionada explicação sobre o gerenciamento de VT e VA.
   - Botões de navegação para acessar outras páginas:
     - "Consultar Benefícios"
     - "Cadastrar Novo Benefício"
   - Estilização da página com fontes personalizadas e elementos centralizados.

### 3. **Sidebar**
   - Implementação de uma barra lateral (Sidebar) com botões de navegação:
     - Botões para "Home", "Cadastro" e "Consulta".
     - Cada botão conectado a funções de navegação (ainda com funcionalidade simples de redirecionamento).

### 4. **Pages (Cadastro e Consulta)**
   - Criação de estrutura básica para páginas de cadastro e consulta de benefícios, com funcionalidade inicial de navegação entre elas.

### 5. **Layout e Estilo (QSS)**
   - Utilização de QSS para personalização visual:
     - Arquivo `main.qss` para estilização global do sistema.
     - Estilos para a barra lateral (`sidebar.qss`) e as páginas principais.

### 6. **Integração Inicial com Banco de Dados**
   - Estrutura de banco de dados e integração com a aplicação prevista, embora a parte de manipulação de dados ainda esteja em andamento.

## Melhorias e Implementações Futuras

### 1. **Estilização Avançada**
   - Implementar tema escuro e claro para o sistema.
   - Adicionar animações e transições nas páginas ao navegar.
   - Melhorar os botões com ícones e efeitos de hover.

### 2. **Funcionalidade de Cadastro Completo**
   - Criar formulário de cadastro de benefícios com campos de entrada (ex: valor, tipo de benefício, data de validade).
   - Implementar validações para o formulário (campos obrigatórios, formatos de entrada, etc.).
   - Conectar o formulário ao banco de dados para registrar informações.

### 3. **Tela de Consulta de Benefícios**
   - Exibir a lista de benefícios cadastrados com filtros de busca (ex: nome do funcionário, tipo de benefício).
   - Adicionar funcionalidades de edição e exclusão de registros.
   - Implementar paginação para a listagem de dados se houver muitos registros.

### 4. **Conectar com Banco de Dados**
   - Finalizar a integração com o banco de dados para armazenar, consultar, editar e excluir dados de benefícios.
   - Usar SQLite ou MySQL para armazenar as informações de benefícios (a definir).

### 5. **Gráficos e Relatórios**
   - Adicionar gráficos para visualizar dados de benefícios (ex: valor total de VT/VA, comparações por tipo de benefício, etc.).
   - Gerar relatórios em formatos como PDF ou Excel para exportação dos dados.

### 6. **Funções de Navegação**
   - Melhorar a navegação entre páginas, garantindo que as transições sejam suaves e intuitivas.
   - Implementar um mecanismo de "histórico" de navegação para que o usuário possa retornar às páginas anteriores.

### 7. **Segurança e Autenticação**
   - Implementar um sistema de login e autenticação de usuários, com controle de permissões.
   - Criar diferentes níveis de acesso para administradores e usuários (ex: apenas administradores podem cadastrar ou editar dados).

### 8. **Testes Automatizados**
   - Implementar testes automatizados para as funcionalidades principais (cadastro, consulta, navegação).
   - Garantir que a aplicação funcione corretamente em diferentes plataformas (Windows, Linux, macOS).

### 9. **Melhorias na Interface**
   - Adicionar um sistema de feedback visual para o usuário (mensagens de sucesso/erro).
   - Melhorar a interface para dispositivos de diferentes tamanhos (responsividade).

### 10. **Documentação**
   - Escrever documentação técnica detalhada sobre a estrutura do código, como rodar a aplicação, configurar o banco de dados, etc.
   - Criar um guia do usuário final para explicar como utilizar o sistema.
# Backlog - Gerenciador de VT e VA

## Funcionalidades Implementadas

### 1. **Estrutura Inicial do Projeto**
   - [x] Criado a estrutura de pastas com organização para facilitar a manutenção.
   - [x] Estrutura de diretórios definida para os módulos:
     - `app/`: Componentes, páginas e lógica do aplicativo.
     - `assets/`: Imagens, ícones e fontes.
     - `backend/`: Lógica de conexão com banco de dados e operações com dados.
     - Arquivo principal `main.py` configurado para iniciar o aplicativo.
   
### 2. **Implementação da HomePage**
   - [x] Página inicial com saudação e descrição breve do sistema.
   - [x] Adicionada explicação sobre o gerenciamento de VT e VA.
   - [x] Botões de navegação para acessar outras páginas:
     - "Consultar Benefícios"
     - "Cadastrar Novo Benefício"
   - [x] Estilização da página com fontes personalizadas e elementos centralizados.

### 3. **Sidebar**
   - [x] Implementação de uma barra lateral (Sidebar) com botões de navegação:
     - Botões para "Home", "Cadastro" e "Consulta".
     - Cada botão conectado a funções de navegação (ainda com funcionalidade simples de redirecionamento).

### 4. **Pages (Cadastro e Consulta)**
   - [x] Criação de estrutura básica para páginas de cadastro e consulta de benefícios, com funcionalidade inicial de navegação entre elas.

### 5. **Layout e Estilo (QSS)**
   - [x] Utilização de QSS para personalização visual:
     - Arquivo `main.qss` para estilização global do sistema.
     - Estilos para a barra lateral (`sidebar.qss`) e as páginas principais.

### 6. **Integração Inicial com Banco de Dados**
   - [x] Estrutura de banco de dados e integração com a aplicação prevista, embora a parte de manipulação de dados ainda esteja em andamento.

## Melhorias e Implementações Futuras

### 1. **Estilização Avançada**
   - [ ] Implementar tema escuro e claro para o sistema.
   - [ ] Adicionar animações e transições nas páginas ao navegar.
   - [ ] Melhorar os botões com ícones e efeitos de hover.

### 2. **Funcionalidade de Cadastro Completo**
   - [ ] Criar formulário de cadastro de benefícios com campos de entrada (ex: valor, tipo de benefício, data de validade).
   - [ ] Implementar validações para o formulário (campos obrigatórios, formatos de entrada, etc.).
   - [ ] Conectar o formulário ao banco de dados para registrar informações.

### 3. **Tela de Consulta de Benefícios**
   - [ ] Exibir a lista de benefícios cadastrados com filtros de busca (ex: nome do funcionário, tipo de benefício).
   - [ ] Adicionar funcionalidades de edição e exclusão de registros.
   - [ ] Implementar paginação para a listagem de dados se houver muitos registros.

### 4. **Conectar com Banco de Dados**
   - [ ] Finalizar a integração com o banco de dados para armazenar, consultar, editar e excluir dados de benefícios.
   - [ ] Usar SQLite ou MySQL para armazenar as informações de benefícios (a definir).

### 5. **Gráficos e Relatórios**
   - [ ] Adicionar gráficos para visualizar dados de benefícios (ex: valor total de VT/VA, comparações por tipo de benefício, etc.).
   - [ ] Gerar relatórios em formatos como PDF ou Excel para exportação dos dados.

### 6. **Funções de Navegação**
   - [ ] Melhorar a navegação entre páginas, garantindo que as transições sejam suaves e intuitivas.
   - [ ] Implementar um mecanismo de "histórico" de navegação para que o usuário possa retornar às páginas anteriores.

### 7. **Segurança e Autenticação**
   - [ ] Implementar um sistema de login e autenticação de usuários, com controle de permissões.
   - [ ] Criar diferentes níveis de acesso para administradores e usuários (ex: apenas administradores podem cadastrar ou editar dados).

### 8. **Testes Automatizados**
   - [ ] Implementar testes automatizados para as funcionalidades principais (cadastro, consulta, navegação).
   - [ ] Garantir que a aplicação funcione corretamente em diferentes plataformas (Windows, Linux, macOS).

### 9. **Melhorias na Interface**
   - [ ] Adicionar um sistema de feedback visual para o usuário (mensagens de sucesso/erro).
   - [ ] Melhorar a interface para dispositivos de diferentes tamanhos (responsividade).

### 10. **Documentação**
   - [ ] Escrever documentação técnica detalhada sobre a estrutura do código, como rodar a aplicação, configurar o banco de dados, etc.
   - [ ] Criar um guia do usuário final para explicar como utilizar o sistema.
