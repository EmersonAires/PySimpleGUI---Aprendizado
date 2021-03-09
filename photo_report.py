import PySimpleGUI as sg
import os                       # Interface de sistema operacional
from PIL import Image, ImageTk  # Biblioteca para manipulação de imagens
import io                       # fornece os principais recursos do Python para lidar com
                                # vários tipos  de E / S.

# Obtem a pasta contendo as imagens do usuário
folder = sg.popup_get_folder('Pasta de imagens para abrir', default_path='')

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
