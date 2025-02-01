using System;
using System.Collections.Generic; //HashSet을 사용하기 위해 필요
using System.Linq; //Linq를 사용하기 위해 필요
using System.Numerics;
using System.Text; // StringBuilder를 사용하기 위해 필요

class Program
{
    static void Main(string[] args)
    {
        int N = int.Parse(Console.ReadLine());
        var hash = new HashSet<string>();
        for (int i = 0; i < N; i++)
        {
            var line = Console.ReadLine().Split();
            if (line[1] == "enter") hash.Add(line[0]);
            else if (line[1] == "leave") hash.Remove(line[0]);
        }
        var result = hash.OrderByDescending(x => x).ToList();
        Console.WriteLine(string.Join("\n",result));
    }
}
