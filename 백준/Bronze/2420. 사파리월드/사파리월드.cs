using System;
using System.Linq;
using System.Collections.Generic;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            var input = Console.ReadLine().Split().Select(long.Parse).ToArray();
            Console.WriteLine(Math.Abs(input[0] - input[1]));
        }
    }
}
