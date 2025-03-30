using System;

class Program
{
    static void Main(string[] args)
    {
        int N = int.Parse(Console.ReadLine());
        Console.WriteLine(SquareCount(N));
    }

    static int SquareCount(int n)
    {
        return (int)Math.Floor(Math.Sqrt(n));
    }
}
