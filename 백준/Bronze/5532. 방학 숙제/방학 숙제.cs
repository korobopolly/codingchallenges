using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

class Program
{
    static void Main(string[] args)
    {
        double L = double.Parse(Console.ReadLine());
        double A = double.Parse(Console.ReadLine());
        double B = double.Parse(Console.ReadLine());
        double C = double.Parse(Console.ReadLine());
        double D = double.Parse(Console.ReadLine());
        int work = (int)Math.Ceiling(A / C > B / D ? A / C : B / D);
        Console.WriteLine(L - work);
    }
}