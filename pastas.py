import os

# Lista com os nomes das pastas desejadas
pastas = [
    'SIM_DOFET_2018_ate_2020',
    'SIM_DOFET_CONCATENADA',
    'SINASC_2018_ate_2020',
    'SINASC_2018_ate_2020_estados',
    'SINASC_2018_ate_2020_estados_processado',
    'SINASC_concatenada_final'
]

# Diretório onde as pastas serão criadas
diretorio_base = ''  # Substitua pelo caminho real desejado

# Cria as pastas
for pasta in pastas:
    caminho_pasta = os.path.join(diretorio_base, pasta)
    os.makedirs(caminho_pasta, exist_ok=True)
    print(f'Criada a pasta: {caminho_pasta}')