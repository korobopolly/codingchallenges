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
        int A = int.Parse(Console.ReadLine());
        Console.WriteLine(A % 5 == 0 ? A / 5 : A / 5 + 1);
    }
}