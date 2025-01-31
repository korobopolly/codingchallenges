using System;
using System.Collections.Generic; //HashSet을 사용하기 위해 필요
using System.Linq; //Linq를 사용하기 위해 필요
using System.Text; // StringBuilder를 사용하기 위해 필요

class Program
{ 
    static void Main(string[] args)
    {
        StringBuilder sb = new StringBuilder();
        int N = int.Parse(Console.ReadLine());
        var line = new HashSet<int>(Console.ReadLine().Split().Select(int.Parse)); // HashSet으로 변경
        int M = int.Parse(Console.ReadLine());
        var cmd = Console.ReadLine().Split().Select(int.Parse).ToList();

        foreach (var num in cmd)
        {
            if (line.Contains(num))
            {
                sb.Append("1 ");
            }
            else
            {
                sb.Append("0 ");
            }
        }
        Console.WriteLine(sb);
    }
}
