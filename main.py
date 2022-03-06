#%%
import pandas as pd
#%%
sldb = pd.read_csv('synergy_logistics_database.csv')
#%%
#hacer un dataframe de la base de datos synergy logistics
valores_transporte = sldb.groupby(['origin','destination']).count()
#%%
#Problema 1 Partes 1/2
exports = sldb[sldb['direction'] == 'Exports']
rutas = exports.groupby(['origin','destination','transport_mode'])
top_rutas = rutas.count()['total_value'].sort_values(ascending=False).head(10)
top_rutas = top_rutas.reset_index()
top_rutas
# %%
#Problema 1 Parte 2/2
exports = sldb[sldb['direction'] == 'Exports']
rutas = exports.groupby(['origin','destination','transport_mode'])
value_rutas = rutas.sum()['total_value'].sort_values(ascending=False).head(10)
value_rutas = value_rutas.reset_index()
value_rutas
# %%
#Problema 2 Parte 1/2
values_transport = sldb['transport_mode'].unique()
# %%
#Problema 2 Parte 2/2
problema_2 = sldb.groupby('transport_mode').sum()['total_value'].sort_values(ascending=False)
problema_2 = problema_2.reset_index()
total = problema_2['total_value'].sum()
problema_2['porcentaje'] = (problema_2['total_value'] / total) * 100
problema_2['porcentaje_acum'] = problema_2.cumsum()['porcentaje']
problema_2
# %%
#Problema 3
paises = sldb.groupby(['origin']).sum()['total_value'].sort_values(ascending=False)
paises = paises.reset_index()
total_paises_value = paises['total_value'].sum()
paises['porcentaje_paises'] = (paises['total_value'] / total_paises_value) * 100
paises['porcentaje_paises_acum'] = paises.cumsum()['porcentaje_paises']
paises_80 = paises[paises['porcentaje_paises_acum'] < 82 ]
paises_80
# %%
#Problema 3
paises1 = sldb.groupby(['origin','destination','transport_mode']).sum()['total_value'].sort_values(ascending=False)
paises1 = paises1.reset_index()
total_paises1_value = paises1['total_value'].sum()
paises1['porcentaje_paises'] = (paises1['total_value'] / total_paises1_value) * 100
paises1['porcentaje_paises_acum'] = paises1.cumsum()['porcentaje_paises']
paises_20 = paises1[paises1['porcentaje_paises_acum'] < 20 ]
paises_20