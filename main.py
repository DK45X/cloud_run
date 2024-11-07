import pandas as pd
from great_expectations import DataContext

def aplicar_reglas_calidad(datos):
  """
  Aplica las reglas de calidad de datos a un DataFrame de Pandas.

  Args:
    datos: Un DataFrame de Pandas que contiene los datos a validar.

  Returns:
    Un diccionario con los resultados de la validación.
  """
  context = DataContext()
  suite = context.get_expectation_suite("mi_suite_de_expectativas") # Reemplaza con el nombre de tu suite
  resultados = suite.run_validation_operator(
      "action_list_operator", assets_to_validate=[datos]
  )
  return resultados.to_json_dict()

if __name__ == "__main__":
  # Ejemplo de datos (reemplázalo con tu fuente de datos)
  datos = pd.DataFrame({
      'nombre': ['Juan', 'Ana', 'Pedro'],
      'edad': [30, 25, 40]
  })

  # Aplicar las reglas de calidad de datos.
  resultados = aplicar_reglas_calidad(datos)

  # Imprimir los resultados.
  print(resultados)