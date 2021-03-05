import PySimpleGUI as sg

# Define uma janela de conteúdo

layout = [ [ sg.Text("Qual é o seu nome?")],
           [ sg.Input()],
           [ sg.Button('OK')] ]

# Cria uma nova janela

window = sg.Window('Título da janela', layout)

# Mostra e interage com a janela

event, values = window.read()

# Fazer alguma coisa com a informação obtida

print( "Olá", values[0], "! Obrigado por testar o PySimpleGUI")

# Finalizar

window.close()