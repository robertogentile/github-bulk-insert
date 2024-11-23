# GitHub Bulk Permissions Manager

> Uma ferramenta para gerenciar permissões em massa no GitHub

![GitHub](https://img.shields.io/badge/github-bulk_manager-blue)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green)

## 📝 Descrição

Automatiza a gestão de permissões de colaboradores em múltiplos repositórios GitHub dentro de uma organização.

## ✨ Funcionalidades

- 👥 Adiciona/Remove colaboradores em massa
- 🔍 Busca repositórios por prefixo
- 💻 Interface interativa em linha de comando
- ⚡ Validação de configurações em tempo real
- 🔒 Confirmação de segurança em operações críticas
- 🚦 Controle automático de rate limiting

## 📋 Pré-requisitos

- Python 3.8 ou superior
- Token de acesso pessoal do GitHub
- Acesso de administrador à organização
- Dependências listadas em requirements.txt

## 🚀 Instalação

1. Clone o repositório:
    git clone https://github.com/robertogentile/git-bulk-actions.git
    cd git-bulk-actions

2. Crie ambiente virtual:
    # Unix/macOS
    python -m venv venv
    source venv/bin/activate

    # Windows
    python -m venv venv
    .\venv\Scripts\activate

3. Instale dependências:
    pip install -r requirements.txt

4. Configure ambiente:
    cp production.env.example production.env

## ⚙️ Configuração

Edite o arquivo production.env:

    GITHUB_TOKEN="seu_token_do_github"
    GITHUB_ORG="sua_organizacao"
    REPO_PREFIX="prefixo_dos_repos"
    COLLABORATOR_USERNAME="usuario"

> ⚠️ **IMPORTANTE**: Nunca compartilhe ou comite seu token do GitHub

## 💻 Uso do Programa

Execute:
    python main.py

### Menu Principal

1. Adicionar Colaborador
2. Remover Colaborador
3. Verificar Configuração
4. Sair

## 🔄 Fluxo de Operação

1. Selecione a operação desejada
2. Confirme ou atualize as configurações
3. Revise a lista de repositórios afetados
4. Confirme a execução
5. Acompanhe o progresso

## 🔑 Níveis de Permissão

| Permissão | Descrição |
|-----------|-----------|
| pull      | Acesso somente leitura |
| push      | Leitura e escrita |
| admin     | Acesso administrativo total |
| maintain  | Gerenciamento sem admin |
| triage    | Gerenciamento somente leitura |

## 🐛 Resolução de Problemas

### Erro: No module named 'requests'
    pip install -r requirements.txt

### Erro de Permissão
- Verifique permissões do token
- Confirme acesso de administrador
- Verifique validade do token

### Rate Limiting
- Aguarde alguns minutos
- Verifique limites da API

## 🔒 Segurança

> **AVISOS IMPORTANTES**:
> - Nunca compartilhe tokens
> - Revise repositórios antes de confirmar
> - Use permissões mínimas necessárias
> - Monitore logs após operações em massa

## 📞 Suporte

Para reportar problemas ou sugerir melhorias:
[Abra uma issue](https://github.com/robertogentile/git-bulk-actions/issues)

---

<div align="center">

**Desenvolvido por Roberto Gentile**  
Licença MIT - 2024

</div>