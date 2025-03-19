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
            int N = cmd[4];
            Console.WriteLine($"{(4 * N - (cmd.Sum() - N) < 0 ? 0 : (4 * N - (cmd.Sum() - N)))}");
        }
    }
}
