using System;
using System.Linq;

class Program
{
    static void Main(string[] args)
    {
        int N = int.Parse(Console.ReadLine());
        for (int i = 0; i < N; i++) { 
            var input = Console.ReadLine().Split().Select(int.Parse).ToArray();
            Console.WriteLine(input.Sum());
        }
    }
}
