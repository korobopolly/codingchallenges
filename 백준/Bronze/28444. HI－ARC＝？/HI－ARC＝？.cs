using System;
using System.Collections.Generic;
using System.Linq;
using System.Numerics;
using System.Text;

class Program
{
    static void Main(string[] args)
    {
        var input = Console.ReadLine().Split().Select(int.Parse).ToArray();
        int H = input[0];
        int I = input[1];
        int A = input[2];
        int R = input[3];
        int C = input[4];

        Console.WriteLine(H * I - A * R * C);
    }
}