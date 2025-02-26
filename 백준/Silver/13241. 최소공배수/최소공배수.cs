using System;
using System.Linq;
using System.Collections.Generic;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            var input = Console.ReadLine().Split().Select(long.Parse).ToArray();
            long A = input[0];
            long B = input[1];
            long LCM = A / GCD(A, B) * B;
            Console.WriteLine(LCM);
        }

        //유클리드 호제법 (GCD 최대공약수, LCM 최소공배수)
        static long GCD(long a, long b)
        {
            if (b > a) { (a, b) = (b, a); }
            while(b != 0)
            {
                (a, b) = (b, a % b);
            }
            return a;
        }
    }
}
