using System;

class Program
{
    static void Main(string[] args)
    {
        var input = Console.ReadLine().Split();
        Console.WriteLine(int.Parse(input[0]) + int.Parse(input[1]));
        Console.WriteLine(int.Parse(input[0]) - int.Parse(input[1]));
        Console.WriteLine(int.Parse(input[0]) * int.Parse(input[1]));
        Console.WriteLine(int.Parse(input[0]) / int.Parse(input[1]));
        Console.WriteLine(int.Parse(input[0]) % int.Parse(input[1]));
    }
}
