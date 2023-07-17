from flask import Flask, render_template #"Pacote que permite" colocar o site no ar. pacote template para interligar o html com python e retornar
app = Flask(__name__) #app é uma instância da classe flask. Permite o flask entender que este arquivo é um site e também vai ser a base para interligar vários arquivos diferentes


@app.route("/") #Chamando o metodo route da classe flask. Define a rota (url) do site e abaixo o que aparecerá nessa página
def home():
    return render_template("home.html") #retornar o que foi feito dentro do arquivo home em html

@app.route("/contato") #Atribuindo uma funcionalidade nova no que está abaixo
def contato():
    return render_template("contato.html")

#if __name__ == "__name__":
#"nome do site".run() coloca o site no ar
app.run(debug=True) #Modo debug ativado para que toda implemntação feita no código suba automaticamente no site sem precisar interromper e ativar o executavel
