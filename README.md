# Port Scanner

Um port scanner TCP desenvolvido em Python como projeto prático de estudos em cibersegurança.

O projeto foi criado para consolidar conhecimentos de **Redes, Linux, Python e Git**, evoluindo gradualmente conforme novos conceitos são estudados.

## Estado atual

**v0.1.0 — versão funcional inicial**

Atualmente, o programa consegue:

* Receber um endereço IP como alvo
* Receber um intervalo de portas para verificação
* Validar entradas numéricas das portas
* Rejeitar portas fora do intervalo válido (`1–65535`)
* Tratar entradas inválidas, números negativos e valores decimais
* Realizar a verificação de portas TCP utilizando `socket.connect_ex()`

> **Nota:** a validação do endereço IP ainda será aprimorada nas próximas versões.

## Tecnologias

* Python 3
* TCP/IP
* Python `socket`
* Linux
* Git

## Como executar

Clone o repositório e execute:

```bash
python3 main.py
```

O programa solicitará o endereço IP de destino e o intervalo de portas que deverá ser analisado.

## Roadmap

### v0.2.0

* [ ] Validação adequada de endereços IPv4
* [ ] Resolução de hostname/domínio
* [ ] Melhor tratamento de erros de rede
* [ ] Melhor organização do código

### v0.3.0

* [ ] Implementação de threads para execução concorrente
* [ ] Melhoria de desempenho
* [ ] Definição de timeout configurável

### Futuro

* [ ] Identificação de serviços/portas comuns
* [ ] Detecção básica de banners
* [ ] Argumentos via linha de comando
* [ ] Opções de saída e geração de relatórios
* [ ] Testes automatizados

## Objetivo

Este projeto faz parte da minha jornada prática em **cibersegurança e segurança ofensiva**, servindo como laboratório para transformar conceitos estudados em ferramentas funcionais.

O foco é evoluir o projeto de forma incremental, documentando as decisões e aprendizados ao longo do desenvolvimento.

## Aviso

Use esta ferramenta somente em sistemas e redes que você possui ou tem autorização explícita para testar.

## Autor

**volktain**

Projeto desenvolvido para fins educacionais e de estudo em cibersegurança.
