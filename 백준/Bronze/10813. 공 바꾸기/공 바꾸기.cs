using System;
using System.Linq;
using System.Text; // StringBuilder를 사용하기 위해 필요

class Program
{
    static void Main(string[] args)
    {
        StringBuilder sb = new StringBuilder();
        int[] input = Console.ReadLine().Split().Select(int.Parse).ToArray();
        int N = input[0];
        int M = input[1];
        int[] baskets = new int[N];
        for (int i = 0; i < N; i++)
        {
            baskets[i] = i+1;
        }
        for (int j = 0; j < M; j++)
        {
            int[] cmd = Console.ReadLine().Split().Select(int.Parse).ToArray();
            int I = cmd[0]-1;
            int J = cmd[1]-1;
            int temp = baskets[I];
            baskets[I] = baskets[J];
            baskets[J] = temp;
        }
        sb.Append(string.Join(' ', baskets));
        Console.WriteLine(sb.ToString());
    }
}
