def main():
  print("Conversor de Celsius para Fahrenheit!")

  celsius = float(input("Digite a temperatura em Celsius: "))
  fahrenheit = (celsius * 9/5) + 32
  print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f}°F")

if __name__ == "__main__":
  main()