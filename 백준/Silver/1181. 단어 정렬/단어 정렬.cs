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
        var hashSet = new HashSet<string>();
        for (int i = 0; i < N; i++) {
            hashSet.Add(Console.ReadLine());
        }
        var sortedList = hashSet
            .OrderBy(x => x.Length)
            .ThenBy(x => x)
            .ToList();
        sb.AppendLine(string.Join("\n", sortedList));
        Console.WriteLine(sb);
    }
}
