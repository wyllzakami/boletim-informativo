# Boletim Informativo 2.0 — ambiente de teste

Esta branch mantém a demonstração da versão 1.0 em `main` sem alterações.

O pacote da aplicação 2.0 está dividido em arquivos `bundle-v2-00.b64` até `bundle-v2-08.b64`. O serviço de teste no Render reconstrói o diretório da aplicação durante o build.

## Configuração usada no Render

- Branch: `boletim-2.0-teste`
- Runtime: Node.js
- Build:
  `cat bundle-v2-*.b64 | base64 -d > /tmp/boletim-v2.tar.gz && tar -xzf /tmp/boletim-v2.tar.gz -C .`
- Start:
  `npm --prefix boletim-informativo start`
- Health check: `/health`

## Primeiro administrador

O primeiro administrador é inicializado por variáveis de ambiente protegidas no Render:
- `BOOTSTRAP_ADMIN_USERNAME`
- `BOOTSTRAP_ADMIN_EMAIL`
- `BOOTSTRAP_ADMIN_PASSWORD`

Não armazene os valores dessas variáveis neste repositório. Não inclua arquivos `.env` ou `data.json` no commit.

## Limitações do ambiente de teste

A aplicação ainda usa armazenamento local `data.json` e sessões em memória. A camada gratuita do Render não fornece disco persistente. Portanto, cadastros, publicações e sessões podem ser perdidos em reinicializações ou novos deploys. Não use dados institucionais confidenciais até migrar para banco persistente, configurar backups e restringir o acesso por rede privada/VPN.
