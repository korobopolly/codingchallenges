using System;
using System.Linq;
using System.Text; // StringBuilder를 사용하기 위해 필요

class Program
{
    static void Main(string[] args)
    {
        StringBuilder sb = new StringBuilder();
        int[] input_nm = Console.ReadLine().Split().Select(int.Parse).ToArray();
        int N = input_nm[0];
        int M = input_nm[1];
        int[] baskets = new int[N];
        for (int i = 0; i < M; i++)
        {
            int[] input_ijk = Console.ReadLine().Split().Select(int.Parse).ToArray();
            int I = input_ijk[0];
            int J = input_ijk[1];
            int K = input_ijk[2];
            for (int j = I-1; j < J; j++) {
                baskets[j] = K;
            }
        }
        sb.Append(string.Join(' ', baskets));
        Console.WriteLine(sb.ToString());
    }
}
