using System;
using System.Collections.Generic;
using System.Linq;
using System.Numerics;
using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;
using System.Text;

class Program2
{
    static void Main(string[] args)
    {
        StringBuilder sb = new StringBuilder();
        while (true)
        {
            var input = Console.ReadLine().Split().Select(int.Parse).ToArray();
            if (input[0] == 0 && input[1] == 0)
            {
                break;
            }
            sb.AppendLine(input[0] > input[1] ? "Yes" : "No");
        }
        Console.WriteLine(sb.ToString());   
    }
}