using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;

class Program
{
    static void Main(string[] args)
    {
        int N = int.Parse(Console.ReadLine());
        var list = new List<int>();
        var diff_list = new List<int>();
        for (int i = 0; i < N; i++)
        {
            int input = int.Parse(Console.ReadLine());
            list.Add(input);
        }

        for (int j = 0; j < N - 1; j++)
        {
            diff_list.Add(list[j + 1] - list[j]);
        }

        int diff_gcd = diff_list.Aggregate((acc, num) => GCD(acc, num));
        int num = (list[^1] - list[0]) / diff_gcd + 1;
        Console.WriteLine(num - list.Count());
    }

    static int GCD(int a, int b) {
        if (b > a) { (a, b) = (b, a); }
        while (b != 0)
        {
            (a, b) = (b, a % b);
        }
        return a;
    }

}