## Relatório: Programa para Cálculo do IMC na Google Cloud Shell Editor

#Introdução

O Índice de Massa Corporal (IMC) é uma medida amplamente utilizada para avaliar a saúde de uma pessoa com base na relação entre seu peso e altura. Este relatório descreve a criação de um programa para calcular o IMC usando a linguagem de programação Python na Google Cloud Shell Editor. Além disso, será abordada a utilização da ferramenta Google Cloud Shell Editor e linguagem Python para a criação deste programa.

#Métodos

Utilização da Google Cloud Shell Editor
A Google Cloud Shell Editor é uma ferramenta de desenvolvimento baseada na web que permite escrever, editar e executar código diretamente no navegador. Ela é especialmente útil para projetos de desenvolvimento na nuvem e oferece um ambiente de programação interativo.
Para acessar a Google Cloud Shell Editor, é necessário ter uma conta no Google Cloud Platform (GCP). Após o login, o usuário pode abrir a Cloud Shell Editor a partir do ícone correspondente no canto superior direito da interface do GCP.

#Desenvolvimento em Python

Para criar o programa de cálculo do IMC, utilizei a linguagem de programação Python. A seguir, descrevo os principais passos do desenvolvimento:
Entrada de Dados: O programa solicita ao usuário que insira seu peso em quilogramas (kg) e sua altura em centímetros (cm).
Cálculo do IMC: Com base nos dados fornecidos, o programa calcula o IMC utilizando a fórmula:

IMC = peso (kg) / (altura (m) ^ 2)
Onde a altura é convertida de centímetros para metros.

Interpretação do IMC: O programa avalia o resultado do cálculo do IMC e fornece uma interpretação do estado de saúde da pessoa com base em faixas de IMC:
Abaixo do Peso (IMC < 18.5)
Peso Normal (18.5 <= IMC < 24.9)
Sobrepeso (25 <= IMC < 29.9)
Obeso (IMC >= 30)
Exibição dos Resultados: O programa exibe o valor do IMC calculado e a interpretação correspondente.

#Resultados

Após a criação e execução do programa na Google Cloud Shell Editor, os resultados foram os seguintes:
O programa solicita as informações de peso e altura do usuário.
Com base nessas informações, o programa calcula o IMC.
O IMC calculado é então interpretado e uma mensagem é exibida informando o estado de saúde da pessoa.
Este programa demonstra uma aplicação prática da linguagem Python para calcular e interpretar o IMC, auxiliando na avaliação da saúde de um indivíduo.

#Conclusão

A criação do programa para calcular o IMC na Google Cloud Shell Editor usando Python foi um exemplo prático de como a programação pode ser aplicada para resolver problemas do mundo real. A Cloud Shell Editor proporcionou um ambiente de desenvolvimento conveniente na web, eliminando a necessidade de configurações complexas.
Além disso, o programa ilustra como o Python pode ser usado para realizar cálculos matemáticos e fornecer informações valiosas, como a interpretação do IMC. Essa combinação de ferramentas e linguagem de programação é valiosa tanto para iniciantes quanto para programadores experientes em busca de soluções práticas para problemas de saúde e bem-estar.
