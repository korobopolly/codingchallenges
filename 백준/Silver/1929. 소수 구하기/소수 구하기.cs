using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;

class Program
{
    static void Main(string[] args)
    { 
        var input = Console.ReadLine().Split().Select(int.Parse).ToArray();
        int M = input[0];
        int N = input[1];
        bool[] IsPrime = new bool[N + 1];
        Eratosthenes(N, IsPrime);
        for (int i = M; i <= N; i++) {
            if (IsPrime[i]) Console.WriteLine(i);
        }
    }

    static void Eratosthenes(int n, bool[] isPrime)
    {
        for (int i = 2; i <= n; i++) isPrime[i] = true;
        
        for (int i = 2; i * i <= n; i++)
        {
            if (isPrime[i])
            {
                for (int j = i * i; j <= n; j += i) { 
                    isPrime[j] = false;
                }
            }
        }
    }
}