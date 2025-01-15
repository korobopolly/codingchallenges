using System;

class Program
{
    static void Main(string[] args)
    {
        string[] strings = Console.ReadLine().Split(" ");
        int[] ints = Array.ConvertAll(strings, s => int.Parse(s));
        Console.WriteLine(ints[0] - ints[1]);
    }
}
