using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

class Program
{
    static void Main(string[] args)
    {
        int N = int.Parse(Console.ReadLine());
        double s = Math.Sqrt(3) / 4 * N * N;
        Console.WriteLine(s);
    }
}