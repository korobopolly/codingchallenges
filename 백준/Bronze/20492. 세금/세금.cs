using System;
using System.Linq;
using System.Numerics;
using System.Collections.Generic;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            int N = int.Parse(Console.ReadLine());
            Console.WriteLine($"{N * 0.78} {N * 0.8 + N * 0.2 * 0.78}");
        }
    }
}
