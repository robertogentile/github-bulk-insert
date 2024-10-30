TÍTULO
GitHub Bulk Permissions Manager

DESCRIÇÃO CURTA
Uma ferramenta em Python para gerenciar permissões em massa para repositórios do GitHub dentro de uma organização.

SEÇÃO: FUNCIONALIDADES
[emoji-rocket] Funcionalidades

- Busca repositórios por prefixo em uma organização
- Adiciona colaboradores em massa com permissões específicas
- Suporte a diferentes níveis de permissão (pull, push, admin, maintain, triage)
- Interface de linha de comando interativa
- Confirmação de segurança antes de aplicar alterações

SEÇÃO: PRÉ-REQUISITOS
[emoji-checklist] Pré-requisitos

- Python 3.8+
- Token de acesso pessoal do GitHub com permissões apropriadas
- Acesso de administrador à organização do GitHub

SEÇÃO: INSTALAÇÃO
[emoji-wrench] Instalação

1. Clone o repositório:
   COMANDO: git clone https://github.com/seu-usuario/git-bulk-actions.git
   COMANDO: cd git-bulk-actions

2. Crie e ative um ambiente virtual:
   COMANDO: python -m venv venv
   COMANDO-UNIX: source venv/bin/activate
   COMANDO-WINDOWS: venv\Scripts\activate

3. Instale as dependências:
   COMANDO: pip install -r requirements.txt

4. Configure as variáveis de ambiente:
   COMANDO: cp production.env.example production.env

SEÇÃO: CONFIGURAÇÃO
[emoji-gear] Configuração

1. Edite o arquivo production.env com suas configurações:
   VARIÁVEL: GITHUB_TOKEN="seu_token_do_github"
   VARIÁVEL: GITHUB_ORG="sua_organizacao"
   VARIÁVEL: REPO_PREFIX="prefixo_dos_repos"
   VARIÁVEL: COLLABORATOR_USERNAME="usuario_a_ser_adicionado"

ALERTA-IMPORTANTE:
- Nunca compartilhe ou comite seu token do GitHub
- O arquivo production.env está no .gitignore por segurança
- Gere um token com as permissões necessárias em: GitHub Settings > Developer Settings > Personal Access Tokens

SEÇÃO: USO
[emoji-rocket] Uso

Execute o script:
COMANDO: python add-user.py

O script irá:
1. Carregar as configurações do ambiente
2. Listar todos os repositórios encontrados com o prefixo especificado
3. Solicitar confirmação antes de adicionar o colaborador
4. Adicionar o colaborador a cada repositório com a permissão "maintain"

SEÇÃO: NÍVEIS DE PERMISSÃO
[emoji-key] Níveis de Permissão

O script suporta os seguintes níveis:
- pull: Acesso somente leitura
- push: Acesso de leitura e escrita
- admin: Acesso administrativo completo
- maintain: Acesso de gerenciamento sem configurações sensíveis
- triage: Acesso de gerenciamento somente leitura

SEÇÃO: FLUXO DE EXECUÇÃO
[emoji-chart] Fluxo de Execução

DIAGRAMA-MERMAID:
graph TD
    A[Início] --> B[Carrega Variáveis]
    B --> C[Conecta API GitHub]
    C --> D[Busca Repositórios]
    D --> E{Encontrou Repos?}
    E -->|Sim| F[Lista Repos]
    E -->|Não| M[Encerra]
    F --> G[Pede Confirmação]
    G --> H{Confirmado?}
    H -->|Sim| I[Adiciona Colaborador]
    H -->|Não| M
    I --> J[Rate Limit]
    J --> K{Mais Repos?}
    K -->|Sim| I
    K -->|Não| L[Concluído]
    L --> M[Fim]

SEÇÃO: SEGURANÇA
[emoji-warning] Notas de Segurança

- Sempre revise os repositórios listados antes de confirmar
- Use tokens com o mínimo de permissões necessárias
- Mantenha seus tokens seguros e nunca os compartilhe
- Revogue tokens comprometidos imediatamente

SEÇÃO: PROBLEMAS COMUNS
[emoji-bug] Resolução de Problemas

Se encontrar erro "No module named 'requests'":
COMANDO: pip install -r requirements.txt

Problemas de permissão:
1. Verifique se o token tem as permissões necessárias
2. Confirme se você é administrador da organização
3. Verifique se o token não expirou

SEÇÃO: CONTRIBUIÇÃO
[emoji-handshake] Contribuindo

Contribuições são bem-vindas! Por favor, sinta-se à vontade para submeter um Pull Request.

SEÇÃO: LICENÇA
[emoji-scroll] Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

SEÇÃO: SUPORTE
[emoji-phone] Suporte

Para reportar bugs ou solicitar funcionalidades, por favor abra uma issue no GitHub. 