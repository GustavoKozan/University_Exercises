{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/GustavoKozan/University_Exercises/blob/main/Analisador_de_Notas.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "try:\n",
        "  qnotas = int(input(\"Digite a quantidade de notas para o cálculo da média e da situação acadêmica: \"))\n",
        "  notas = np.zeros(qnotas)\n",
        "\n",
        "  while qnotas <= 0:\n",
        "      print(\"Quantidade de notas inválida, apenas números maiores que 0\")\n",
        "      qnotas = int(input(\"Digite a quantidade de notas para o cálculo da média e da situação acadêmica: \"))\n",
        "\n",
        "  print(f\"Digite {qnotas} notas\")\n",
        "\n",
        "  for i in range(qnotas):\n",
        "    notas[i] = int(input(f\"Digite a {i+1}ª nota: \"))\n",
        "\n",
        "    while notas[i] < 0 or notas[i] > 100:\n",
        "      print(\"Nota inválida, apenas números positivos entre 0 e 100\")\n",
        "      notas[i] = int(input(f\"Digite a {i+1}ª nota: \"))\n",
        "\n",
        "  med = np.mean(notas)\n",
        "  maior = np.max(notas)\n",
        "  menor = np.min(notas)\n",
        "\n",
        "  print(f\"A média é = {med:.1f}\")\n",
        "  print(f\"A maior nota foi = {maior}\")\n",
        "  print(f\"A menor nota foi = {menor}\")\n",
        "\n",
        "  if med >= 70:\n",
        "    print(\"Resultado = Aprovado\")\n",
        "  elif 40 <= med < 70:\n",
        "    print(\"Resultado = Exame Final\")\n",
        "  else:\n",
        "    print(\"Resultado = Reprovado\")\n",
        "except ValueError:\n",
        "  print(\"Quantidade de notas inválida, apenas números inteiros podem ser admitidos\")"
      ],
      "metadata": {
        "id": "qYPGyE7RDjoN"
      },
      "execution_count": null,
      "outputs": []
    }
  ],
  "metadata": {
    "colab": {
      "name": "Conheça o Colab",
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}