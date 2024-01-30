# IMPORTAR LIBRERIAS NECESARIAS
import requests
import pandas as pd
import matplotlib.pyplot as plt

# OBTENER DATOS DE CELEBRIDADES: 'Lionel Messi', 'Selena Gomez', 'Cristiano Ronaldo', 'Taylor Lautner', 'Manu Ginobili'
api_key = 'API-KEY'
celebrities_names = ['Lionel Messi', 'Selena Gomez', 'Cristiano Ronaldo', 'Taylor Lautner', 'Manu Ginobili']

celebrities_data = []

for name in celebrities_names:
    api_url = f'https://api.api-ninjas.com/v1/celebrity?name={name}'
    response = requests.get(api_url, headers={'X-Api-Key': api_key})

    if response.status_code == requests.codes.ok:
        data = response.json()
        if data:
            celebrities_data.append(data[0])
    else:
        print(f"Error al acceder a la API para {name}. Código de estado: {response.status_code}")

# CREAR UN DATAFRAME Y GUARDAR EN UN CSV LOS DATOS: 'name', 'gender', 'occupation', 'birthday', 'age'
df = pd.DataFrame(celebrities_data)
selected_columns = ['name', 'gender', 'occupation', 'birthday', 'age']
df_selected = df[selected_columns]

print(df_selected)

csv_filename = 'celebrities_info.csv'
df_selected.to_csv(csv_filename, index=False)

# GRAFICAR LA EDAD DE LAS CELEBRIDADES
plt.figure() 
plt.bar(df_selected['name'], df_selected['age'])
plt.title('EDAD DE CELEBRIDADES')
plt.xlabel('NOMBRE DEL FAMOSO')
plt.ylabel('EDAD')
plt.xticks(rotation=25, ha='right')
plt.show()
