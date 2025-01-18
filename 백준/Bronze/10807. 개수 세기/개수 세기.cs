using System;
using System.Linq;
using System.Text; // StringBuilder를 사용하기 위해 필요

class Program
{
    static void Main(string[] args)
    {
        StringBuilder sb = new StringBuilder();
        int N = int.Parse(Console.ReadLine());
        int[] numbers = Console.ReadLine().Split().Select(int.Parse).ToArray();
        int v = int.Parse(Console.ReadLine());
        int count = numbers.Count(x => x == v);
        sb.Append(count);
        Console.WriteLine(sb.ToString());
    }
}
