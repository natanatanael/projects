import requests


bases = requests.get("http://127.0.0.1:8000/bases/")
bases = bases.json()
   

agendamentos = requests.get("http://127.0.0.1:8000/agendamentos/")
agendamentos = agendamentos.json()

    
