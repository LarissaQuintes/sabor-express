# 🍽️ Sabor Express

Sistema de linha de comando em Python pra cadastrar, listar e ativar/desativar restaurantes. Fiz esse projeto estudando lógica de programação com Python.

## ✅ Funcionalidades

- Cadastrar um restaurante novo, com nome e categoria
- Listar os restaurantes cadastrados
- Ativar ou desativar um restaurante que já existe na lista
- Se você digitar uma opção que não existe no menu, o programa avisa em vez de travar

## 🛠️ Tecnologias

- Python
- Módulo `os`, só pra limpar o terminal

## ▶️ Como rodar

1. Clone o repositório:

```
git clone <https://github.com/LarissaQuintes/sabor-express>
```

1. Entre na pasta e roda:

```
python app.py
```

Obs: o `os.system("cls")` limpa a tela só no Windows. Se rodar em Mac ou Linux não dá erro, só não limpa o terminal entre uma tela e outra.

## 💡 O que eu aprendi

Enquanto fazia esse projeto errei uma coisa boba que acabou virando aprendizado. Escrevi `restaurante_encontrado == True` dentro de um `if`, achando que estava atualizando a variável. Só que `==` é comparação, não atribuição, então a variável nunca mudava de valor de verdade e o aviso de restaurante não encontrado ficava sempre errado. Levei um tempo pra perceber, porque o código rodava sem erro nenhum, só dava resultado errado.

Outra coisa que aprendi testando: onde um `if` fica dentro de um `for` muda o resultado. Eu tinha colocado um `if` um nível a mais de indentação do que devia, e ele ficou dentro do laço em vez de rodar só depois que o laço terminasse. Deu pra ver na prática que em Python indentação não é só estética, é parte da lógica mesmo.

## 🚀 Próximos passos

- Salvar os dados em arquivo, hoje eles somem quando fecha o programa
- Colocar opção de remover restaurante
- Quem sabe transformar isso numa API depois

## 👩‍💻 Autora

Larissa Quintes, estudante de Engenharia da Computação