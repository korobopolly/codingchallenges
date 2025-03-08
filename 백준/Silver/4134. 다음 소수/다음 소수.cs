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
        var list = new List<long>();
        for (int i = 0; i < N; i++)
        {
            long input = long.Parse(Console.ReadLine());
            for (long j = input; true; j++)
            {
                if (IsPrime(j))
                {
                    Console.WriteLine(j);
                    break;
                };
            }
        }
    }

    static long GCD(long a, long b) {
        if (b > a) { (a, b) = (b, a); }
        while (b != 0)
        {
            (a, b) = (b, a % b);
        }
        return (a);
    }

    static bool IsPrime(long n)
    {
        if (n < 2) return false;
        if (n == 2) return true;
        if (n % 2 == 0) return false;

        for (long i = 3; i * i <= n; i += 2) // 홀수만 검사
        {
            if (n % i == 0) return false;
        }
        return true;
    }
}