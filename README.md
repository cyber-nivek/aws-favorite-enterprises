<!--
title: 'Deale's Favourite Enterprises'
description: 'En este documento se describe el funcionamiento de esta API'
layout: Doc
framework: v3
platform: AWS
language: Python
priority: 2
authorName: 'Kevin Ortega'
-->

# Deale's Favourite Enterprises

En este documento se describe el funcionamiento de esta API. Realizada mediante Serverless, con Python Flask, DinamoDB, AWS Lambda. Desarrollo en PyCharm.


## USO 

Para poder visualizar esta API, basta con introducir la siguiente URL en el navegador o a través de cualquier otro medio que lo pueda cargar:

`https://efblbcw0n9.execute-api.us-east-1.amazonaws.com`


Por otro lado, también es posible lanzarlo por terminal con el siguiente comando:
```bash
curl https://efblbcw0n9.execute-api.us-east-1.amazonaws.com
```

Una vez accedido, se muestra por pantalla... un mensaje de error. 
Desgraciadamente, la aplicación no funciona. PERO, su uso intencionado sería el de poder visualizar la tabla de favoritos desde el momento de acceso al link, y desde ahí, quizás desde un botón o un cuadro de texto, poder añadir entradas nuevas. 
No obstante, si bien la lógica para insertar un elemento está semi-implementada, no lo están así los medios user-friendly para hacerlo.

## Recursos

Enumero aquí las diversas plataformas online utilizadas, en mayor o menor medida.

- https://app.serverless.com/
- Amazaon AWS console (Lambda, DynamoDB, etc)
- https://console.serverless.com/
- 

## Recursos adicionales

Algunas de las webs que he consultado durante mi trabajo en este mini-proyecto. Propósito de documentación principalmente
- https://www.serverless.com/blog/flask-python-rest-api-serverless-lambda-dynamodb/
- https://www.serverless.com/framework/docs/tutorial
- https://dynobase.dev/dynamodb-serverless-framework/
- https://www.serverless.com/guides/dynamodb


- https://docs.aws.amazon.com/lambda/latest/dg/welcome.html
- https://docs.aws.amazon.com/lambda/latest/dg/python-handler.html
- https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html
- https://www.serverless.com/aws-lambda
- https://docs.aws.amazon.com/lambda/latest/dg/urls-tutorial.html
- https://www.serverless.com/blog/serverless-python-packaging/
- https://www.lewuathe.com/post-api-by-lambda-with-serverless-framework.html


- https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Scan.html
- https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html
- https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-test-and-debug.html
- https://www.serverless.com/framework/docs/providers/aws/guide/serverless.yml
- https://www.serverless.com/framework/docs/providers/aws/guide/resources/#configuration
- https://newrelic.com/blog/best-practices/create-a-serverless-function-in-python


- https://www.tutorialspoint.com/tkinter-button-commands-with-lambda-in-python
- https://medium.com/meliopayments/url-redirection-in-serverless-d1fc2fa99319
- https://flask.palletsprojects.com/en/2.3.x/quickstart/
- https://hackersandslackers.com/flask-routes/