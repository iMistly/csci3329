import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("titanic.csv", sep=',')

#Top of DataFrame
print(df.head())

#Columns of DataFrame
print(df.columns)

#DataFrame summary
print(df.info())

#Filter df
print(df['Sex'] == 'male')

#Make new df from other df
m_data = df[df['Sex'] == 'male']
print(m_data.info())
print(m_data.head())

f_data = df[df['Sex'] == 'female']
print(f_data.head())

#Sum of all male survivors
totalM = m_data['Survived'].sum()
totalF = f_data['Survived'].sum()

print(f"Total males survived: {totalM/len(m_data)*100:.2f} %")
print(f"Total females survived: {totalF/len(f_data)*100:.2f} %")

print(f"Male average fare: ${m_data['Fare'].mean():.2f}")
print(f"Female average fare: ${f_data['Fare'].mean():.2f}")

print(f"Lowest fare: ${df.Fare.min():.2f}")
print(f"Highest fare: ${df.Fare.max():.2f}")

print(df.sort_values('Fare', ascending=False))

plt.scatter(df.index, df.Fare.sort_values())
plt.show()