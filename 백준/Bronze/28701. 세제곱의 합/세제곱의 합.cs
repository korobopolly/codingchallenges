using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

class Program
{
    static void Main(string[] args)
    {
        int N = int.Parse(Console.ReadLine());
        int pow1 = 0;
        int pow3 = 0;
        for (int i = 1; i < N + 1; i++) {
            pow1 += i;
            pow3 += i * i * i;
        }
        Console.WriteLine(pow1);
        Console.WriteLine(Math.Pow(pow1, 2));
        Console.WriteLine(pow3);
    }
}