using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

class Program
{
    static void Main(string[] args)
    {
        int N = int.Parse(Console.ReadLine());

        for (int i = 0; i <= N / 3; i++) { 
            for (int j = 0; j <= N / 5; j++)
            {
                if (N - (5 * j) - (3 * i) == 0)
                {
                    Console.WriteLine(i + j);
                    return;
                }
            }
        }
        Console.WriteLine("-1");
    }
}
