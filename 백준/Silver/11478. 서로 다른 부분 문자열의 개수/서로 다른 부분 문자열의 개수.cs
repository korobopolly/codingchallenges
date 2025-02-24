using System;
using System.Collections.Generic;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            string input = Console.ReadLine();
            var parts = new HashSet<string>();
            for(int j = 1; j <= input.Length; j++)
            {
                for (int i = 0; i < input.Length; i++)
                {
                    if(i + j <= input.Length) parts.Add(input.Substring(i, j));
                }
            }
            Console.WriteLine(parts.Count);
        }
    }
}
