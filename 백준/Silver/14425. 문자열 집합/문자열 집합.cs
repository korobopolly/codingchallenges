using System;
using System.Collections.Generic; //HashSet을 사용하기 위해 필요
using System.Linq; //Linq를 사용하기 위해 필요
using System.Numerics;
using System.Text; // StringBuilder를 사용하기 위해 필요

class Program
{ 
    static void Main(string[] args)
    {
        var input = Console.ReadLine().Split().Select(int.Parse).ToArray();
        int N = input[0];
        int M = input[1];
        var hash = new HashSet<string>();
        int result = 0;
        for (int i = 0; i < N; i++) {
            hash.Add(Console.ReadLine());
        }
        for (int j = 0; j < M; j++)
        {
            if (hash.Contains(Console.ReadLine())) {
                result += 1;
            }
        }
        Console.WriteLine(result);
    }
}
