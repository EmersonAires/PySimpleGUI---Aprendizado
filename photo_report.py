import PySimpleGUI as sg
import os                       # Interface de sistema operacional
from PIL import Image, ImageTk  # Biblioteca para manipulação de imagens
import io                       # fornece os principais recursos do Python para lidar com
                                # vários tipos  de E / S.

# Obtem a pasta contendo as imagens do usuário
path_padrao = 'C://Users//emerson eduardo//Pictures//Recortes'
folder = sg.popup_get_folder('Pasta de imagens para abrir', default_path=path_padrao)

if not folder: # Se não for selecionado nenhuma pasta --> cancelar
    sg.popup_cancel('Cancelando')
    raise SystemExit()

# Tipos de imagens suportados pelo pacote PIL
img_types = ('.png', '.jpg', '.jpeg', '.tiff', '.bmp')

# Obtém uma lista de arquivos da pasta (folder)
flist0 = os.listdir(folder)

# cria uma sublista de arquivos de imagens (não subpasta, nenhum tipo de arquivo errado)
# verfica se o caminho passado corresponde a um arquivo e 
# se o formato do arquivo correponde aos suportados pelo PIL
fnames = [f for f in flist0 if os.path.isfile(
    os.path.join(folder, f)) and f.lower().endswith(img_types)]

num_files = len(fnames)    # número de imagens encontradas
if num_files == 0:         # se nenhum arquivo for encontrado --> exit
    sg.popup('Nenhum arquivo na pasta')
    raise SystemExit

del flist0                  # não mais preciso

# --------------------------------------------------------------------------------------------
# Usar PIL para ler dados de uma imagem
# --------------------------------------------------------------------------------------------

def get_img_data(f, maxsize=(1200, 850), first=False):
    """ Gera dados de imagem usando PIL
    """
    img = Image.open(f)         # abre uma imagem  com caminho (f)
    img.thumbnail(maxsize)      # miniatura 1200x850 pixels
    if first:
        bio = io.BytesIO()      # Um fluxo binário usando um buffer (região de 
                                # memória física utilizada para armazenar temporariamente os # dados enquanto eles estão sendo movidos de um lugar para   outro) de bytes na memória

        img.save(bio, format='PNG') # salva a imagem temporariamente na memória
        del img                     # deleta a variável contendo a imagem

        return bio.getvalue()       # retorna a imagem armazenada no buffer
    return ImageTk.PhotoImage(img)
# --------------------------------------------------------------------------------------------


# Faça esses 2 elementos fora do layout, pois queremos "atualizá-los" mais tarde
# Inicializar com o primeiro arquivo da lista
filename = os.path.join(folder, fnames[0])               # nome do primeiro elemento da lista
image_elem = sg.Image(data=get_img_data(filename, first=True)) # atribui a primeira imagem à variável
filename_display_elem = sg.Text(filename, size=(80, 3)) # atribui o nome da primeira imagem à variável
file_num_display_elem = sg.Text('File 1 of {}'.format(num_files), size=(15,1)) # atribui o texto contendo a quantidade de arquivos à variável

# Define layout, exibe e lê o formulário
col = [[filename_display_elem],  # Coluna com duas linhas: 1ª Nome da foto, 
       [image_elem]]             # 2ª imagem

col_files = [[sg.Listbox(values=fnames, change_submits=True, size=(60, 30), key='listbox')], 
             [sg.Button('Next', size=(8, 2)), sg.Button('Prev', size=(8, 2)),
             file_num_display_elem]]

layout = [[sg.Column(col_files), sg.Column(col)]]   # Layout --> duas colunas

window = sg.Window('Image Browser', layout, return_keyboard_events=True, location=(0, 0), size=(1200, 700), use_default_focus=False)

event, values = window.read()