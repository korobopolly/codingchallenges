using System;
using System.Linq;
using System.Text; // StringBuilder를 사용하기 위해 필요

class Program
{
    static void Main(string[] args)
    {
        StringBuilder sb = new StringBuilder();
        int[] input = Console.ReadLine().Split().Select(int.Parse).ToArray();
        int[] numbers = Console.ReadLine().Split().Select(int.Parse).ToArray();
        int N = input[0];
        int X = input[1];

        var result = numbers.Where(n => n < X).ToArray();
        sb.Append(string.Join(" ", result));
        Console.WriteLine(sb.ToString());
    }
}
