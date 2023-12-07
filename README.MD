# Projeto de IoT integrado com Mecatrônica.

## Índice
- [Descrição](#descrição)
- [Projetos](#projetos)
- [Capturas de Tela](#capturas-de-tela)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Inicialização](#inicialização)
- [Uso](#uso)

## Descrição
Este é um projeto realizado pela turma de ADS da Escola e Faculdade Técnica SENAI Gaspar Ricardo Jr. com o objetivo de criar uma integração com dois projetos da turma de Mecatrônica. Isso resultou na criação de uma interface, uma API e uma integração específica para cada projeto.

## Projetos:
- ### [Janela Automática](https://github.com/RenanHS2RP/IoT_Window_squad3)
    - *Descrição do Projeto:*
        - O projeto "Janela Automática" tem como objetivo automatizar uma janela, tomando ações com base nas condições climáticas. Se a previsão indicar alta probabilidade de chuva e ela realmente ocorrer, a janela será fechada; caso contrário, ela será aberta.
        - Para isso, sensores de umidade e dados de previsão do tempo de uma API externa serão utilizados. Um painel no ThingsBoard exibirá gráficos relacionados à probabilidade de chuva, histórico de aberturas e fechamentos, além de alertas sobre o estado da janela.

- ### [Sensor de Combustível](https://github.com/seu-usuario/sua-repo)
    - *Descrição do Projeto:*
        - O projeto "Sensor de Combustível" tem como finalidade considerar o preço pago e a quantidade de combustível emitido pela bomba, comparando com o que foi realmente recebido e o preço correto de acordo com o posto.
        - O preço e a quantidade emitida pela bomba serão informados pelo cliente, mas o sensor enviará a quantidade correta de combustível. A API calculará e enviará o valor correto para o aplicativo mobile.

## Capturas de Tela
![Texto Alternativo](/caminho/para/a/imagem)

## Pré-requisitos
Para executar nosso projeto, é recomendado:
- Acesso à um computador ou laptop
- Uma IDE como Visual Studio Code
- Conhecimento básico em terminais
- Conhecimento básico em envio de JSON (back)
- Acesso ao ThingsBoard Community ou ThingsBoard Cloud (recomendado para aplicações de curto prazo)

## Instalação
- Copie este repositório com o comando `git clone --recurse-submodules https://github.com/RenanHS2RP/IoT_Window_squad3.git` em uma pasta que desejar usando o terminal.

- ### Frontend
    - [Instruções de instalação para o Frontend]

- ### Backend
- *Nota: O Backend está hospedado em: [sensorWindow.pythonanywhere.com](http://sensorwindow.pythonanywhere.com/api/), dezembro de 2023, não é efetivamente necessário rodar a API localmente para interagir com ela.*
1. No terminal, navegue até o repositório com o comando `cd /IoT_Flow_squad3/codigo/back/FlowAPIProject`.
2. Execute o comando `python manage.py makemigrations` para criar migrações.
3. Execute o comando `python manage.py migrate` para migrar.

## Inicialização
- ### Frontend
    - [Instruções de inicialização para o Frontend]
### Backend
- Execute o comando `python manage.py runserver` para iniciar a API em: [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Uso
### Frontend
- Em manutenção.
### Backend
- Tanto no host [local](http://127.0.0.1:8000/api/) ou [online](https://sensorwindow.pythonanywhere.com/api/), ao acessar a página será exibido três caminhos:
- **Previsão** [[local]](http://127.0.0.1:8000/api/previsao/) [[online]](https://sensorwindow.pythonanywhere.com/api/previsao/): 
    - Nestas URLs serão exibidos métodos para listar (GET) e inserir (POST). Se desejar deletar (DELETE) ou atualizar (PUT), será necessário uma busca específica, basta adicionar o ID do JSON escolhido no final da URL, exemplo: `https://sensorwindow.pythonanywhere.com/api/previsao/1` ou `http://127.0.0.1:8000/api/previsao/1`.
    - Para adicionar um JSON ao banco, pode-se ser adicionado pela interface gráfica. Na parte inferior, o campo "City name" indica o nome da cidade e uma vez fornecido o sistema ira entregar uma telemetria da previsão do tempo das próximas 72 horas.
    - Também há outros dois modos de envio, ambos por JSON. Na aba Raw data, pode ser enviado um JSON ou, caso já tenha um maior conhecimento sobre ferramentas auxiliares como Postman, pode ser feita esta inserção com JSON. Um exemplo de inserção através deste método:
```JSON
{
    "city_name": "Sorocaba"
}
```
- **Chuva** [[local]](http://127.0.0.1:8000/api/chuva/) [[online]](https://sensorwindow.pythonanywhere.com/api/chuva/): 
    - Nestas URLs serão exibidos métodos para listar (GET) e inserir (POST). Se desejar deletar (DELETE) ou atualizar (PUT), será necessário uma busca específica, basta adicionar o ID do JSON escolhido no final da URL, exemplo: `https://sensorwindow.pythonanywhere.com/api/chuva/1` ou `http://127.0.0.1:8000/api/chuva/1`.
    - Para adicionar um JSON ao banco, pode-se ser adicionado pela interface gráfica. Na parte inferior, o campo: Is raining demontra se esta ocorrendo chuva e o sensor envia um sinal quando o estado é alterado.
    - Também há outros dois modos de envio, ambos por JSON. Na aba Raw data, pode ser enviado um JSON ou, caso já tenha um maior conhecimento sobre ferramentas auxiliares como Postman, pode ser feita esta inserção com JSON. Um exemplo de inserção através deste método:
```JSON
{
    "is_raining": true
}
```
- **Luminosidade** [[local]](http://127.0.0.1:8000/api/luminosidade/) [[online]](https://sensorwindow.pythonanywhere.com/api/luminosidade/): 
    - Nestas URLs serão exibidos métodos para listar (GET) e inserir (POST). Se desejar deletar (DELETE) ou atualizar (PUT), será necessário uma busca específica, basta adicionar o ID do JSON escolhido no final da URL, exemplo: `https://sensorwindow.pythonanywhere.com/api/luminosidade/1` ou `http://127.0.0.1:8000/api/luminosidade/1`.
    - Para adicionar um JSON ao banco, pode-se ser adicionado pela interface gráfica. Na parte inferior, o campo: lux representa o quanto de lux o sensor captou e envia como mais um dos dados para determinar se esta ou não chovendo.
    - Também há outros dois modos de envio, ambos por JSON. Na aba Raw data, pode ser enviado um JSON ou, caso já tenha um maior conhecimento sobre ferramentas auxiliares como Postman, pode ser feita esta inserção com JSON. Um exemplo de inserção através deste método:
```JSON
{
    "lux": 1000
}
```