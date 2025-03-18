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
            var cmd = Console.ReadLine().Split().Select(int.Parse).ToArray();
            int K = cmd[0];
            int N = cmd[1];
            int M = cmd[2];
            Console.WriteLine($"{(M - K * N > 0 ? 0 : Math.Abs(M - K * N))}");
        }
    }
}
