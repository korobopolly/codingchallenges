using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using System.Runtime.Intrinsics.X86;
using System.Text;

class Program
{
    static void Main(string[] args)
    {
        while (true)
        {
            int n = int.Parse(Console.ReadLine());
            if (n == 0) break;

            int n2 = n * 2;
            bool[] IsPrime = new bool[n2 + 1];
            int cnt = 0;
            Eratosthenes(n2, IsPrime);
            for (int i = n + 1; i <= n2; i++)
            {
                if (IsPrime[i]) cnt += 1;
            }
            Console.WriteLine(cnt);
        }
    }

    static void Eratosthenes(int n, bool[] isPrime)
    {
        for (int i = 2; i <= n; i++) isPrime[i] = true;

        for (int i = 2; i * i <= n; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j <= n; j += i) {
                    isPrime[j] = false;
                }    
            }
        }
    }
}