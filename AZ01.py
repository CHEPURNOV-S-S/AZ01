import pandas as pd

df = pd.read_csv("health_activity_data.csv")

print("Первый 5 строк:")
print(df.head(5))
print()

print("Информация о датасете:")
print(df.info())
print()

print("статистическое описание датасета:")
print(df.describe())
print()

print("читаем данные из нового датасета")
df = pd.read_csv("dz.csv")

print("Информация о датасете:")
print(df.info())
print()

print("удаляем строки с пропущенными значением City и Salary")
df.dropna(subset = ["City"], inplace=True, axis = "rows")
df.dropna(subset = ["Salary"], inplace=True, axis = "rows")

print("Информация о датасете:")
print(df.info())
print()

print("Средняя зарплата по городам")
print(df.groupby("City")["Salary"].mean())
print()