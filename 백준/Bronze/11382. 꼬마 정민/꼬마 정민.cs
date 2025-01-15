using System;

class Program
{
    static void Main(string[] args)
    {
        var input = Console.ReadLine().Split();
        Console.WriteLine(long.Parse(input[0]) + long.Parse(input[1]) + long.Parse(input[2]));
    }
}
