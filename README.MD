# Projeto de IoT integrado com Mecatrônica.

## Índice
- [Descrição](#descrição)
- [Projetos](#projetos)
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

- ### [Sensor de Combustível](https://github.com/RenanHS2RP/IoT_Flow_squad3.git)
    - *Descrição do Projeto:*
        - O projeto "Sensor de Combustível" tem como finalidade considerar o preço pago e a quantidade de combustível emitido pela bomba, comparando com o que foi realmente recebido e o preço correto de acordo com o posto.
        - O preço e a quantidade emitida pela bomba serão informados pelo cliente, também terão os dados conferidos pelo sensor, estes são enviados para uma API, que esta, calculará e enviará o valor correto para o aplicativo mobile.

## Pré-requisitos
Para executar nosso projeto, é recomendado:
- Acesso à um computador ou laptop
- Uma IDE como Visual Studio Code
- Conhecimento básico em terminais
- Conhecimento básico em envio de JSON
- Ter um celular com câmera e Expo Go instalado

## Instalação
- Copie este repositório com o comando: 

    `git clone --recurse-submodules https://github.com/RenanHS2RP/IoT_Window_squad3.git` 
    
    em uma pasta que desejar usando o terminal.

### Frontend
1. No terminal, navegue até o repositório com o comando:

    `cd /IoT_Window_squad3/codigo/front/window_mobile`.
    
2. Execute o comando: `npm i` para baixar todas as dependências do projeto

### Backend
- *Nota: O Backend está hospedado em: [sensorWindow.pythonanywhere.com](http://sensorwindow.pythonanywhere.com/api/), dezembro de 2023, não é efetivamente necessário rodar a API localmente para interagir com ela.*
1. No terminal, navegue até o repositório com o comando:

    `cd /IoT_Window_squad3/codigo/back/window_api`.
2. Execute o comando: `python manage.py makemigrations` para criar migrações.
3. Execute o comando: `python manage.py migrate` para migrar.

## Inicialização
### Frontend
- Para iniciar a interface, execute o comando `npx expo start`. Um código QR será gerado, e ao escaneá-lo com a câmera, a página da interface será aberta utilizando o Expo Go.

### Backend
- Execute o comando: `python manage.py runserver` para iniciar a API em: [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Uso
### Frontend
- Após aguardar o carregamento, a interface será mostrada, contendo a cidade, data, temperatura, umidade, estado da janela e uma previsão futura.

- Onde os componentes relacionados à telemetria, como temperatura, umidade e previsão futura, recebem dados telemetricos de uma fonte externa.

- A janela na aplicação possui dados coletados do sensor físico, informando se a janela está aberta ou fechada.
### Backend
- Tanto no host [local](http://127.0.0.1:8000/api/) ou [online](https://sensorwindow.pythonanywhere.com/api/), ao acessar a página será exibido três caminhos:

![Tela inicial/root API](/assets/img1.0.png)

- **Previsão** [[local]](http://127.0.0.1:8000/api/previsao/) [[online]](https://sensorwindow.pythonanywhere.com/api/previsao/): 
    - Nestas URLs serão exibidos métodos para listar (GET) e inserir (POST). Se desejar deletar (DELETE) ou atualizar (PUT), será necessário uma busca específica, basta adicionar o ID do JSON escolhido no final da URL, exemplo: 
    
        `https://sensorwindow.pythonanywhere.com/api/previsao/1` 
        
        ou 
        
        `http://127.0.0.1:8000/api/previsao/1`.
    - Para adicionar um JSON ao banco, pode-se ser adicionado pela interface gráfica. Na parte inferior, o campo "City name" indica o nome da cidade e uma vez fornecido o sistema ira entregar uma telemetria da previsão do tempo das próximas 72 horas.
    - Também há outros dois modos de envio, ambos por JSON. Na aba Raw data, pode ser enviado um JSON ou, caso já tenha um maior conhecimento sobre ferramentas auxiliares como Postman, pode ser feita esta inserção com JSON. Um exemplo de inserção através deste método:
```JSON
{
    "city_name": "Sorocaba"
}
```
![Tela lista da API de Previsão](/assets/img2.0.png)
![Tela input da API de Previsão](/assets/img2.1.png)
![Tela de edição da API de Previsão](/assets/img2.2.png)

- **Chuva** [[local]](http://127.0.0.1:8000/api/chuva/) [[online]](https://sensorwindow.pythonanywhere.com/api/chuva/): 
    - Nestas URLs serão exibidos métodos para listar (GET) e inserir (POST). Se desejar deletar (DELETE) ou atualizar (PUT), será necessário uma busca específica, basta adicionar o ID do JSON escolhido no final da URL, exemplo: 
    
        `https://sensorwindow.pythonanywhere.com/api/chuva/1` 
        
        ou 
        
        `http://127.0.0.1:8000/api/chuva/1`.
        
    - Para adicionar um JSON ao banco, pode-se ser adicionado pela interface gráfica. Na parte inferior, o campo: Is raining demontra se esta ocorrendo chuva e o sensor envia um sinal quando o estado é alterado.
    - Também há outros dois modos de envio, ambos por JSON. Na aba Raw data, pode ser enviado um JSON ou, caso já tenha um maior conhecimento sobre ferramentas auxiliares como Postman, pode ser feita esta inserção com JSON. Um exemplo de inserção através deste método:
```JSON
{
    "is_raining": true
}
```
![Tela lista da API de Chuva](/assets/img3.0.png)
![Tela input da API de Chuva](/assets/img3.1.png)
![Tela de edição da API de Chuva](/assets/img3.2.png)

- **Luminosidade** [[local]](http://127.0.0.1:8000/api/luminosidade/) [[online]](https://sensorwindow.pythonanywhere.com/api/luminosidade/): 
    - Nestas URLs serão exibidos métodos para listar (GET) e inserir (POST). Se desejar deletar (DELETE) ou atualizar (PUT), será necessário uma busca específica, basta adicionar o ID do JSON escolhido no final da URL, exemplo: 
    
        `https://sensorwindow.pythonanywhere.com/api/luminosidade/1` 
        
        ou 
        
        `http://127.0.0.1:8000/api/luminosidade/1`.

    - Para adicionar um JSON ao banco, pode-se ser adicionado pela interface gráfica. Na parte inferior, o campo: lux representa o quanto de lux o sensor captou e envia como mais um dos dados para determinar se esta ou não chovendo.
    - Também há outros dois modos de envio, ambos por JSON. Na aba Raw data, pode ser enviado um JSON ou, caso já tenha um maior conhecimento sobre ferramentas auxiliares como Postman, pode ser feita esta inserção com JSON. Um exemplo de inserção através deste método:
```JSON
{
    "lux": 1000
}
```
![Tela lista da API de Luminosidade](/assets/img4.0.png)
![Tela input da API de Luminosidade](/assets/img4.1.png)
![Tela de edição da API de Luminosidade](/assets/img4.2.png)