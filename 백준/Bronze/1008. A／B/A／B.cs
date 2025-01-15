using System;

class Program
{
    static void Main(string[] args)
    {
        var input = Console.ReadLine().Split();
        Console.WriteLine($"{double.Parse(input[0]) / double.Parse(input[1]):F9}");
    }
}
