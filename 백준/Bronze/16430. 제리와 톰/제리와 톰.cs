using System;
using System.Collections.Generic;
using System.Linq;
using System.Numerics;
using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;
using System.Security.Claims;
using System.Text;

class Program2
{
    static void Main(string[] args)
    {
        var input1 = Console.ReadLine().Split().Select(int.Parse).ToArray();
        int A1 = input1[0];
        int B1 = input1[1];
        Console.WriteLine($"{B1 - A1} {B1}");
    }
}