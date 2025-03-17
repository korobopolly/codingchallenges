using System;
using System.Linq;
using System.Collections.Generic;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            var cmd1 = Console.ReadLine().Split().Select(int.Parse).ToArray();
            var cmd2 = Console.ReadLine().Split().Select(int.Parse).ToArray();
            int ax = cmd1[0];
            int ay = cmd1[1];
            int az = cmd1[2];
            int cx = cmd2[0];
            int cy = cmd2[1];
            int cz = cmd2[2];
            Console.WriteLine($"{cx - az} {cy / ay} {cz - ax}");
        }
    }
}
