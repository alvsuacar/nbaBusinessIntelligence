import time
import random
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
import requests

import pandas as pd

from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog

# 1. Creamos una sesión con reintentos y mayor timeout
def create_session_with_retries(
    total_retries=5, 
    backoff_factor=1, 
    status_forcelist=(429, 500, 502, 503, 504),
    timeout=60
):
    session = requests.Session()
    retries = Retry(
        total=total_retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist
    )
    adapter = HTTPAdapter(max_retries=retries)
    session.mount('https://', adapter)
    return session

session = create_session_with_retries()

# 2. Función para obtener los datos de un jugador en una temporada
def get_player_season_gamelog(player_id, season):
    """
    Descarga el registro de partidos (gamelog) de un jugador en una temporada dada.
    Devuelve un DataFrame con las columnas por defecto de la nba_api, más 'SEASON'.
    """
    try:
        gamelog = playergamelog.PlayerGameLog(
            player_id=player_id,
            season=season,
            season_type_all_star='Regular Season',
            timeout=30,
        )
        df = gamelog.get_data_frames()[0]
        df['SEASON'] = season
        df['PLAYER_ID'] = player_id
        return df
    except Exception as e:
        print(f"Error con player_id={player_id}, season={season}: {e}")
        return pd.DataFrame()

# 3. Obtenemos la lista de jugadores activos
active_players = players.get_active_players()
print(f"Jugadores activos obtenidos: {len(active_players)}")

# 4. Dividimos la lista de jugadores en chunks de 50
CHUNK_SIZE = 15
def chunk_list(lst, chunk_size):
    for i in range(0, len(lst), chunk_size):
        yield lst[i:i + chunk_size]

player_chunks = list(chunk_list(active_players, CHUNK_SIZE))

# 5. Recolectamos datos para 2023-24
all_data_2324 = []
print("=== Comenzando descargas para la temporada 2023-24 ===")

for idx, chunk in enumerate(player_chunks):
    print(f"Procesando chunk {idx+1} de {len(player_chunks)} (2023-24)...")
    # Para cada jugador del chunk, descargamos sus datos
    for p in chunk:
        df_log = get_player_season_gamelog(p['id'], '2023-24')
        if not df_log.empty:
            # Añadimos nombre de jugador para referencia
            df_log['PLAYER_NAME'] = p['full_name']
            all_data_2324.append(df_log)
    # Esperamos 2 minutos antes de seguir con el siguiente chunk
    print("Pausa de 2 minutos para evitar sobrecarga...")
    time.sleep(180)

df_2324 = pd.concat(all_data_2324, ignore_index=True) if all_data_2324 else pd.DataFrame()
print(f"Datos 2023-24 recopilados. Filas totales: {len(df_2324)}")

#Guardamos el resultado en CSV
output_file = "nba_players_gamelog_2023-24.csv"
df_2324.to_csv(output_file, index=False)
print(f"Archivo CSV generado: {output_file}")
