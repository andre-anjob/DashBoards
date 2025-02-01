import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

st.title('Analise do Titanic Dataset')


carregamento = pd.read_csv('tested.csv', encoding='ISO-8859-1', sep=',')
titanic = pd.DataFrame(carregamento)


st.sidebar.header('Analise de Dados')
sexo = st.sidebar.selectbox('Selecione o Sexo', ['Todos', 'male', 'female'])
classe = st.sidebar.selectbox('Selecione a Classe', ['Todas', 'First', 'Second', 'Third'])

if sexo != 'Todos':
    titanic = titanic[titanic['Sex'] == sexo]
if classe != 'Todas':
    titanic = titanic[titanic['Pclass'] == classe]

st.write(f'Monstrando {sexo} e {classe}')
st.write(titanic)

st.header('Visualizações')

st.subheader('Distribuição de Idade')   
fig, ax = plt.subplots()
titanic['Age'].hist(bins=20, ax=ax, color='blue', edgecolor='black')
ax.set_xlabel('Idade')
ax.set_ylabel('Frequencia')
st.pyplot(fig)


st.subheader('Contagem de Sobreviventes')
sobreviventes = titanic['Survived'].value_counts()
st.bar_chart(sobreviventes)

st.subheader('taxa de Sobreviventes por Sexo')
taxa_sobrevivencia = titanic.groupby('Pclass')['Survived'].mean()
st.bar_chart(taxa_sobrevivencia)

st.subheader('Gráfico de Dispersão: Idade vs Tarifa')
fig, ax = plt.subplots()
ax.scatter(titanic['Age'], titanic['Fare'], alpha=0.5)
ax.set_xlabel('Idade')
ax.set_ylabel('Tarifa')
st.pyplot(fig)
