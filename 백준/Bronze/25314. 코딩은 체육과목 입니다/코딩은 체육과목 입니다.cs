using System;

class Program
{
    static void Main(string[] args)
    {
        int N = int.Parse(Console.ReadLine()) / 4;
        for (int i = 0; i < N; i++) {
            Console.Write("long ");
        }
        Console.WriteLine("int");
    }
}
