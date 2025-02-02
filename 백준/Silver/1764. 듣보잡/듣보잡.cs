using System;
using System.Collections.Generic; //HashSet을 사용하기 위해 필요
using System.Collections.Immutable;
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
        var notlisten = new HashSet<string>();
        var both = new HashSet<string>();
        for (int i = 0; i < N; i++) {
            notlisten.Add(Console.ReadLine());
        }
        for (int j = 0; j < M; j++)
        {
            string notseen = Console.ReadLine();
            if (notlisten.Contains(notseen)) {
                both.Add(notseen);
            }
        }
        Console.WriteLine(both.Count);
        Console.WriteLine(string.Join("\n", both.OrderBy(x => x)));
    }
}
