using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;

class Program2
{
    static void Main(string[] args)
    {
        var input = Console.ReadLine().Split().Select(double.Parse).ToArray();
        double N = input[0];
        double A = input[1];
        double B = input[2];
        double MAX = Math.Pow(10, 6);
        string x;
        double y;

        if (N > B) {
            y = MAX;
        }
        else if (N == B)
        {
            y = N;
        }
        else
        {
            y = B;
        }

        if (A > y)
        {
            x = "Subway";
        }
        else if (A == y) {
            x = "Anything";
        }
        else
        {
            x = "Bus";
        }

        Console.WriteLine(x);
    }
}