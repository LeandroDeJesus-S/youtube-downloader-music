from pathlib import Path

save_path = Path.home() / 'Music'
P_MESSAGE = 'especifica que o link é uma playlist'
V_MESSAGE = 'especifica que o link é de um video'
T_MESSAGE = 'especifica o tipo como mp3 ou mp4. padrão: mp3'
O_MESSAGE = f'''passa o destino onde o arquivo sera salvo, por padrão ele salva
em: "{save_path}"'''
