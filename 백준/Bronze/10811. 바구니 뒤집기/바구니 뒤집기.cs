using System;
using System.Collections.Generic; //HashSet을 사용하기 위해 필요
using System.Linq; //Linq를 사용하기 위해 필요
using System.Text; // StringBuilder를 사용하기 위해 필요

class Program
{
    static void Main(string[] args)
    {
        StringBuilder sb = new StringBuilder();
        var input = Console.ReadLine().Split().Select(int.Parse).ToArray();
        int N = input[0], M = input[1];
        var array = Enumerable.Range(1, N).ToArray();
        for (int i = 0; i < M; i++) {
            var cmd = Console.ReadLine().Split().Select(int.Parse).ToArray();
            int I = cmd[0], J = cmd[1];
            Array.Reverse(array, I - 1, J - I + 1);
        }
        sb.Append(string.Join(" ", array));
        Console.WriteLine(sb.ToString());
    }
}
