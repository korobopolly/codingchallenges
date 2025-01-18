using System;
using System.Linq;
using System.Text; // StringBuilder를 사용하기 위해 필요

class Program
{
    static void Main(string[] args)
    {
        StringBuilder sb = new StringBuilder();
        int N = int.Parse(Console.ReadLine());
        for (int i = 0; i < N; i++) {
            var input = Console.ReadLine().Split().Select(int.Parse).ToArray();
            sb.AppendLine($"Case #{i+1}: {input[0]} + {input[1]} = {(input[0] + input[1])}");
        }
        Console.WriteLine(sb.ToString());
    }
}
