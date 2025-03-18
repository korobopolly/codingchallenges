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
            var cmd = Console.ReadLine().Split().Select(BigInteger.Parse).ToArray();
            BigInteger x = cmd[0];
            BigInteger y = cmd[1];
            Console.WriteLine($"{x / y}\n{x % y}");
        }
    }
}
