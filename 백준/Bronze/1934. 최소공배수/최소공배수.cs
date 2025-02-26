using System;
using System.Linq;
using System.Collections.Generic;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            int N = int.Parse(Console.ReadLine());
            for (int i = 0; i < N; i++)
            {
                var input = Console.ReadLine().Split().Select(int.Parse).ToArray();
                int A = input[0];
                int B = input[1];
                int LCM = A / GCD(A, B) * B;
                Console.WriteLine(LCM);
            }
        }

        //유클리드 호제법 (GCD 최대공약수, LCM 최소공배수)
        static int GCD(int a, int b)
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
