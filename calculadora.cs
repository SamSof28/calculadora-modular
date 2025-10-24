using System;

class Calculadora
{
    static void Main(string[] args)
    {
        double a, b, n;
        string operacion;

        do
        {
            Console.WriteLine("Ingrese el primer número:");
            a = Convert.ToInt(Console.ReadLine());

            Console.WriteLine("Ingrese el segundo número:");
            b = Convert.ToDouble(Console.ReadLine());

            Console.WriteLine("Ingrese la operación (+, -, *, /) o 'exit' para salir:");
            operacion = Console.ReadLine();

            switch (operacion)
            {
                case "+":
                    Console.WriteLine("Resultado: " + Sumar(num1, num2));
                    break;
                case "-":
                    Console.WriteLine("Resultado: " + Restar(num1, num2));
                    break;
                case "*":
                    Console.WriteLine("Resultado: " + Multiplicar(num1, num2));
                    break;
                case "/":
                    try
                    {
                        Console.WriteLine("Resultado: " + Dividir(num1, num2));
                    }
                    catch (DivideByZeroException)
                    {
                        Console.WriteLine("Error: División por cero.");
                    }
                    break;
                case "exit":
                    Console.WriteLine("Saliendo...");
                    break;
                default:
                    Console.WriteLine("Operación no válida.");
                    break;
            }
        } while (operacion != "exit");
    }

    static double Sumar(double a, double b) { return a + b; }
    static double Restar(double a, double b) { return a - b; }
    static double Multiplicar(double a, double b) { return a * b; }
    static double Dividir(double a, double b) { return b != 0 ? a / b : throw new DivideByZeroException(); }
}