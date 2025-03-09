using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

class Program
{
    static void Main(string[] args)
    {
        long N = int.Parse(Console.ReadLine());
        long factorial = 1;
        for (long i = 1; i < N + 1; i++) {
            factorial *= i;
        }
        Console.WriteLine(factorial / (3628800 / 6));
    }
}