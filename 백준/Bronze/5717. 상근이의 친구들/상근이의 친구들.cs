using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

class Program
{
    static void Main(string[] args)
    {
        while (true) {
            var input = Console.ReadLine().Split().Select(int.Parse).ToArray();
            if (input[0] == 0 && input[1] == 0)
                break;
            Console.WriteLine(input[0] + input[1]);
        }
    }
}