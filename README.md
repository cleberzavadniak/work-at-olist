# Work at Olist

Yeap, Olist is a nice place to work.


Tem algum falante nativo de inglês que lerá isso durante a análise do
teste? Eu espero que não. Se for o caso, por favor me avisem.

Estou escrevendo **em português** porque gosto de fazer com que esse tipo
de teste sirva, da minha parte, como uma espécie **material de estudos**
para quem quer que se interesse a fuçar nos meus repositórios públicos.

Portanto, mesmo que eu consiga escrever bem em inglês, prefiro usar meu
idioma nativo, já que é o que eu domino **muito** mais e me permite me
expressar da melhor maneira possível, de forma que **outros eventuais
leitores** possam tirar o máximo de proveito do texto.


Começarei documentando a API, mas logo em seguida comento mais
extensivamente a respeito dos vários tópicos ligados a esse projeto.

## A API

```python
BASE_URL = "https://cz-work-at-olist.herokuapp.com/"
```

* Todas as URLs representando recursos **precisam** ter a barra (`/`) no
  final.
* **Nenhuma** URL representando um documento deve ter a barra (`/`) no
  final.

(Porque isso é o certo.)

### Endpoints

(Aqui, em inglês, já que me parece **tão** mais natural escrever
documentação técnica assim...)

* `v1/records/start/` : CallStartRecords list
* `v1/records/start/<id>`
* `v1/records/end/` : CallEndRecords list
* `v1/records/end/<id>`
* `v1/bills/bill/<source>` : The Bill for a specific source. You can pass
  `period` as query parameter, like `period=03/1986`.
* `v1/bills/charge-entries/` : ChargeEntries list.
* `v1/bills/charge-entries/<id>`

### Create new records

```javascript
POST /v1/records/start/
{
    "call_id": 99,
    "timestamp": "1970-12-25 12:34:56",
    "source": "AAXXXXXXXX",
    "destination": "AAXXXXXXXX"
}
```

```javascript
POST /v1/records/end/
{
    "call_id": 99,
    "timestamp": "1970-12-25 12:34:56",
}
```

### Create new charge entries

You can't do that!

### Get the bill

```javascript
GET /v1/bills/bill/AAXXXXXXXX

->

{
    "price": "1099.90",
    "entries": [
        {
            "destination": "AAXXXXXXXY", 
            "start_date": "1970-25-12"
            "start_time": "12:34:56",
            "duration": 30,
            "price": "78.12"
        },
        ...
    ]
}
```

## Install

You must have a **Postgres** database available. Set `DATABASE_URL`
environment variable properly.

Set `SECRET_KEY` environment variable to any random value (or put it
inside `piririm/.env` file).

```bash
$ git clone 'git@github.com:cleberzavadniak/work-at-olist.git'
$ cd work-at-olist
$ # Activate your virtual environment preferred tool.
$ # Mine is https://github.com/pyenv/pyenv .
$ pip install -U -r requirements/test.txt
```

## Test

You must have a **Postgres** test database available. Set `DATABASE_URL`
environment variable properly. The test database name should be equal the
"production" database name prefixed with `test_`.

Set `SECRET_KEY` environment variable to any random value (or put it
inside `piririm/.env` file).

```bash
$ cd work-at-olist
$ # Activate your virtual environment preferred tool.
$ # Mine is https://github.com/pyenv/pyenv .
$ cd piririm
$ pytest
```

## Work environment

* Laptop Asus Intel Core i5, 8GB RAM;
* Linux Mint;
* lxterm;
* zsh;
* pyenv;
* vim.

See https://sanctum.geek.nz/arabesque/series/unix-as-ide/ .

## Commit history

O caminho desde o *fork* até a versão funcional e publicada no Heroku foi
percorrido por **8 commits**:

* First draft (1): responsável pelo **boilerplate** do Django e demais
  ferramentas. É uma "versão funcional", já que é possível rodar vários
  comandos do `manage.py`, mas não faz nenhum trabalho.
* Models (2): como o problema é até simples, fiz a **modelagem dos dados**
  antes de qualquer outra coisa.
* Método "charge" (1): responsável por tentar **registrar as cobranças**
  toda vez que um registro chega. Já que não se pode contar com ordem (ou
  seja, que um "end" chegará necessariamente depois do respectivo
  "start"), a tentativa é feita para qualquer tipo de registro.
* APIs (2): responsáveis pela implementação das **APIs REST básicas**,
  para criação e recuperação de CallRecords e ChargeEntries. Esses
  endpoints são os que considero "bem comportados" de acordo com as
  melhores práticas para APIs REST.
* Endpoint da "bill": implementei à parte, já que me parece o endpoint
  **mais heterodoxo** e, especialmente, com a especificação mais "frouxa".

Como você pode ver, cada *commit* representa uma nova funcionalidade,
sendo que todos são realmente significativos e, a princípio,
"*deployable*".

Curiosamente, o capítulo 6 das minhas [Diretrizes de
Desenvolvimento](https://cleber.netlify.com/clebercaverna/#cl%C3%A9ber/CTO/diretrizes/)
fala brevemente sobre isso.

### git: ciclos curtos

**Ciclos curtos de implementação são melhores que ciclos longos**.
É melhor ter implementações atômicas que aceitam facilmente um `git
rebase` do que sofrer com *branches* cheios de diversas novas
funcionalidades que requerem um `git merge` geralmente complicado e que
expõe a base de código a regressões (geralmente bem estúpidas).

## Design

### 12 factor app

Vide o capítulo 3 das minhas [Diretrizes de
Desenvolvimento](https://cleber.netlify.com/clebercaverna/#cl%C3%A9ber/CTO/diretrizes/).

### Powerlibs

Quando trabalhei na Olist, usávamos Django e o `Django Rest Framework`.
Gosto muito do primeiro e absolutamente detesto o segundo. Os motivos
precisariam de um artigo completo, mas, basicamente, posso dizer sobre
o "DRF":

* O código é macarrônico e difícil de navegar.
* Ele obriga a repetir muita bobagem, como ficar escrevendo
  serializadores, que geralmente ficam vazios.
* Certa vez, ainda na Olist, eu fiquei indignado com tanto código se
  repetindo e tentei automatizar as coisas, já que a maioria das APIs era
  **muito** simples. Fiquei uma semana lidando nisso e, no fim, meio que
  desisti, porque o DRF é cheio de "mágica" e, portanto, se você não
  seguir à risca tudo o que ele manda fazer, você fica numa pior, porque
  certas coisas simplesmente param de funcionar sem uma explicação
  decente. (E se você quiser descobrir os motivos, terá que ler o código
  terrível e macarrônico da biblioteca).

Por isso, logo que entrei na DroneMapp, cuidei de procurar uma alternativa
mais simples e encontrei o `django-restless`, que acabou sendo incorporado
dentro de um conjunto de bibliotecas que me ajudariam a desenvolver [APIs
REST](https://medium.com/clebertech/o-guia-definitivo-para-constru%C3%A7%C3%A3o-de-apis-rest-470d0c885fe1)
de maneira mais sã, [as Powerlibs](https://github.com/DroneMapp).

Com as Powerlibs eu consigo escrever um serviço REST HTTP com pouquíssimo
esforço. Veja o `piririm/apps/records/views.py`, por exemplo.

(Saiba mais em
https://medium.com/dronemapp/dronemapp-software-livre-e-as-powerlibs-19d5330c0c71)

### "utils"

O Osvaldo Santana sempre ficava ressabiado ao ver esses "utils", mas
acredito que meu motivo é bom o bastante. Talvez eu até devesse chamar
esse módulo de "mixins", já que a ideia é manter ali código que seja
**comum a todas as apps**, como o gerador de ULID e o modelo base que usa
isso como `id`.

`utils.endpoints`, por exemplo, define classes para serem usadas nas
*views*, já com os métodos padrão (somente GET e POST), assim como
a implementação de busca e paginação.

(A busca é feita usando-se os campos dos modelos como *query parameters*
e a paginação com `_limit` e `_offset`.)

### ULIDs

Se tem algo que aprendi nessa vida de desenvolvedor web é que **IDs
numéricos são geralmente algo ruim**. E é curioso que as pessoas os usem
sem absolutamente pensar a respeito.

Veja só, o ID numérico é, sozinho, uma informação praticamente inútil,
enquanto um ULID me permite fazer uma varredura em todos os meus
modelos/tabelas, se necessário for, já que posso considerá-lo **único
dentro do sistema todo**.


É claro que há alguma consideração a ser feita com relação ao
**desempenho** no banco de dados, mas não me parece que isso torne-se um
problema tão rápido ao ponto de abrir-se mão das benesses do ULID tão
cedo. O problema, se houver, só vem depois de alguns anos, provavelmente,
e enquanto ele não chega, não há um bom motivo para que os mantenedores do
sistema fiquem privados delas.

## Arquitetura

### O método "charge"

**Seria muito melhor usar eventos**. Sério.

Há várias abordagens para a geração de eventos. A Olist, se não me engano,
costuma gerar os eventos nos **modelos** do Django. Eu, na DroneMapp,
achei melhor [gerar eventos nas
views](https://medium.com/clebertech/o-dequeuer-3fcb40e75463), mas,
recentemente, descobri uma maneira ainda mais interessante de fazer isso.

Estou começando a guiar meu pensamento de arquiteto de sistemas pelo
esforço para evitar A Grande Pilha de Merda (sobre a qual pretendo falar
em detalhes em breve), ou seja, evitar que as camadas "de baixo" vão sendo
subutilizadas enquanto arranjamos desculpas para, ao invés de otimizá-las,
**adicionar ainda outras camadas** e, assim, formar-se uma "GPM".

Por isso, pelo que entendo hoje, **o ideal seria deixar que o Postgres
enviasse os eventos de notificação de CRUD**. Além de questões de
desempenho, organização e até clareza, quem já precisou lidar com
alterações em massa, que tornam o envio de mensagens um grande desafio
verá como tudo fica muito mais simples quando o próprio banco de dados
trata dessa questão.

Mas, enfim...

Cada vez que salva-se uma nova CallRecord o sistema precisa verificar se
há um "par" solto por aí para poder, então, criar o ChargeEntry
correspondente. Ou seja: o caso médio de requisições ao banco fica em
torno de **3** quando, idealmente, deveria ser 1. Veja como é hoje:

* Salva o *start*;
* Verifica se existe o *end* correspondente;
* Se existe, verifica se já não há um *ChargeEntry*;
* Se não há, salva uma nova *ChargeEntry*.

**E isso é péssimo**. O ideal seria que simplesmente fosse salva a nova
entrada e tudo o mais fosse verificado por outro componente que lesse as
mensagens de uma **fila**.

Há várias formas de se implementar isso. Apresento aqui três, da melhor
para a pior:

* Postgres gera mensagens (NOTIFY) e um terceiro componente ouve (LISTEN)
  as mensagens e manda para o SNS, SQS ou o que for.
* Django chama uma função via **Celery** e um terceiro componente
  a executa e manda a mensagem para o SNS.
* Django envia direto para o SNS.

Do SNS ou SQS, outro componente, em outra máquina, não afetado pela
eventual sobrecarga de requisições do serviço atual, pode ir fazendo os
registros de cobranças em ritmo independente.


Além de melhorar o desempenho (e diminuir a exposição a bugs), passa-se
a tirar proveito das vantagens das [Arquiteturas Orientadas
e Eventos](https://slides.com/cleberz/eda-1#/).

## Uso

A forma como o problema foi enunciado não deixa clara a interface
necessária para que "as várias tecnologias de plataformas de
telecomunicações" usem o serviço, ou mesmo se eu sou livre para escolher
a melhor interface.

**Na dúvida, escolhi**.

### Dois modelos para as CallRecords

Não consegui saber se os exemplos dados no README para "Call Start Record"
e "Call End Record" (em formado JSON, supostamente) seriam exemplos de
*payloads* ou meramente do conceito geral da modelagem de dados. Por isso
tomei a liberdade de dividir a informação da maneira que acredito ser
a correta, que é usar **dois modelos**.

A abordagem de jogar tudo numa tabela só **é péssima**, já que manda
o serviço para o caminho dA Grande Pilha de Merda, na qual os componentes
de baixo (o banco de dados), ao invés de serem bem utilizados, são
preteridos por soluções nos componentes de cima (o Django): ao invés de eu
ter os campos `origin` e `destination` como **obrigatórios**, eu acabaria
tornando-os sempre opcionais e teria que verificar durante o *runtime* da
API se o `type` bate com o formato dos dados.

Diabos, quem é **especialista** em checar integridade de dados é o banco
de dados!


Ademais, me parece que um programa que já está preparado para enviar uma
informação com `type` para determinado endpoint não terá dificuldades em
fazer o envio de praticamente o mesmo *payload* para um endpoint diferente
baseando-se justamente no valor de `type`.

### call_id

Não ficou claro se `call_id` deve ser `unique` no banco. O sistema seria
usado por "várias plataformas diferentes", certo? Mas elas já tem um
entendimento quanto ao formato de `call_id`? E mais: elas tem como
comunicar-se entre si para evitar repetições?

Caso as plataformas consigam lidar entre si com a unicidade de `call_id`,
o ideal seria não criar os CallRecords com POST, como implementei, mas com
**PUT**, já que eu poderia usar a própria `call_id` como chave primária no
banco de dados.

Caso cada plataforma tenha seu próprio *range* de `call_id`, também seria
possível implementar, **com a devida autenticação** de cada uma, um
`unique_together = ("call_id", "platform_id")`.

## Segurança

### Autenticação e autorização

Qualquer um pode criar novos registros e, a não ser que estejamos dentro
de uma DMZ, isso é absurdamente errado por questões óbvias.

Além disso, é importante haver o registro de qual cliente criou cada
registro, já que isso facilita a identificação de erros eventualmente
causados por eles.

### CORS

Usei o `django-cors-headers` para permitir que qualquer um possa usar
a API, incluindo uma eventual interface rodando via Javascript.

## Testes

Usei a biblioteca `pytest` ao invés do sistema de testes do Django porque
considero-a superior e, especialmente, por maior familiaridade.

Foi configurado o Circle-CI para rodar os testes.

## Heroku

Publiquei no Heroku, mas você já conhece
o [Dokku](http://dokku.viewdocs.io/dokku/)? Ele é maravilhosamente simples
de usar, é compatível com os *buildpacks* do Heroku e ainda permite que se
trabalhe diretamente com containers do Docker.

Recomendo, especialmente quando a empresa estiver começando a pensar em
**diminuir custos**, já que a transição Heroku -> Dokku é muito suave
enquanto [o preço pode ficar muito mais
baixo](https://cleber.netlify.com/clebercaverna/#computa%C3%A7%C3%A3o/VPCs/).

(Sim, passa-se a "manter máquinas". Tudo tem um preço. Comento porque fiz
uma instalação e fiquei muito satisfeito.)

## Have fun...

Olha, eu já escrevi tanto endpoint de API nessa vida que parece que fazer
esse teste, para mim, [é meramente outra
quinta-feira](https://www.youtube.com/watch?v=iVzAMmpMra8).

*Fun, but not so much, really...*
