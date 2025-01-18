using System;
using System.Linq;

class Program
{
    static void Main(string[] args)
    {
        int total = int.Parse(Console.ReadLine());
        int N = int.Parse(Console.ReadLine());
        int[] sum = new int[N];
        for (int i = 0; i < N; i++) {
            var input = Console.ReadLine().Split().Select(int.Parse).ToArray();
            sum[i] = input[0] * input[1];
        }
        Console.WriteLine(total == sum.Sum() ? "Yes" : "No");
    }
}
