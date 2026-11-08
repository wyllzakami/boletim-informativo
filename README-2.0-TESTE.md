# Boletim Informativo 2.2.0 — ambiente de apresentação

Esta branch contém a versão de apresentação 2.2.0. A branch `main` permanece separada.

## Recursos incluídos

- Acesso interno com cadastro por solicitação e aprovação administrativa.
- Perfis: leitor, publicador, administrador secundário e Administrador Principal.
- Administradores secundários podem apoiar a gestão de usuários comuns, publicações, destaques, convites e registros.
- Somente o Administrador Principal pode promover, rebaixar, suspender ou reativar administradores secundários. A conta principal é protegida contra alterações pelas demais contas.
- Comunicados com imagem, links e um anexo PDF opcional (até 4 MB).
- PDF validado no servidor e disponível apenas para usuários autenticados.
- Até cinco destaques fixos, ordenação administrativa e navegação para o comunicado original.
- Validade e arquivamento automático de comunicados.
- Convites por QR Code com aprovação posterior do cadastro.

## Configuração de execução

- Branch: `boletim-2.0-teste`
- Runtime: Node.js 18+
- Build: `cat bundle-v2-*.b64 | base64 -d > /tmp/boletim-v2.tar.gz && tar -xzf /tmp/boletim-v2.tar.gz -C .`
- Start: `npm --prefix boletim-informativo start`
- Health check: `/health`

## Administrador Principal inicial

A conta inicial é criada por variáveis protegidas no Render:
- `BOOTSTRAP_ADMIN_USERNAME`
- `BOOTSTRAP_ADMIN_EMAIL`
- `BOOTSTRAP_ADMIN_PASSWORD`

Não armazene esses valores neste repositório. Em bases existentes, a inicialização identifica/designa uma conta principal. Nunca compartilhe os segredos nem inclua `.env` ou dados de usuários no commit.

## Limitações importantes

Esta é uma demonstração para avaliação, não uma instalação pronta para uso institucional. A aplicação ainda usa `data.json`, sessões em memória e arquivos locais. O serviço gratuito do Render tem armazenamento efêmero: contas, publicações, sessões e anexos podem ser perdidos em reinicializações ou novos deploys.

Não utilize informações pessoais, escalas, dados de RH ou documentos confidenciais neste ambiente. Antes do uso real, migrar para PostgreSQL, sessões persistentes e armazenamento durável de anexos; configurar backups com restauração testada; restringir acesso por rede privada/VPN; e realizar revisão de segurança e privacidade com a TI.

## Evolução após aprovação

A futura versão multiunidade deverá modelar empresa, região, unidade (CD/loja) e setor em uma única aplicação, com permissões por escopo e comunicados locais ou gerais. A identidade visual, logotipo e paleta institucional serão aplicados após a validação da empresa.