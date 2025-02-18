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
        var input = Console.ReadLine().Split().Select(int.Parse).ToArray();
        int A = input[0];
        int B = input[1];
        int C = input[2];
        Console.WriteLine(B / A * 3 * C);
    }
}