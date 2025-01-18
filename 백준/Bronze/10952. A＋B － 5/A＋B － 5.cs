using System;
using System.Linq;
using System.Text; // StringBuilder를 사용하기 위해 필요

class Program
{
    static void Main(string[] args)
    {
        StringBuilder sb = new StringBuilder();
        while (true) { 
            var input = Console.ReadLine().Split().Select(int.Parse).ToArray();
            if (input.Sum() == 0)
                break;
            sb.AppendLine(input.Sum().ToString());
        }
        Console.WriteLine(sb.ToString());
    }
}
